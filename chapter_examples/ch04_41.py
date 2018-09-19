### Example 4-41: Simple Rebase reader, step 5

from ch04_39 import *

def write_table_to_filename(table, data_filename):
    """Write table in a simple format to a file named
    data_filename"""
    with open(data_filename, 'w') as file:
        write_table_entries(table, files)

def write_table_entries(table, datafile):
    for enzyme in sorted(table.keys()):
        print(enzyme, table[enzyme], sep='        ', file=datafile)

def read_table_from_filename(data_filename):
    """Return a table read from the file named data_filename that was
    previously written by write_table_to_filename"""
    with open(data_filename) as file:
        return read_table_entries(file, {})

def read_table_entries(datafile):
    for line in datafile:
        fields = line.split()
        table[fields[0]] = fields[1]
    return table
