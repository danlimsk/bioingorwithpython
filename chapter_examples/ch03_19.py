### Example 3-19: Reading FASTA descriptions from a file

def get_FASTA_descriptions(filename):
    with open(filename) as file:
        return [line[1:].split('|') for line in file if line[0] == '>']

print(get_FASTA_descriptions('../data/aa010.fasta'))


