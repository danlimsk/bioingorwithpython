### Example 7-10: Defining next_item as a generator

import re

pat = re.compile(r'^>(.*)$([^>]+)', re.MULTILINE) # as in 7-6

def item_generator(src):
    pos = 0
    item, pos = next_item(src, pos)
    while item:
        yield item
        item, pos = next_item(src, pos)

def find_item(src, testfn):
    itemgen = item_generator(src)
    item = next(itemgen)
    while (item):
        if testfn(item):
            return item
        item = next(itemgen)

if __name__ == '__main__':
    filename = '../data/aa003.fasta'
    with open(filename) as file:
        contents = file.read()

    item, pos = next_item(contents, 0)
    expect_equal('6693803',
                 find_item(contents, lambda itm : itm[0][1] == '6693803')[0][1])

    print('Done.')
