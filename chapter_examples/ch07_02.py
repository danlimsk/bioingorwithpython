### Example 7-2: A VERBOSE regular expression for decimal numbers

r"""\d +  # match one or more digits (remember to use raw strings!)
    \.    # match a decimal point (not any character, because backslashed)
    \d *  # match 0 or more digits"""
