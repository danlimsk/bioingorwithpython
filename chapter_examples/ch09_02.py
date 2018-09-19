### Example 9-2: Making a web page with links extracted from HTML files

import sys
import webbrowser

from utilities import get_html_file_encoding
from ch08_01_02_03_05 import get_all_atags

html_start = ('''<!DOCTYPE html PUBLIC
          "-//W3C//DTD XHTML 1.0 Transitional//EN"
          "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<title>Collected Links</title>
</head>
<body>
''')

html_end = '''
</body>
</html>
'''

filetagformat = '\n<h3>{0}</h3>\n'
atagformat = "<li><a {0}>{1}</a></li>\n"

def make_html_file_from_files(filenames, outputfilename='links.html'):
    with open(outputfilename, 'w') as outfile:
        outfile.write(html_start)
        for filename in filenames:
            make_html_for_filename(filename, outfile)
        outfile.write(html_end)
    return outputfilename

def make_html_for_filename(filename, outfile):
    outfile.write(filetagformat.format(filename))
    outfile.write('<ol>\n')
    with open(filename, encoding=get_html_file_encoding(filename)) as infile:
        for tag in get_all_atags(infile.read()):
            if tag[1]:
                make_html_for_tag(tag, outfile)
    outfile.write('</ol>\n')

def make_html_for_tag(tag, outfile):
    outfile.write(atagformat.format(tag[0], tag[1]))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        filenames = ['../data/REBASEFormats.html']
    else:
        filenames = sys.argv[:1]

    webbrowser.open(
        'file://' + os.path.abspath(make_html_file_from_files(filenames))
        )
