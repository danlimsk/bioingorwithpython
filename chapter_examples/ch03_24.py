### Example 3-24: Definition of a function with a functional argument

def some(coll, pred=lambda x: x):
    """Return true if pred(item) is true for some item in coll"""
    return next((True for item in coll if pred(item)), False)

print()
print('some(range(5)) is', some(range(5)))
print('some((None, '', 0)) is', some((None, '', 0)))
print('some(range(5), lambda x: x > 5) is', some(range(5), lambda x: x > 5))
print('some(range(5), lambda x: x > 3) is', some(range(5), lambda x: x > 3))
