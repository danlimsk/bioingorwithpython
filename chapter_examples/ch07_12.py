### Example 7-12: Buffered regular expression generator for a file

from ch07_09 import next_item
from ch07_11 import get_item

def item_generator(file, chunksize=1000):
    curpos = 0
    itm, buffer, nxtpos = get_item(file, '', curpos, chunksize)
    nxtitm, buffer, nxtend = get_item(file, buffer, nxtpos, chunksize)

    while nxtitm:
        if nxtend == len(buffer) - 1:               # buffer was extended to find nxtitm 
            itm, nxtpos = next_item(buffer, curpos) # reread to ensure complete
            buffer = buffer[nxtpos:]                # shorten buffer to start at nxtitm
            nxtend -= nxtpos
            nxtpos = 0
        yield itm
        itm, curpos, nxtpos = nxtitm, nxtpos, nxtend
        nxtitm, buffer, nxtend  = get_item(file, buffer, nxtpos, chunksize)
    yield itm
    
def print_items(filename, chunksize=1000):
    with open(filename) as file:
        for n, itm in enumerate(item_generator(file, chunksize)):
            print('\nitem', n+1, itm, end='\n\n')

if __name__ == '__main__':
    print()
    print_items('../data/aa010.fasta')
    
