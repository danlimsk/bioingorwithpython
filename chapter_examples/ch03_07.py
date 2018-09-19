### Example 3-7: Validating base sequences using a list comprehension

def validate_base_sequence(base_sequence, RNAflag = False):
    valid_bases = 'UCAG' if RNAflag else 'TCAG'
    return all([(base in valid_bases)
                for base in base_sequence.upper()])
