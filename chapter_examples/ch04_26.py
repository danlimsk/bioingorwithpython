### Example 4-26: Printing a tree

import pprint

def treeprint(tree, level=0):
    print(' ' * 4 * level, tree[0], sep='')
    for node in tree[1:]:
        treeprint(node, level+1)

def test():
    tree1 = ['',
             ['A', ['CC', ['CCTGATTACCG'], ['G']], ['TTACCG']],
             ['C', ['C', ['CTGATTACCG'], ['TGATTACCG'], ['G']],
              ['TGATTACCG'], ['G']],
             ['T', ['GATTACCG'], ['TACCG'], ['ACCG']],
             ['GATTACCG']
             ]
    print()
    pprint.pprint(tree1)
    print()
    treeprint(tree1)
    print()

