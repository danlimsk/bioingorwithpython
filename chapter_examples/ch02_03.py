### Example 02-03: Using backslash for line continuations

def validate_base_sequence(base_sequence):
    seq = base_sequence.upper()
    return len(seq) == \
                seq.count('A') + seq.count('G') + \
                seq.count('T') + seq.count('C')
