### Example 7-1: Functions for multiple match and search

from utilities import expect_equal

def multi_match(target, patterns):
    """Return True if target begins with any of the strings in
    patterns"""
    for pattern in patterns:
        if target.startswith(pattern):
            return True

def multi_search(target, patterns):
    """Return the first position in target where any of the strings
    in patterns is found; return -1 if not found (since 0 means the
    pattern is found at the beginning of the target).."""
    return max(-1,
                min([target .find(pattern)
                     for pattern in patterns
                     if target.find(pattern) >= 0])
                )

if __name__ == '__main__':
    assert multi_match('GAATTCTAATGCC', ('TAAA', 'GAATTC', 'GCC'))
    assert not multi_match('GAATTCTAATGCC', ('TAAA', 'GCC'))
    expect_equal(multi_search('GAATTCTAATGCC', ('TAAA', 'GAATTC', 'GCC')), 0)
    expect_equal(multi_search('GAATTCTAATGCC', ('TAAA', 'GCC')), 10)
    assert not multi_search('GAATTCTAATGCC', ('TAAA', 'GAA'))
    print('Done.')
