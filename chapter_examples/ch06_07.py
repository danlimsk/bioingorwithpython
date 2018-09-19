### Example 6-7: Calculating the total size of files in a directory

"""Print the sum of the sizes of the files in the directory given on the command line
(or the current directory if none is given), in megabytes rounded to 2 places"""

import os.path

def directory_size(path='.'):
    """Sum of the sizes of all files in the directory at path,
    including those beginning with a '.', and ignoring subdirectories"""
    result = 0                                     # identity element
    for item in os.listdir(path):
        if os.path.isfile(item):                   # the test
            result += os.path.getsize(os.path.join(path, item))
    return result

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print('Usage: directory_size path')
    else:
        size = directory_size('.' if len(sys.argv) == 1 else sys.argv[1])
        print(round(size/1024/1024, 2), 'Mb', sep='')
