### Example 4-19: Filtered Combine: another definition of product

def is_number(value):
    """Return True if value is an int or a float"""
    return isinstance(value, int) or isinstance(value, float)

def product(coll):
    """Return the product of the numeric elements of coll"""
    result = 1.0                         # initialize
    for elt in coll:
        if is_number(elt):
            result = result * float(elt) # combine element with accumulated result
    return result

def test():
    assert 7.0 == product((2, None, 3.5, 'four')))
