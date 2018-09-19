### Example 6-8: Hierarchical directory listing

import os.path

def dirtree(path='.', ignoredots=True, level=0):
    print_path(path, level)                        # "do something" with tree root and level
    for name in os.listdir(path):                  # repeat with the rest of the tree
        subpath = os.path.join(path, name)
        if os.path.isdir(subpath):
            dirtree(subpath, ignoredots, level+1)

def print_path(path, level):
    print(' ' * 3 * level, path, sep='')

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print('Usage: directory_size path')
    else:
        dirtree('.' if len(sys.argv) == 1 else sys.argv[1])
