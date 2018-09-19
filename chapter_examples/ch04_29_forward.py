### Example 4-29: Searching for data in an HTML file

# This is rewritten from the text to search forward instead of
# searching backward and reversing the results.

import sys

beginresults = '- - - - - - - - begin Results - - - - - -'
endresults = '- - - - - - - - end Results - - - - - -'
patterns = ('</a></div><div class="rprtMainSec"><div class="summary">',
            '\n',
            '</em>]',
            )

def get_field(contents, pattern, curpos, endpos):
    pos = contents.find(pattern, curpos, endpos)
    if pos < 0:                     # successful search?
        raise StopIteration         # no
    newpos = contents.find('>', pos, endpos)
    return (newpos, contents[pos+1:newpos])

def get_next(contents, curpos, endpos):
    fields = []
    for pattern in patterns:
        pos, field = get_field(contents, pattern, curpos, endpos)
        fields.append(field)
    return pos, fields

def get_gene_info(contents):
    lst = []
    curpos = contents.find(beginresults)
    endpos = contents.rfind(endresults, 0, len(contents))
    try:
        while(True):
            curpos, fields = get_next(contents, curpos, endpos)
            lst.append(fields)
    except StopIteration:
        pass
    return lst

def get_gene_info_from_file(filename):
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
    return get_gene_info(contents)

def show_gene_info_from_file(filename):
    infolst = get_gene_info_from_file(filename)
    for info in infolst:
        print(info[0], info[1], info[2], sep='\n    ')

if __name__ == '__main__':
    show_gene_info_from_file(sys.argv[1]
                             if len(sys.argv) > 1
                             else '../data/EntrezGeneResults-vWF.html')
