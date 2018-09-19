### Example 8-14: Printing information for a range of proteins

import sys
import xml.etree.cElementTree as ETree

from ch08_12 import print_subtree

def describe_proteins(tree, limit=2, start=1):
    # start at 1 because 0 is the whole genome!
    iter = tree.getiterator('Seq-entry')
    # +1 to always skip entry for entire genome
    for n in range(start+1):
        next(iter)
    for k in range(limit+1):
        print('{:4}'.format(k+start))
        print_subtree(next(iter), 6)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        filename = '../data/Acidobacterium-capsulatum-sequences.xml'
    else:
        filename = sys.argv[1]
    tree = ETree.parse(filename)
    descrs = root.getiterator('Seqdesc_source')
    print()
    describe_proteins(tree)
