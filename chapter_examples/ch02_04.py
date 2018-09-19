### Example 02-04: Documentation of a function with commented lines

# A short example illustrating various details of function
# definitions. Given a string ostensibly representing a base
# sequence, return True or False according to whether the string is
# composed entirely of upper- or lowercase T, C, A, and G characters
def validate_base_sequence(base_sequence):
    # argument should be a string
    seq = base_sequence.upper()
    # ensure all uppercase characters
    return len(seq) == (seq.count('T') + seq.count('C') +
                        seq.count('A') + seq.count('G'))
