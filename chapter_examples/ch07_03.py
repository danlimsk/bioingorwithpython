### Example 7-3: Directory listing filtered by regular expressions

import re

def ls(path = ".", ignorepats = (r'.+\.pyc$', r'.+~$', r'^\#')):
    if ignorepats:
        pat = re.compile('|'.join(ignorepats))
        # construct an RE disjunction containing each item of
        # ignorepats to create an RE that matches any of the items
    for filnam in os.listdir(path):
        if not ignorepats or not pat.search(filnam):
            print(filnam)

if __name__ == '__main__':
    ls()
