### Example 02-11: Adding a “flag” parameter

def validate_base_sequence(base_sequence, RNAflag):
    """Return True if the string base_sequence contains only upper-
    or lowercase T (or U, if RNAflag), C, A, and G characters, otherwise
    False""" 
    seq = base_sequence.upper()
    return len(seq) == (seq.count('U' if RNAflag else 'T') +
                        seq.count('C') +
                        seq.count('A') +
                        seq.count('G'))
