### Example 3-18: Filtering out the underscore names from dir

def dr(name):
    """Return the result of dir(name), omitting any names beginning
    with an underscore"""
    return [nm for nm in dir(name) if nm[0] != '_']

import random
print(dir(random))
print(dr(random))
