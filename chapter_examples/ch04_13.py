### Example 4-13: A definition of product

def product(coll):
    """Return the product of the elements of coll converted to
    floats, including elements that are string representations of
    numbers; if coll has an element that is a string but doesn't
    represent a number, an error will occur"""
    result = 1.0                                        # initialize
    for elt in coll:
        result *= float(elt)                            # combine element with
    return result                                       # accumulated result

def test():
    assert(product(range(1, 6)) == 120)

