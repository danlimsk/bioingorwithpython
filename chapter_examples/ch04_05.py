### Example 4-5: Recording echo using "loop forever"

def recording_echo_with_conditional():
    """Echo the user's input until it equals 'bye', then return a
    list of all the inputs received"""
    seq = []
    # no need to initialize a value to be tested since nothing is tested!
    while True:
        entry = echo1()
        if entry == 'bye':
            return seq
        seq.append(entry)

def test():
    print(recording_echo_with_conditional())

