### Example 3-21: Constructing a selective dictionary

from ch03_14 import read_FASTA

def make_gi_indexed_sequence_dictionary(filename):
    return {info[1]: seq for info, seq in read_FASTA(filename)
            if len(info) >= 2 and info[0] == 'gi'}

print(make_gi_indexed_sequence_dictionary('../data/aa003.fasta'))
