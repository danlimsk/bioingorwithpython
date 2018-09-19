### Example 8-6: Extracting an outline from an HTML file

import sys
import re

## This is slightly expanded from the example in the book.
## Adding (<a.*</a>)? filters out links that follow the title.
## "optlink" is added to the "for" statement to receive that
## optional part of the heading.

pattern = r'<h(\d).*?>(.+?)(<a.*</a>)?</h'
def print_outline(filename):
    with open(filename) as fil:
        for level, hd, optlink in re.findall(pattern, fil.read()):
            # indent for each level and print the level in brackets
            print("{0}[{1}] {2}".format(' '*3*int(level), level, hd))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_outline('../data/PythonBuiltinTypes.html')
    else:
        print_outline(sys.argv[1])
