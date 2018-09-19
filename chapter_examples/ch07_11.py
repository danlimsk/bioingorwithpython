### Example 7-11: Buffered regular expression search of a file

import re

from ch07_09 import next_item

def get_item(fil, buffer, pos, chunksize):
    """Return an item along with the new value of buffer and the end
    position of the successful match; the new item's sequence may be
    incomplete -- this is fixed in Example 7-12"""
    item, endpos = next_item(buffer, pos)         # initialize loop
    while not item:                               # look for next item
        chunk = fil.read(chunksize)               # read next chunk
        if not chunk:
            return None, buffer, len(buffer)      # end of file
        buffer += chunk                           # add chunk to buffer
        item, endpos = next_item(buffer, pos)     # try again
    return item, buffer, endpos-1                 # endpos is where the
                                                  # next > was last char
                                                  # of match, so -1


def print_items(filename, chunksize):
    with open(filename) as file:
        item, buffer, endpos = get_item(file, '', 0, chunksize)
        while item:
            print('item = {}\n\nbuffer = "{}"\n\nendpos = {}'.
                  format(item, buffer, endpos))
            print('_'*72)
            buffer = buffer[endpos:]
            endpos = 0
            item, buffer, endpos = get_item(file, buffer, endpos, chunksize)

if __name__ == '__main__':
    print()
    print_items('../data/aa010.fasta', 100)
    
