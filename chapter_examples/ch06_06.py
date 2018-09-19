### Example 6-6: Filtered directory listing

import os.path

def filtered_directory_listing(dirpath = '.',
                               ignore_extensions = ('.pyc', '.bak')):
    for filename in os.listdir(dirpath):
        if os.path.splitext(filename)[1] not in ignore_extensions:
            print(filename)

def cd(path):
    """Make path the current directory, expanding environment
    variables and a ~ representing the user's home directory"""
    os.chdir(os.path.expandvars(os.path.expanduser(path)))

def merge_ext(path, ext=''):
    """Return path with its extension replaced by ext, which normally
    starts with a period; with no arguments, remove the extension"""
    splitpath, splitname = os.path.split(path)
    return os.path.join(splitpath, os.path.splitext(splitname)[0] + ext)

if __name__ == '__main__':
    filtered_directory_listing('..')
