### Example 4-1: Echo

def echo():
    """Echo the user's input until an empty line is entered"""
    while echo1():
        pass

def echo1():
    """Prompt the user for a string, "echo" it, and return it"""
    line = input('Say something: ')
    print('You said "', line, '"', sep='')
    return line

def test():
    echo()

