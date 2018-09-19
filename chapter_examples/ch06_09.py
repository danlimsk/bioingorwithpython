### Example 6-9: Find files matching a pattern

import os.path
import fnmatch

def find_matching_files(startpath, pattern):
    """Return a list of filenames that match pattern in the directory
    tree starting at startpath"""
    paths = []
    for path, dirnames, filenames in os.walk(startpath):
        for dirname in dirnames:
            if dirname[0] == '.':
                dirnames.remove(dirname)
        paths += [os.path.join(path, filename)
                      for filename in fnmatch.filter(filenames, pattern)]
    return paths

if __name__ == '__main__':
    print(find_matching_files('..', '*.txt'))
