### Example 8-16: Getting content from a specified XML tag

import xml.parsers.expat

def handle_start(p, target, name):
    """Install data handler when target tag is encountered"""
    if name == target:
        # now install handler for data tag
        p.CharacterDataHandler = lambda data: return_data(data)

def return_data(data):
    """Stop searching, since the target has been found; installed
     when the target start tag has been encountered"""
    raise StopIteration(data)

def lookup(filename, target):
    p = xml.parsers.expat.ParserCreate()
    # install handler for start tags
    p.StartElementHandler = \
        lambda name, attrs: handle_start(p, target, name)
        # one way to "forward" a parameter to an outside function

    with open(filename) as file:
        try:
            while True:
                p.Parse(file.read(2000))     # read 2000 bytes at a time
        except StopIteration as stop:        # expected!
            return str(stop)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        filename = '../data/Acidobacterium-capsulatum-sequences.xml'
    else:
        filename = sys.argv[1]
    print(lookup(filename, 'Seqdesc_title'))
