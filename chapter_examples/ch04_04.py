### Example 4-4: Commented recording echo function

def recording_echo():

    # initialize entry and lst
    lst = []

    # get the first input
    entry = echo1()

    # test entry
    while entry != 'bye':

        # use entry
        lst.append(entry)

        # change entry
        entry = echo1()

        # repeat

    # return result
    return lst

def test():
    print(recording_echo())
