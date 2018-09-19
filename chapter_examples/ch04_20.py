### Example 4-20: Generalized combine function

def combine(coll, initval, action, filter=None):
    """Starting at initval, perform action on each element of coll,
    finally returning the result. If filter is not None, only include
    elements for which filter(element) is true. action is a function
    of two arguments--the interim result and the element--which
    returns a new interim result."""
    result = initval
    for elt in coll:
        if not filter or filter(elt):
           result = action(result, elt)
    return result

def test():
    assert 9 == combine((4.2, 3, ' ', 4, 5.0, 2),
                        0,
                        lambda result, elt: result + elt,
                        lambda elt: isinstance(elt, int))
    print('All tests passed.')
