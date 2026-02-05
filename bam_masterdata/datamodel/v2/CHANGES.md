# Summary of changes

- New `code` only identifiers for the classes names
- `is_a` field in ObjectTypeDef keeps track of inheritance
- `previous_versions` encodes metadata about the previous version equivalent object code

- Changed descriptions: $NAME, $SHOW_IN_PROJECT_OVERVIEW, START_DATE, END_DATE
- `$SHOW_IN_PROJECT_OVERVIEW` changed property_label
- Refactored `PUBLICATION` to `EXTERNAL_ID`
- Refactored `FINISHED_FLAG` to `STATUS` vocabulary
- Changed `EXPERIMENTAL_STEP.EXPERIMENTAL_GOALS` to `GOALS`
- Changed `EXPERIMENTAL_STEP.SPREADSHEET` to `SPREADSHEET`
- Deleted EXPERIMENTAL_STEP.EXPERIMENTAL_DESCRIPTION, EXPERIMENTAL_STEP.EXPERIMENTAL_RESULTS, $ANNOTATIONS_STATE, $XMLCOMMENTS
