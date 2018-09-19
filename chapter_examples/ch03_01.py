### Example 3-1: Rewriting validate_base_sequence using a set

DNAbases = set('TCAGtcag')
RNAbases = set('UCAGucag')
def validate_base_sequence(base_sequence, RNAflag = False):
    """Return True if the string base_sequence contains only upper-
    or lowercase T (or U, if RNAflag), C, A, and G characters,
    otherwise False"""
    return set(base_sequence) <= (RNAbases if RNAflag else DNAbases)

def test():
    assert validate_base_sequence('ACTG')
    assert validate_base_sequence('')
    assert not validate_base_sequence('ACUG')

    assert validate_base_sequence('ACUG', True)
    assert not validate_base_sequence('ACUG', False)
    assert validate_base_sequence('ACTG', False)

    print('All tests passed.')

