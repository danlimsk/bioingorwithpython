### Example 4-37: Simple Rebase reader, step 1

# EnzymeName (Prototype)       ... spaces ...   CutSite

def load_enzyme_table():
    return load_enzyme_data_into_table({})
    # start with empty dictionary

def load_enzyme_data_into_table(table):
    line = get_first_line()
    while not end_of_data(line):
        parse(line)
        store_entry(table)
        line = get_next_line()
    return table

def get_first_line():
    return ''                    # stop immediately

def get_next_line():
    return ' '                   # so it stops after getting the first line

def end_of_data(line):
    return True

def parse(line):
    return line

def store_entry(table):
    pass

# testing:
def test():
    table = load_enzyme_table()
    assert len(table) == 0
    print('All tests passed.')

