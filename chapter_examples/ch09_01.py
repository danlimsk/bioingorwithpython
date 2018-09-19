### Example 9-1: Searching the Python Package Index

"""Search the Python Package Index for one or more words"""

import sys
import webbrowser
import urllib.parse

urlpart1 = 'http://pypi.python.org/pypi?:action=search&term='
urlpart2 = '&submit=search'

def search_pypi(words):
    webbrowser.open(urlpart1 +
                    urllib.parse.quote_plus(' '.join(words)) +
                    urlpart2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: pypi term ...")
    else:
        search_pypi(sys.argv[1:])
