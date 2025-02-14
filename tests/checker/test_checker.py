from bam_masterdata.checker import MasterdataChecker

checker = MasterdataChecker(
    validation_rules_path="bam_masterdata/checker/validation_rules.json"
)
checker.load_current_model()  # Automatically finds Python files in the datamodel directory
# print(checker.current_model)
