# How to define a type

Notes for writing the v1 datamodel by hand. Start at the top; the last section is
reference material you only need once you hit a problem.

## What you are actually doing

openBIS is the lab database. Before anyone can save "an experiment" into it, openBIS has
to be told **what an experiment is**: which fields it has, and what kind of data each
field holds. That description is called a **type**.

In this repo we write those descriptions as Python classes, and a separate tool reads them
and creates the matching types inside openBIS. So this is not really programming — it is
**filling in a form, where Python syntax is the form.** Almost all of the work is copying
a block and changing the text inside it.

## The shape of a type

Every type is one class with two kinds of things inside it:

```python
class Experiment(Activity):        # 1. the type's name, and the type it builds on

    defs = ObjectTypeDef(          # 2. facts about the type itself — exactly one of these
        code="ACTIVITY.EXPERIMENT",
        description="""Experiment//Experiment""",
        generated_code_prefix="ACT.EXP",
    )

    method_name = PropertyTypeAssignment(   # 3. one field — as many of these as you need
        code="METHOD_NAME",
        data_type="VARCHAR",
        property_label="Method name",
        description="""Name of the experimental method//Name der experimentellen Methode""",
        mandatory=False,
        section="Experiment Details",
    )
```

- `defs = ObjectTypeDef(...)` means *"here is the type."* Every class has exactly one.
- `something = PropertyTypeAssignment(...)` means *"here is one field on that type."*
  Repeat it once per field.

The name on the left (`method_name`) is how Python refers to the field. The `code` on the
right (`METHOD_NAME`) is how openBIS refers to it. Keep them matching — lowercase on the
left, UPPERCASE on the right.

## Filling in a field

Six arguments are **required**. Leave one out and Python raises an error telling you which:

| Argument | What to put |
|---|---|
| `code` | The openBIS name. `ALL_CAPS_WITH_UNDERSCORES`, always. |
| `description` | `"""English//Deutsch"""` — both languages, separated by `//`. BAM convention. |
| `data_type` | What kind of data it holds. See the table below. |
| `property_label` | What a scientist reads next to the box in the openBIS UI. |
| `mandatory` | `True` if it cannot be left blank, otherwise `False`. |
| `section` | Which box in the UI it appears in, e.g. `"General Information"`. |

### The data types

| `data_type` | Use it for |
|---|---|
| `VARCHAR` | short text (one line) |
| `MULTILINE_VARCHAR` | long text (a paragraph) |
| `INTEGER` | whole numbers |
| `REAL` | decimal numbers |
| `BOOLEAN` | yes / no |
| `DATE` | a date |
| `TIMESTAMP` | a date *and* a time |
| `HYPERLINK` | a URL |
| `XML` | structured XML |
| `CONTROLLEDVOCABULARY` | a dropdown with fixed choices |
| `OBJECT` | a link to another object type |
| `SAMPLE` | a link to a sample |

Two of those need a **second argument**, or the type is incomplete:

```python
data_type="CONTROLLEDVOCABULARY"  →  also pass  vocabulary_code="SOME_VOCAB"
data_type="OBJECT"                →  also pass  object_code="SOME_OBJECT"
```

### Optional arguments

The common one is `units`:

```python
units="mm"
```

**It rewrites your label for you.** With `property_label="Length"` and `units="mm"`, the
final label becomes `Length in [mm]`. Do not type the unit into the label yourself or you
will end up with `Length in [mm] in [mm]`.

Others you will rarely need: `show_in_edit_views` (default `True`), `ordinal`, `unique`,
`metadata`, `internal_assignment`, `iri`, `dynamic_script`.

## Building on another type

`class Experiment(Activity)` means Experiment **gets all of Activity's fields for free**.
So inside `Experiment` you only write the fields that are new to Experiment — never repeat
the parent's.

The current hierarchy:

```
Root
├── Activity
│   ├── Experiment    (activities.py)
│   └── Computation   (activities.py)
└── Entity
```

Three things to get right on a child type:

1. **`code` mirrors the hierarchy with dots:** `ACTIVITY.EXPERIMENT`. This is only a
   naming habit — see the note below.
2. **Always set `generated_code_prefix` yourself** on a child. If you omit it, it defaults
   to the first three letters of the code, which for `ACTIVITY.EXPERIMENT` gives `ACT` —
   the same as the parent. Set `ACT.EXP`.
3. **Never set `id`.** It is worked out from the code automatically.

> **Why the dots are only a habit:** openBIS has no inheritance of its own. When the
> exporter runs, it copies every inherited field into the child, so what actually reaches
> openBIS is one flat list. `Experiment` ships with `start_date`, `end_date`, … *and*
> `method_name`. The dotted code just keeps the names readable for humans.

## Three traps

These produce no error message, which is what makes them expensive.

### 1. Never reuse a field name from a parent

If `Activity` has `start_date` and you also write `start_date` in `Experiment`, you do not
override it — you get the field **twice**, and the parent's version is the one that wins.
Treat every field name used by a parent as taken.

### 2. A misspelled argument is thrown away silently

These models ignore any argument they do not recognise — pydantic is left on its default
`extra="ignore"`. What happens next depends on whether the argument was required.

**Misspell one of the six required arguments and you do get an error**, but it points at
the wrong thing:

```python
property_lable="Length"        # typo
# → ValidationError: property_label | Field required
```

The typo is discarded, and *then* the required `property_label` is found to be missing. So
the message says "missing" about a line that is sitting right in front of you. Annoying,
but at least it is loud.

**Misspell an optional argument and nothing happens at all:**

```python
unit="mm"                      # should be `units`
# → no error. property_label stays "Length", .units is None, your "mm" is gone.
```

The type is still valid; it is just quietly missing something you thought you had set. The
optional arguments are the only ones that behave this way: `units`,
`show_in_edit_views`, `vocabulary_code`, `object_code`, `ordinal`, `metadata`, `unique`,
`internal_assignment`, `iri`, `dynamic_script`. Anything you type that is on neither that
list nor the required six is doing nothing.

The same applies to arguments that sound plausible but do not exist yet. `prev_version=`
is currently one of these — it is not defined anywhere in `definitions.py`, so every
`prev_version=[...]` line in `base_objects_claude.py` is being discarded. Either add the
field to `definitions.py` or delete those lines.

### 3. `section` controls the order, not your typing order

All fields sharing a `section` get grouped together in the UI, wherever they were declared
— including fields pulled in from a parent. If you give a new field in `Experiment`
`section="General Information"`, it lands next to the parent's General Information fields,
*above* fields declared earlier in the parent under a different section. Pick section
names deliberately.

The reason is that openBIS draws each section as one collapsible box in the UI, so it
needs every field of a section together — it cannot draw the box twice. Worked example:

```python
class Parent(ObjectType):
    name  = ...  section="General Information"   # typed 1st
    notes = ...  section="Extra Details"         # typed 2nd

class Child(Parent):
    owner = ...  section="General Information"   # typed 3rd, and in another file
```

`Child().properties` comes out as `NAME`, `OWNER`, `NOTES` — `OWNER` was typed last but is
hoisted up beside `NAME`, pushing `NOTES` down.

Two practical consequences: moving lines around in the file does **not** change the
ordering, and grouping is an exact string match, so `"General information"` with a
lowercase i silently creates a second, separate box.

## A skeleton to copy

```python
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class Root(ObjectType):
    defs = ObjectTypeDef(
        code="ROOT",
        description="""Root of the masterdata hierarchy//Wurzel der Masterdaten-Hierarchie""",
        generated_code_prefix="ROOT",
    )

    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="""Name//Name""",
        mandatory=False,
        section="General Information",
    )
```

Note the top two lines. `ObjectType` is the thing you subclass; `ObjectTypeDef` and
`PropertyTypeAssignment` are the two form-fillers. Those three imports are all you need.

## Checking your work

Run this after each type you add. It builds the type, runs every validation rule, and
prints the full flattened field list — so you can see exactly what openBIS will receive:

```bash
python -c "from bam_masterdata.datamodel.v1.activities import Experiment; print(Experiment().model_to_json(indent=2))"
```

If it prints JSON, your type is valid. If it raises, the message names the field and the
problem.

> **Known breakage:** `activities.py` line 1 imports from `base_objects`, but the file on
> disk is called `base_objects_claude.py`, so the command above fails with
> `ModuleNotFoundError`. Rename the file to `base_objects.py` (or fix the import) before
> you rely on this check.

---

## Appendix: how it works underneath

You do not need this to write types. It is here for when something behaves strangely.

### Definitions vs. entities

| Layer | File | What it is |
|---|---|---|
| **Definition** | `bam_masterdata/metadata/definitions.py` | the form-fillers: `ObjectTypeDef`, `PropertyTypeAssignment` |
| **Entity** | `bam_masterdata/metadata/entities.py` | `ObjectType` — the class you subclass |

### Why class attributes do not become pydantic fields

`entities.py:889`:

```python
model_config = ConfigDict(
    ignored_types=(
        ObjectTypeDef,
        CollectionTypeDef,
        DatasetTypeDef,
        PropertyTypeAssignment,
    )
)
```

Normally pydantic sees `name = PropertyTypeAssignment(...)` in a class body and tries to
turn it into a model field with a default. `ignored_types` tells it to leave these four
alone, so `defs` and every field assignment stay **ordinary class attributes**. Nothing
collects them when the class is defined; they are discovered later by walking `__mro__`
and `__dict__`. The only real pydantic field on `ObjectType` is
`properties: list[PropertyTypeAssignment]`, which gets *populated* from those attributes.

### Where the flattening happens

On instantiation, `model_validator_after_init` (`entities.py:1111`) walks
`reversed(cls.__mro__)`, collects every `PropertyTypeAssignment` it finds, regroups them
by `section` preserving first-appearance order, and writes the result to
`self.properties`. That is the mechanism behind trap 3.

Trap 1 has two separate causes: that same validator builds a list with no de-duplication,
so a repeated name appears twice; and `get_property_metadata()` (`entities.py:276`)
iterates `__mro__` *forward* assigning into a dict, so the parent overwrites the child —
the opposite of normal Python override semantics.

### Trap 2, precisely

None of these models set `extra=` in their `model_config`, so pydantic v2 falls back to
`extra="ignore"`. Unrecognised keyword arguments are dropped without any error.

### `code` validation

Regex `^[\w_\$\.\-\+]+$` (`definitions.py:132`). Conventions on top of that: `$` prefix
means the property is openBIS-native (`$NAME`), `.` means inheritance
(`EXPERIMENTAL_STEP.EXPERIMENTAL_GOALS`).

### `generated_code_prefix`

Defaults to `code[:3]` (`definitions.py:326`).
