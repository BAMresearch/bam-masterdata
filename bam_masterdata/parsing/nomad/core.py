"""Offline NOMAD archive handling; source-schema semantics belong in mappings.

This module deliberately has no datamodel or domain imports. See the mapping guide
for the supported JSON/reference forms and the deliberately explicit unit policy.
"""

import base64
import hashlib
import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any, Protocol

from pint import UnitRegistry

from bam_masterdata.metadata.definitions import PropertyTypeAssignment
from bam_masterdata.metadata.entities import CollectionType, ObjectType
from bam_masterdata.parsing.parsing import AbstractParser

_UNITS = UnitRegistry()
_MISSING = object()
_ARCHIVE_REFERENCE = re.compile(r"\.\./uploads/([^/]+)/archive/([^/#]+)#(.*)")


class MappingError(ValueError):
    """A source cannot be mapped without losing or inventing information."""


def entry_id(upload_id: str, mainfile: str, mainfile_key: str | None = None) -> str:
    """NOMAD's SHA-512/websafe identity recipe, without a NOMAD dependency.

    Mirrors nomad.utils.generate_entry_id/hash (28-character default). Mainfile
    is the exact path relative to the upload's raw directory, not a guessed name.
    """
    content = upload_id + mainfile + (mainfile_key or "")
    return base64.urlsafe_b64encode(hashlib.sha512(content.encode()).digest())[
        :28
    ].decode()


@dataclass(frozen=True)
class ArchiveSource:
    """Explicit identity for a data-only archive or an override checked against metadata."""

    path: str | Path
    upload_id: str
    mainfile: str
    entry_id: str | None = None
    mainfile_key: str | None = None

    def __post_init__(self):
        if not self.upload_id or not self.mainfile:
            raise MappingError("ArchiveSource requires upload_id and exact mainfile")
        mainfile = PurePosixPath(self.mainfile)
        if mainfile.is_absolute() or ".." in mainfile.parts or "\\" in self.mainfile:
            raise MappingError(f"Invalid upload-relative mainfile: {self.mainfile!r}")

    @property
    def identity(self) -> tuple[str, str]:
        return self.upload_id, self.entry_id or entry_id(
            self.upload_id, self.mainfile, self.mainfile_key
        )


@dataclass(frozen=True, order=True)
class SourceKey:
    upload_id: str
    entry_id: str
    pointer: str = "/data"

    def __str__(self):
        return f"nomad://{self.upload_id}/{self.entry_id}#{self.pointer}"


@dataclass
class Archive:
    source: ArchiveSource
    document: dict
    consumed: set[str] = field(default_factory=set)

    def key(self, pointer="/data") -> SourceKey:
        return SourceKey(*self.source.identity, pointer)


@dataclass(frozen=True)
class Diagnostic:
    code: str
    source: str
    pointer: str
    message: str


@dataclass(frozen=True)
class Relationship:
    parent: SourceKey
    child: SourceKey
    role: str
    source_pointer: str
    qualifiers: dict
    provenance: bool = True


@dataclass
class MappingReport:
    objects: dict[SourceKey, ObjectType]
    relationships: list[Relationship]
    diagnostics: list[Diagnostic]

    def to_json(self, *, indent=None) -> str:
        """Serialize values and OBJECT identities without recursively nesting objects."""
        objects = []
        for key, obj in sorted(self.objects.items()):
            values = {}
            for name, metadata in obj._property_metadata.items():
                value = getattr(obj, name)
                if isinstance(value, PropertyTypeAssignment):
                    continue
                values[metadata.code] = (
                    value.code if isinstance(value, ObjectType) else value
                )
            objects.append(
                {
                    "source": str(key),
                    "type": obj.defs.code,
                    "code": obj.code,
                    "properties": values,
                }
            )
        return json.dumps(
            {
                "objects": objects,
                "relationships": [
                    {
                        "parent": str(r.parent),
                        "child": str(r.child),
                        "role": r.role,
                        "source_pointer": r.source_pointer,
                        "qualifiers": r.qualifiers,
                        "provenance": r.provenance,
                    }
                    for r in self.relationships
                ],
                "diagnostics": [vars(d) for d in self.diagnostics],
            },
            sort_keys=True,
            ensure_ascii=False,
            allow_nan=False,
            indent=indent,
        )


def _pointer(document, pointer):
    if pointer == "":
        return document
    if not pointer.startswith("/"):
        raise MappingError(f"Unsupported section pointer: {pointer!r}")
    value = document
    try:
        for token in pointer[1:].split("/"):
            token = token.replace("~1", "/").replace("~0", "~")
            value = value[int(token)] if isinstance(value, list) else value[token]
    except (KeyError, IndexError, ValueError, TypeError) as exc:
        raise MappingError(f"Unresolved section pointer: {pointer}") from exc
    return value


def _leaves(value, prefix=""):
    if isinstance(value, dict) and value:
        for key, item in value.items():
            yield from _leaves(
                item, prefix + "/" + key.replace("~", "~0").replace("/", "~1")
            )
    elif isinstance(value, list) and value:
        for index, item in enumerate(value):
            yield from _leaves(item, f"{prefix}/{index}")
    else:
        yield prefix


class ArchiveContext:
    """A mapping's local identity index, conversion tools, and qualified graph."""

    def __init__(self, archives: list[Archive], mapping_id: str, target_version: str):
        self.archives = archives
        self.mapping_id = mapping_id
        self.target_version = target_version
        self.index = {archive.source.identity: archive for archive in archives}
        self.objects: dict[SourceKey, ObjectType] = {}
        self.relationships: list[Relationship] = []
        self.diagnostics: list[Diagnostic] = []
        self._bindings: list[tuple[SourceKey, str, SourceKey]] = []
        self._profiles: dict[SourceKey, str | None] = {}

    def value(self, archive: Archive, pointer: str, default=_MISSING):
        try:
            value = _pointer(archive.document, pointer)
        except MappingError:
            if default is _MISSING:
                raise MappingError(
                    f"{archive.source.path}: missing mandatory value {pointer}"
                ) from None
            return default
        archive.consumed.add(pointer)
        return value

    def required_text(self, archive: Archive, pointer: str) -> str:
        value = self.value(archive, pointer)
        if not isinstance(value, str) or not value.strip():
            raise MappingError(
                f"{archive.source.path}: missing mandatory text {pointer}"
            )
        return value

    def diagnostic(self, archive: Archive, pointer: str, code: str, message: str):
        self.diagnostics.append(Diagnostic(code, str(archive.key()), pointer, message))

    def quantity(self, value, source_unit: str, target_unit: str) -> float:
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(value)
        ):
            raise MappingError(f"Expected a finite numeric quantity, got {value!r}")
        try:
            return float(_UNITS.Quantity(value, source_unit).to(target_unit).magnitude)
        except Exception as exc:
            raise MappingError(
                f"Unsupported conversion {source_unit!r} -> {target_unit!r}"
            ) from exc

    def create(
        self,
        archive: Archive,
        cls: type[ObjectType],
        values: dict,
        *,
        pointer="/data",
        profile=None,
    ) -> SourceKey:
        key = archive.key(pointer)
        if key in self.objects:
            raise MappingError(f"Duplicate mapped section: {key}")
        digest = hashlib.sha256(
            f"{self.mapping_id}|{self.target_version}|{key}".encode()
        ).hexdigest()[:32]
        obj = cls(code=f"NOMAD_{digest.upper()}", **values)
        for name, prop in obj._property_metadata.items():
            value = getattr(obj, name, None)
            # A required OBJECT may be bound in the second mapping pass, after
            # every source identity has been materialized. Other required values
            # must already be supplied; all OBJECT requirements are checked below
            # in finalize, after deferred bindings and before collection mutation.
            if (
                prop.mandatory
                and prop.data_type != "OBJECT"
                and (
                    isinstance(value, PropertyTypeAssignment)
                    or value is None
                    or value == ""
                )
            ):
                raise MappingError(f"{key}: missing mandatory target value {name}")
        self.objects[key] = obj
        self._profiles[key] = profile
        return key

    def resolve(self, archive: Archive, reference: str) -> SourceKey:
        if not isinstance(reference, str):
            raise MappingError(f"{archive.source.path}: reference must be a string")
        if reference.startswith("#"):
            identity, fragment = archive.source.identity, reference[1:]
        else:
            match = _ARCHIVE_REFERENCE.fullmatch(reference)
            if not match:
                raise MappingError(f"Unsupported archive reference: {reference!r}")
            identity, fragment = (match[1], match[2]), match[3]
        if fragment == "data":
            fragment = "/data"
        target = self.index.get(identity)
        if target is None:
            raise MappingError(f"Unresolved archive reference: {reference}")
        _pointer(target.document, fragment)
        key = target.key(fragment)
        if key not in self.objects:
            raise MappingError(
                f"Reference does not identify a mapped object: {reference}"
            )
        return key

    def relate(
        self,
        parent: SourceKey,
        child: SourceKey,
        *,
        role: str,
        source_pointer: str,
        qualifiers=None,
        provenance=True,
    ):
        if parent not in self.objects or child not in self.objects:
            raise MappingError("Relationship endpoints must identify mapped objects")
        self.relationships.append(
            Relationship(
                parent, child, role, source_pointer, qualifiers or {}, provenance
            )
        )

    def reference(
        self,
        archive: Archive,
        owner: SourceKey,
        pointer: str,
        *,
        attribute=None,
        role: str,
        qualifiers=None,
        provenance=True,
    ) -> SourceKey:
        target = self.resolve(archive, self.value(archive, pointer))
        self.relate(
            target,
            owner,
            role=role,
            source_pointer=pointer,
            qualifiers=qualifiers,
            provenance=provenance,
        )
        if attribute:
            self._bindings.append((owner, attribute, target))
        return target

    def finalize(self) -> tuple[CollectionType, MappingReport]:
        """Validate graph and build a temporary collection before exposing results."""
        for owner, attribute, target in self._bindings:
            obj, referenced = self.objects[owner], self.objects[target]
            prop = obj._property_metadata[attribute]
            if prop.data_type != "OBJECT" or prop.object_code != referenced.defs.code:
                raise MappingError(
                    f"{owner}.{attribute}: exact target {prop.object_code!r} does not match {referenced.defs.code!r}"
                )
            setattr(obj, attribute, referenced)

        for key, obj in self.objects.items():
            for name, prop in obj._property_metadata.items():
                value = getattr(obj, name, None)
                if (
                    prop.mandatory
                    and prop.data_type == "OBJECT"
                    and (
                        isinstance(value, PropertyTypeAssignment)
                        or value is None
                        or value == ""
                    )
                ):
                    raise MappingError(f"{key}: missing mandatory target value {name}")

        # Order scalar references before owners, independent of source ordering.
        dependencies = {key: set() for key in self.objects}
        for owner, _, target in self._bindings:
            dependencies[owner].add(target)
        ordered = []
        while dependencies:
            ready = sorted(key for key, deps in dependencies.items() if not deps)
            if not ready:
                raise MappingError("Cyclic OBJECT references are unsupported")
            ordered.extend(ready)
            for key in ready:
                del dependencies[key]
            for deps in dependencies.values():
                deps.difference_update(ready)

        for archive in self.archives:
            retained = sorted(
                path
                for path in _leaves(archive.document)
                if not any(
                    path == used or path.startswith(used + "/")
                    for used in archive.consumed
                )
            )
            if retained:
                self.diagnostic(archive, "", "retained_fields", ", ".join(retained))
            # A lab identifier is a claim, not a cross-file deduplication key.
            lab_id = archive.document["data"].get("lab_id")
            if (
                lab_id
                and sum(
                    a.document["data"].get("lab_id") == lab_id for a in self.archives
                )
                > 1
            ):
                self.diagnostic(
                    archive,
                    "/data/lab_id",
                    "duplicate_lab_id",
                    "Distinct archives retain distinct source identities",
                )
            for key in self.objects:
                if (key.upload_id, key.entry_id) != archive.source.identity:
                    continue
                obj = self.objects[key]
                if "source_record" not in obj._property_metadata:
                    raise MappingError(f"{key}: target has no SOURCE_RECORD assignment")
                relations = [
                    {
                        "parent": str(r.parent),
                        "child": str(r.child),
                        "role": r.role,
                        "source_pointer": r.source_pointer,
                        "qualifiers": r.qualifiers,
                        "provenance": r.provenance,
                    }
                    for r in self.relationships
                    if key in (r.parent, r.child)
                ]
                obj.source_record = json.dumps(
                    {
                        "source": str(key),
                        "upload_id": key.upload_id,
                        "entry_id": key.entry_id,
                        "mainfile": archive.source.mainfile,
                        "mainfile_key": archive.source.mainfile_key,
                        "pointer": key.pointer,
                        "mapping": self.mapping_id,
                        "target_version": self.target_version,
                        "quantity_profile": self._profiles[key],
                        "archive": archive.document,
                        "retained_fields": retained,
                        "relationships": relations,
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                    allow_nan=False,
                )
        temporary = CollectionType()
        ids = {key: temporary.add(self.objects[key]) for key in ordered}
        for relationship in self.relationships:
            if relationship.provenance:
                temporary.add_relationship(
                    ids[relationship.parent], ids[relationship.child]
                )
        return temporary, MappingReport(
            self.objects, self.relationships, self.diagnostics
        )


class NomadMapping(Protocol):
    mapping_id: str
    target_version: str

    def map(self, context: ArchiveContext) -> None: ...


class NomadParser(AbstractParser):
    """Map a supplied archive batch offline, then append its validated graph."""

    def __init__(self, mapping: NomadMapping, sources=(), *, exclude=None):
        self.mapping = mapping
        self.sources = {Path(source.path).resolve(): source for source in sources}
        # Explicit exclusions are paths plus reasons; no filename-based filtering.
        self.exclude = {
            Path(path).resolve(): reason for path, reason in (exclude or {}).items()
        }
        if any(
            not isinstance(reason, str) or not reason.strip()
            for reason in self.exclude.values()
        ):
            raise MappingError("Every explicit exclusion requires a reason")
        self.report: MappingReport | None = None

    def parse(self, files, collection, logger):
        self.report = None
        archives = {}
        exclusions = []
        for path in sorted({Path(path).resolve() for path in files}):
            if path in self.exclude:
                exclusions.append(
                    Diagnostic("excluded", str(path), "", self.exclude[path])
                )
                continue
            try:
                document = json.loads(
                    path.read_text(encoding="utf-8"),
                    parse_constant=lambda value: (_ for _ in ()).throw(
                        MappingError(f"Non-finite JSON number: {value}")
                    ),
                )
            except (OSError, json.JSONDecodeError) as exc:
                raise MappingError(f"{path}: cannot read JSON archive: {exc}") from exc
            if not isinstance(document, dict) or not isinstance(
                document.get("data"), dict
            ):
                raise MappingError(f"{path}: expected archive object containing data")
            metadata = document.get("metadata", {})
            if not isinstance(metadata, dict):
                raise MappingError(f"{path}: metadata must be an object")
            source = self.sources.get(path)
            if source is None:
                try:
                    source = ArchiveSource(
                        path,
                        metadata["upload_id"],
                        metadata["mainfile"],
                        metadata.get("entry_id"),
                        metadata.get("mainfile_key"),
                    )
                except KeyError as exc:
                    raise MappingError(
                        f"{path}: missing source identity; supply ArchiveSource"
                    ) from exc
            for name, expected in (
                ("upload_id", source.upload_id),
                ("entry_id", source.identity[1]),
                ("mainfile", source.mainfile),
                ("mainfile_key", source.mainfile_key),
            ):
                if name in metadata and metadata[name] != expected:
                    raise MappingError(f"{path}: conflicting source metadata {name}")
            previous = archives.get(source.identity)
            if previous:
                if previous.document != document:
                    raise MappingError(
                        f"{path}: duplicate source identity with conflicting content"
                    )
                exclusions.append(
                    Diagnostic(
                        "duplicate_input",
                        str(path),
                        "",
                        "Identical archive identity/content included once",
                    )
                )
            else:
                archives[source.identity] = Archive(source, document)
        context = ArchiveContext(
            sorted(archives.values(), key=lambda archive: archive.key()),
            self.mapping.mapping_id,
            self.mapping.target_version,
        )
        self.mapping.map(context)
        temporary, report = context.finalize()
        if any(
            obj.code
            in {existing.code for existing in collection.attached_objects.values()}
            for obj in report.objects.values()
        ):
            raise MappingError(
                "Mapped object code already exists in supplied collection"
            )
        # All operations that can fail scientific validation completed above.
        collection.attached_objects.update(temporary.attached_objects)
        collection.relationships.update(temporary.relationships)
        report.diagnostics.extend(exclusions)
        self.report = report
        for diagnostic in report.diagnostics:
            logger.warning(
                f"NOMAD {diagnostic.code}: {diagnostic.source}{diagnostic.pointer}: {diagnostic.message}"
            )
