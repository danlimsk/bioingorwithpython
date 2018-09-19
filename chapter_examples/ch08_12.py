### Example 8-12: Functions for printing subtree of an ElementTree

import sys
import xml.etree.cElementTree as ETree

def print_element(element, level=1):
    """Print tag, content, and attributes of element, indented level
    spaces, but only if element has text or attributes"""
    # ignoring tail
    if element.text and not element.text.isspace():
        print(' '*level, element.tag, ': ', element.text.strip(), sep='')
    elif element.attrib:
        print(' '*level, element.tag)
    for attr in sorted(element.keys()):
        print(' '*(level+2), attr, '=', element.get(attr))

def print_subtree(element, level = 0):
    """Print the tags, attributes, and contents of element and all of
    its children, in depth-first order, starting with an indentation
    of level spaces"""
    print_element(element, level)
    for subelt in element.getchildren():
        print_subtree(subelt, level+1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        filename = '../data/Acidobacterium-capsulatum-sequences.xml'
    else:
        filename = sys.argv[1]
    tree = ETree.parse(filename)
    root = tree.getroot()
    descrs = root.getiterator('Seqdesc_source')
    print()
    print_subtree(next(descrs))
