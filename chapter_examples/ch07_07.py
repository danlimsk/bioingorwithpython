### Example 7-7: A findall function for ordinary strings

def findall(string, substring):
    """Return a list of all nonoverlapping positions in string where
    substring appears"""
    positions = []
    pos = string.find(substring)
    while pos >= 0:
        positions.append(pos)
        pos = string.find(substring, pos + len(substring))
    return positions
