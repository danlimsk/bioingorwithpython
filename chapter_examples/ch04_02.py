### Example 4-2: Polite echo

from ch04_01 import echo1

def polite_echo():
    """Echo the user's input until it equals 'bye'"""
    while echo1() != 'bye':
        pass

def test():
    polite_echo()
