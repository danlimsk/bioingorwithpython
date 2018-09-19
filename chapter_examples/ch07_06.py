### Example 7-6: Defining next_item for FASTA with a regular expression

import re

from utilities import expect_equal

pat = re.compile(r'^>(.*)$([^>]+)', re.MULTILINE)

def next_item(src):
    return extract_from_match(pat.search(src))

def extract_from_match(matchobj):
    return (matchobj and            # return None when match fails
            (([field.strip() for field in matchobj.group(1).split('|')],
              matchobj.group(2).replace('\n', '')),
              matchobj.end()))

if __name__ == '__main__':
    filename = '../data/aa003.fasta'
    with open(filename) as file:
        contents = file.read()

    source = contents
    item = next_item(contents)
    expect_equal(349, item[1])      # where the item ends in contents
    expect_equal('6693803', item[0][0][1])
    
    # read next item from where previous one ended
    source = source[item[1]:]
    item = next_item(source)
    expect_equal(373, item[1])
    expect_equal('6693805', item[0][0][1])

    # read next item from where previous one ended
    source = source[item[1]:]
    item = next_item(source)
    expect_equal(257, item[1])
    expect_equal('6693816', item[0][0][1])
    
    print('Done.')



