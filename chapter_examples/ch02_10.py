### Example 02-10: Adding an assertion to the gc_content function

def gc_content(base_seq):
    """Return the percentage of G and C characters in base_seq"""
    assert validate_base_sequence(base_seq), \
           'argument has invalid characters'
    seq = base_seq.upper()
    return ((base_seq.count('G') + base_seq.count('C')) /
            len(base_seq))
