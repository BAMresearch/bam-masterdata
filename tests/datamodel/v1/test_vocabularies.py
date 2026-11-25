def test_vocabulary_term_codes_are_unique(v1_vocabulary_type):
    codes = [term.code for term in v1_vocabulary_type().terms]
    assert codes
    assert len(codes) == len(set(codes))
