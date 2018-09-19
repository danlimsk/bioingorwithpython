### Example 6-5: Showing a file tree

def show_directory_contents(dirpath, filenames, level):
    print('    '*level, dirpath, sep='')
    for name in filenames:
        print('    '*(level+1), name, sep='')

def show_in_path(startpath, ignoredots=True):
    print(startpath)
    for path, dirnames, filenames in os.walk(startpath):
        for dirname in dirnames:
            if dirname[0] == '.':
                dirnames.remove(dirname)
        show_directory_contents(path[len(startpath)+1:],       # strip dirpath
                                filenames,
                                path.count(os.sep))

if __name__ == '__main__':
    show_in_path('..')
 
