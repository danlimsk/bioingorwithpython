### Example 9-4 - 9-7 : Downloading links

## Example of use:
## python3 ch09_04_05_06_07.py -l http://docs.python.org/py3k/download.html

import sys
import os
import re
import optparse
import urllib.request

### Example 9-4: Downloading links: setting up the option parser

def make_command_line_parser():
    optparser = optparse.OptionParser(
        usage='Usage: downloadLinks [--destdir dir] [-extension ext]* URL')
    optparser.set_defaults(extension=('zip', 'pdf'))
    optparser.add_option('-d', '--destdir',
                      help='directory to which files will be downloaded')
    optparser.add_option('-e', '--extension', action='append',
                      help='extension(s) of links to download')
    optparser.add_option('-l', '--list', action='store_true',
                      help="list, but don't download, links")
    return optparser

### Example 9-6: Downloading links: finding the links

def get_url_contents(url):
    response = urllib.request.urlopen(url)
    contents = response.read()
    response.close()
    return str(contents)

linkstring = r"'([^']+?\.(exts))'|\"([^\"]+?\.(exts))\""

def extract_links_from_string(string, extensions):
    results = re.findall(linkstring.replace('exts', '|'.join(extensions)),
                         string,
                         re.M | re.S | re.I)
    return [result[1] or result[2] for result in results]

def get_url_links(url, options):
    return extract_links_from_string(get_url_contents(url),
                                     options.extension)

### Example 9-7: Downloading links: the real work

def list_links_from_url(url, options):
    for link in get_url_links(url, options):
        print(link)

def download_links_from_url(url, options):
    for n, link in enumerate(get_url_links(url, options)):
        path = urllib.parse.urlsplit(link).path
        targeturl = urllib.parse.urljoin(url, link)
        print(n+1, targeturl, sep='\t')         # show progress
        urllib.request.urlretrieve(targeturl,
                                   os.join(options.destdir,
                                           os.path.basename(path)))

### Example 9-5: Downloading links: main

if __name__ == '__main__':
    optparser = make_command_line_parser()
    (options, args) = optparser.parse_args()
    if len(args) != 1:
        optparser.print_help()
        sys.exit(2)                         # command-line error
    else:
        if options.list:
            list_links_from_url(args[0], options)
        else:
            download_links_from_url(args[0], options)

