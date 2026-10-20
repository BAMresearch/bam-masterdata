from types import SimpleNamespace

import pytest
from openpyxl import Workbook

from bam_masterdata.cli.entities_to_excel import entities_to_excel
from bam_masterdata.metadata import definitions
from tests.conftest import InstrumentObjectType, MockedObjectTypeLonger


class OptionalInstrumentName(InstrumentObjectType):
    name = InstrumentObjectType.name.model_copy(update={"mandatory": False})


@pytest.mark.parametrize(
    "entity,expected_codes,name_required",
    [
        (
            MockedObjectTypeLonger,
            ["$NAME", "ALIAS", "SETTINGS", "$STORAGE.STORAGE_VALIDATION_LEVEL"],
            True,
        ),
        (InstrumentObjectType, ["$NAME", "RESPONSIBLE_PERSON"], True),
        (OptionalInstrumentName, ["$NAME", "RESPONSIBLE_PERSON"], False),
    ],
)
def test_export_preserves_every_property_row(
    monkeypatch, entity, expected_codes, name_required
):
    monkeypatch.setattr(
        "bam_masterdata.cli.entities_to_excel.import_module",
        lambda module_path: SimpleNamespace(ExportedType=entity),
    )
    worksheet = Workbook().active

    entities_to_excel(worksheet, "test-module.py", definitions)

    rows = list(worksheet.values)
    assert not any(rows[-1])
    assert rows[3][0] == "Code"
    properties = rows[4:-1]
    assert [row[0] for row in properties] == expected_codes
    headers = list(rows[3])
    name = next(row for row in properties if row[0] == "$NAME")
    assert name[headers.index("Mandatory")] is name_required
    if issubclass(entity, InstrumentObjectType):
        target = next(row for row in properties if row[0] == "RESPONSIBLE_PERSON")
        assert target[headers.index("Data type")] == "SAMPLE:PERSON"
