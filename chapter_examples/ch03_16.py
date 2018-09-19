### Example 3-16: Constructing a dictionary with a comprehension

from ch03_14 import read_FASTA

def make_indexed_sequence_dictionary(filename):
    return {info[1]: seq for info, seq in read_FASTA(filename)}

print(make_indexed_sequence_dictionary('../data/aa003.fasta'))
