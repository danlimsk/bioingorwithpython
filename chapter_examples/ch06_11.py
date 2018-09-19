### Example 6-11: Loading Rebase data into a dbm database

import dbm
from ch04_39 import *

def load_enzyme_data(data_filename, dbm_filename):
    try:
        table = dbm.open(dbm_filename, 'n') # 'n' for new database
        with open(data_filename) as datafile:
            load_enzyme_data_into_table(datafile, table)
    finally:
        table.close()

def load_enzyme_data_into_table(datafile, table):
    line = get_first_line(datafile)
    while not end_of_data(line):
        key, value = parse(line)
        store_entry(table, key, value)
        line = get_next_line(datafile)
    # return table   not needed

def store_entry(table, key, value):
    table[key] = value       # table is an open dbm file, but [ ] unchanged

data_filename = '../data/rebase-bionet-format.txt'
dbm_filename = '../output/rebase.dbm'
load_enzyme_data(data_filename, dbm_filename)
