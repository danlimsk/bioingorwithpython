### Example 4-7: Checking for a result after every read

def read_sequence(filename):
    """Given the name of a FASTA file named filename, read and return
    its first sequence, ignoring the sequence's description"""
    seq = ''
    with open(filename) as file:
        line = file.readline()
        while line and line[0] == '>':
            line = file.readline()
        while line and line[0] != '>':      # must check for end of file
            seq += line
            line = file.readline()
    return seq

def test():
    print(read_sequence('../data/aa003.fasta'))

