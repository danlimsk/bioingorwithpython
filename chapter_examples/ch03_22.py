### Example 3-22: Using a generator to find the first common element

def first_common(collection1, collection2):
    """Return the first element in collection1 that is in collection2"""
    return next((item for item in collection1 if item in collection2), None)

print(first_common(range(1,22, 5), range(0, 22, 4)))
