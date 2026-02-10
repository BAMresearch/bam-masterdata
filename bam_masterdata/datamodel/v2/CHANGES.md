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
- Deleted `EXPERIMENTAL_STEP.RM_ETHANOL`, `ACTION.DEVICE_TRAINING`, `ACTION.DEVICE_USAGE`, `EXPERIMENTAL_STEP.MEASUREMENT_SESSION`
- Changed Calibration properties descriptions, sections, and property labels
- Changed `CALIBRATION_PROVIDER` from CONTROLLEDVOCABULARY to VARCHAR
- Deleted `COMPUTATIONAL_ANALYSIS` (now it is `ANALYSIS`)
- Deleted `CONDA_ENVIRONMENT`, `JUPYTER_NOTEBOOK`
- Change vocabulary code `DCPD_POT_CAL` to `DCPD_POT_DROP_CALIBRATION`
- Changed `DCPD_INITIAL_CRACKLENGTH` property code to `DCPD_INITIAL_CRACK_LENGTH`
- Deleted all properties in DCPD which are instrument-specific --> they should be properties of the instrument
- Changed `RAZOR_STROKELENGTH`, `RAZOR_STROKESPEED`, and `RAZOR_STROKECOUNT` to `RAZOR_STROKE_LENGTH`, `RAZOR_STROKE_SPEED`, and `RAZOR_STROKE_COUNT`
- Changed `RAZOR_STROKE_COUNT` from REAL to INTEGER
- Combined `FCG_TEST` and `FCG_STEP` into `FCG_TEST`
- Changed `FINAL_CYCLES` from REAL to INTEGER
- Changed vocabulary code `MICROSCOPY_FCG_CRACK_LENGTH_TYPE` to `MICROSCOPY_FS_TYPE`
- Deleted `EXPERIMENTAL_STEP.FCG_EVALUATION`
