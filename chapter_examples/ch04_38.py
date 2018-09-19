### Example 4-38: Simple Rebase reader, step 2

def load_enzyme_table():
    return load_enzyme_data_into_table({})
    # start with empty dictionary

def load_enzyme_data_into_table(table):
    line = get_first_line()
    while not end_of_data(line):
        key, value = parse(line)
        store_entry(table, key, value)
        line = get_next_line()
    return table

def get_first_line():
    return 'enzymeA (protoA)             CCCGGG'
    # return a typical line

def get_next_line():
    return ' '                       # so it stops after getting the first line

def end_of_data(line):
    return len(line) < 2
                                     # 0 means end of file, 1 would be a blank line

def parse(line):
    fields = line.split()
                                     # with no argument, split splits at whitespace
                                     # tuple packing (omitting optional parens)
    return fields[0], fields[-1]
                                     # avoiding having to determine whether there are 2 or 3

def store_entry(table, key, value):
    table[key] = value

def test():
    table = load_enzyme_table()
    assert len(table) == 1
    result =  parse('enzymeA (protoA)             CCCGGG')
    assert result == ('enzymeA', 'CCCGGG'), result
    print('All tests passed.')
