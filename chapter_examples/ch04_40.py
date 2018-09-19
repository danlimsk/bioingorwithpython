### Example 4-40: Simple Rebase reader, step 4

# This step uses the definitions of the previous step unchanged, except
# that the call to print in load_enzyme_data_into_table could be removed

from ch04_39 import *

def test():
    print()
    datafilename = '../data/rebase-bionet-format.txt'
    table = load_enzyme_table(datafilename)
    # check first entry from file:
    assert table['AaaI'] == 'C^GGCCG'
    # check an ordinary entry with a prototype:
    assert table['AbaI'] == 'T^GATCA', table
    # check an ordinary entry that is a prototype:
    assert table['BclI'] == 'T^GATCA', table
    # check last entry from file:
    assert table['Zsp2I'] == 'ATGCA^T'
    assert len(table) == 3559, len(table)
    print()
    print('All tests passed.')
