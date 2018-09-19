### Example 7-9: Defining next_item to return and receive a position

import re
from utilities import expect_equal

pat = re.compile(r'''
^>                              # a > on the beginning of a line
(.*?)$                         # 0 more more characters to end of line
([^>]+)                         # 1 or more characters not >
''',
   re.MULTILINE | re.DOTALL | re.VERBOSE) # as in 7-6

def next_item(src, startpos):
    return extract_from_match(pat.search(src, startpos))

def extract_from_match(matchobj):
    return ((None, -1)              # pos doesn't matter here
            if not matchobj
            else
            (([field.strip() for field in matchobj.group(1).split('|')],
              matchobj.group(2).replace('\n', '')),
             matchobj.end()))       # new value of pos to be remembered

def find_item(src, testfn):
    item, pos = next_item(src, 0)
    while (item):
        if testfn(item):
            return item
        item, pos = next_item(src, pos)

if __name__ == '__main__':
    filename = '../data/aa003.fasta'
    with open(filename) as file:
        contents = file.read()

    pos = 0
    for gid in ('6693803', '6693805', '6693816', ):
        item, pos = next_item(contents, pos)
        assert item
        expect_equal(2, len(item))
        assert item[1]
        expect_equal(gid, item[0][1])
    
        
    item, pos = next_item(contents, pos)
    assert not item
    
    expect_equal('6693803',
                 find_item(contents, lambda itm : itm[0][1] == '6693803')[0][1])

    expect_equal('6693805',
                 find_item(contents, lambda itm : itm[0][1] == '6693805')[0][1])

    expect_equal('6693816',
                 find_item(contents, lambda itm : itm[0][1] == '6693816')[0][1])

    print('Done.')
