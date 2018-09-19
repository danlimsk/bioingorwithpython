### Example 3-14: Reading FASTA sequences with one compact function

def read_FASTA(filename):
    with open(filename) as file:
        return [(part[0].split('|'),
                 part[2].replace('\n', ''))
                for part in
                [entry.partition('\n')
                 for entry in file.read().split('>')[1:]]]

print(read_FASTA('../data/aa003.fasta'))
