### Example 02-05: A function definition with a docstring

def validate_base_sequence(base_sequence):
    """Return True if the string base_sequence contains only
    upper- or lowercase T, C, A, and G characters, otherwise False"""
    seq = base_seq.upper()
    return len(seq) == (seq.count('T') + seq.count('C') +
                        seq.count('A') + seq.count('G'))
