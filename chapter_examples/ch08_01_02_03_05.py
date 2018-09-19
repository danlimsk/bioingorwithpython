import sys
import re
import textwrap

from utilities import get_html_file_encoding

### Example 8-1: Extracting <a> links from an HTML file, step 1

import sys
import re
import textwrap

def print_atags_in_files(lst):
    for filename in lst:
        print(64*'-')                       # draw separator line
        print(filename)                     # added from example in book
        print_atags_in_file(filename)

def print_atags_in_file(filename):
    with open(filename, encoding=get_html_file_encoding(filename)) as file:
        print_atags(replace_substrings(file.read(), html_entities))
        # replace_substrings added for step 3; see below

def print_atag(results):
   print(textwrap.fill(results[0], 75),
         textwrap.fill(results[1], 75),
         sep='\n',
         end='\n\n')

### Example 8-2: Extracting <a> links from an HTML file, step 2

atagpat = re.compile(
    r'''<a\s+(.*?)>   # the <a> tag attributes up to first >
        (.*?)         # capturing the entire content up to first </a>
        </a>          # the </a> end tag
     ''',
    re.IGNORECASE|re.MULTILINE | re.DOTALL | re.VERBOSE)

### Example 8-3: Extracting <a> links from an HTML file, step 3

html_entities = {
# Reserved characters in HTML
    '&#34;' : '"', '&quot;' : '"',
    '&#39;' : "'", '&apos;' : "'",
    '&#38;' : '&', '&amp;' : '&',
    '&#60;' : '<', '&lt;' : '<',
    '&#62;' : '>', '&gt;' : '>',
# ISO 8859-1 symbols       160-191, 215, 247
    '&#160;' : ' ', '&nbsp;' : ' ',
# Math symbols
    '&#8211;' : '-', '&ndash;' : '-',
    '&#8212;' : '-', '&mdash;' : '--',
    '&#8242;' : "'", '&prime;' : "'",
    '&#8243;' : "'", '&Prime;' : '"',
}

def replace_substrings(string, dictionary):
    """Return a copy of string in which every key of dictionary has
    been replaced with the corresponding value, in arbitrary order"""
    for key, value in dictionary.items():
        string = string.replace(key, value)
    return string

### Example 8-5: Extracting <a> links from an HTML file, step 5

tagpat = re.compile(r"<[^>]+?>") # easy - anything within a pair of <>s

def remove_tags(content):
    return tagpat.sub('', content)

## replaces definition from Example 8-2
def get_all_atags(string):
    return [(url, remove_tags(content))
            for url, content in atagpat.findall(string)
            if url[0] != '#']

## replaces definition from Example 03
def print_atags(string):
    for atag in get_all_atags(string):
        if atag[1]:
            print_atag(atag)
###

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_atags_in_file('../data/PLoS-NonsenseMediatedDecay.html')
    else:
        print_atags_in_files(sys.argv[1:])
