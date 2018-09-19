### Example 8-9: Using a subclass of html.parser.HTMLParser

from utilities import get_html_file_encoding

import sys
import re
import html.parser

class HTMLOutlineParser(html.parser.HTMLParser):
    """Show an indented outline of the headings in the HTML file
    provided as a command-line argument"""

    # HTMLParser converts tag to lowercase
    HeadingPat = re.compile('title|h([1-6])')
    Indent = 4

    def __init__(self):
        super().__init__()
        self.inheading = False

    def handle_starttag(self, tag, attrs):
        match = self.HeadingPat.match(tag)
        if match:
            self.inheading = True
            if match.group(1): # otherwise title & do nothing
                print('{0:{1}}[{2}]'.format(' ',
                                            self.Indent * int(match.group(1)),
                                            match.group(1)),
                      end=' ')

    def handle_data(self, data):
        if self.inheading:
            print(data, end=' ')
            # end=' ' so printing stays on this line in case
            # parts of the heading are nested inside other
            # markup, such as <i></i>

    def handle_endtag(self, tag):
        if self.inheading and self.HeadingPat.match(tag):
        # assuming heading tags (h1, h2, ...) cannot be nested
            print()             # close tag
            self.inheading = False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        filename = '../data/PythonBuiltinTypes.html'
    else:
        filename = sys.args[1]

    parser = HTMLOutlineParser()
    with open(filename, encoding= get_html_file_encoding(filename)) as file:
        contents = file.read()
    print('File contains', len(contents), 'bytes')
    parser.feed(contents)
    parser.close()
