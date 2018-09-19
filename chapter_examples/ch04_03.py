### Example 4-3: Recording echo

def recording_echo():
    """Echo the user's input until it equals 'bye', then return a
    list of all the inputs received"""
    lst = []
    entry = echo1()
    while entry != 'bye':
        lst.append(entry)
        entry = echo1()
    return lst

def test():
    print(recording_echo())

