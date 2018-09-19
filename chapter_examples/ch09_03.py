### Example 9-3: Constructing a web page directly from requests

import sys
import webbrowser

import urllib.parse
import urllib.request

from ch08_01_02_03_05 import get_all_atags

filetagformat = '\n<h3>{0}</h3>\n'
atagformat = "<li><a {0}>{1}</a></li>\n"

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

def make_html_file_from_urls(urls, outputfilename='links.html'):
    with open(outputfilename, 'w', encoding='UTF-8') as outfile:
        outfile.write(html_start)
        for url in urls:
            make_html_for_url(url, outfile)
        outfile.write(html_end)
    return outputfilename

def make_html_for_url(url, outfile):
    outfile.write(filetagformat.format(url))
    outfile.write('<ol>\n')
    for tag in get_all_atags(
        str(urllib.request.urlopen(url).read().decode('UTF-8'))):
        if tag[1]:
            make_html_for_tag(url, tag, outfile)
    outfile.write('</ol>\n')

def make_html_for_tag(url, tag, outfile):
    outfile.write(atagformat.format(make_absolute(url, tag[0]), tag[1]))

def make_absolute(url, tagaddress):
    return urllib.parse.urljoin(url, tagaddress)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        URLS = [
            'http://www.plosgenetics.org/search/simpleSearch.action?' +
            'query=nmd&x=0&y=0']
    else:
        URLS = sys.argv[:1]

webbrowser.open(
    'file://' + os.path.abspath(make_html_file_from_urls(URLS))
    )


