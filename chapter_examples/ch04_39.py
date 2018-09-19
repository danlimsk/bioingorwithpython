### Example 4-39: Simple Rebase reader, step 3

def load_enzyme_table(data_filename):
    with open(data_filename) as datafile:
        return load_enzyme_data_into_table(datafile, {})

def load_enzyme_data_into_table(datafile, table):
    line = get_first_line(datafile)
    while not end_of_data(line):
        print(line, end='')
        key, value = parse(line)
        store_entry(table, key, value)
        line = get_next_line(datafile)
    return table

def get_first_line(fil):
     line = fil.readline()
     while line and not line[0] == 'A':
         line = fil.readline()
     return line

def get_next_line(fil):
    return fil.readline()

def end_of_data(line):
    return len(line) < 2

def parse(line):
    fields = line.split()
    return fields[0], fields[-1]

def store_entry(table, key, value):
    table[key] = value

def test():
    print()
    datafilename = '../data/rebase-bionet-format.txt'
    table = load_enzyme_table(datafilename)
    assert len(table) == 3559, len(table)
    result =  parse('enzymeA (protoA)             CCCGGG')
    assert result == ('enzymeA', 'CCCGGG'), result
    print()
    print('All tests passed.')

