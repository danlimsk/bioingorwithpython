### Example 6-1: An approximation of the Unix ls command

def ls(path ='.', args = ''):
    """Invoke the shell ls command with args on path"""
    subprocess.call('ls' + ' ' +  args + ' ' + path, shell=True)

if __name__ == '__main__':
    ls('*.py')

