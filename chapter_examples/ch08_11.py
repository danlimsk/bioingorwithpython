# Example 8-11: Counting the nodes for a specified type of tag

import sys
import xml.etree.cElementTree as ETree

def count_nodes(element, tagname): 
    """Return the number of tagname nodes in the tree rooted at element""" 
    count = 0 
    for node in element.getiterator(tagname): 
        count += 1 
    return count 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        filename = '../data/Acidobacterium-capsulatum.xml'
    else:
        filename = sys.argv[1]
    tree = ETree.parse(filename)
    print(filename,
          'contains',
          count_nodes(tree, 'Seq-entry'),
          'Seq-entry nodes and',
          count_nodes(tree, 'Seq-feat'),
          'Seq-feat nodes.',
          )
          
        
