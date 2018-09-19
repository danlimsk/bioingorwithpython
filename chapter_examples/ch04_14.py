### Example 4-14: Combine: identifying the longest FASTA sequence

from ch03_14 import read_FASTA

def longest_sequence(filename):
    longest_seq = ''
    for info, seq in read_FASTA(filename):
        longest_seq = max(longest_seq, seq, key=len)
    return longest_seq

def test():
    assert 271 len(longest_sequence('../data/aa003.fasta'))
