### Example 8-8: Extracting plain text from HTML

import sys
import re

encoding_pat = re.compile( 
    b'<meta [^>]*?content *= *[^>]*' +            # just to fit line 
    b'charset *= *([a-zA-Z0-9-]+)', 
    re.I | re.A) 

def get_html_encoding(html): 
    encoding = encoding_pat.search(html) 
    return encoding and encoding.group(1).decode() 

def get_html_file_encoding(filename): 
    with open(filename, 'rb') as file: 
        return get_html_encoding(file.read(2000)) 

patterns = (r'<!--.*?-->',               # comments
            r'<script.*?</script>',        # scripts
            r'<[^<>]*>',                  # other tags
           )

def skip_to_body(string):
    matchobj = re.search('<body.*?>', string, re.I)
    return string[matchobj.end():] if matchobj else string

def remove_pats(string, pats):
    for pat in pats:
        string = re.sub(pat,' ', string, flags=re.I|re.S)
    return string

def remove_html(string):
    return remove_pats(string, patterns)

# Example 8-3 added to Example 8-8 in book,
# with an extended table
html_entities = {
# Reserved characters in HTML
    '&#34;' : '"', '&quot;' : '"',
    '&#39;' : "'", '&apos;' : "'",
    '&#38;' : '&', '&amp;' : '&',
    '&#60;' : '<', '&lt;' : '<',
    '&#62;' : '>', '&gt;' : '>',
# ISO 8859-1 symbols       160-191, 215, 247
    '&#160;' : ' ', '&nbsp;' : ' ',
# Punctuation
    '&#8216;' : "'",                # "fancy" open quote
    '&#8217;' : "'",                # "fancy" close quote
    '&#8220;' : '"',                # "fancy" open double-quote
    '&#8221;' : '"',                # "fancy" close double-quote
    '&laquo' : '<<',
    '&raquo' : '>>',
# Symbols
    '&copy;' : '(c)',
    '&para;' : '(P)',
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

# Added from example in book
def print_file_without_html(filename):
    with open(filename, encoding=get_html_file_encoding(filename)) as file:
        print(remove_html(replace_substrings(skip_to_body(file.read()),
                                             html_entities)
                          )
              )

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(print_file_without_html('../data/PythonBuiltinTypes.html'))
