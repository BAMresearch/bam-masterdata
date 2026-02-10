# Summary of changes

- New `code` only identifiers for the classes names
- `is_a` field in ObjectTypeDef keeps track of inheritance
- `previous_versions` encodes metadata about the previous version equivalent object code

- Changed descriptions: $NAME, $SHOW_IN_PROJECT_OVERVIEW, START_DATE, END_DATE
- `$SHOW_IN_PROJECT_OVERVIEW` changed property_label
- Deleted EXPERIMENTAL_STEP.EXPERIMENTAL_RESULTS, $ANNOTATIONS_STATE, $XMLCOMMENTS
- Deleted `GMAW_BASE` and `LASER_HYBRID_MAGNET` (Cagtay)
- Fix `ACCREDITATED_CALIBRATION_LAB` to `ACCREDITED_CALIBRATION_LAB`
- Deleted `TASK`, `ACTION`
- Changed Calibration properties descriptions, sections, and property labels
- Changed `CALIBRATION_PROVIDER` from CONTROLLEDVOCABULARY to VARCHAR
- Deleted `COMPUTATIONAL_ANALYSIS` (now it is `ANALYSIS`)
- Deleted `CONDA_ENVIRONMENT`, `JUPYTER_NOTEBOOK`
