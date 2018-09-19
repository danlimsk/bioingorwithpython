### Example 4-17: Printing the header lines from a FASTA file

def print_FASTA_headers(filename):
    with open(filename) as file:
        for line in file:
            if line[0] == '>':
                print(line[1:-1])

def test():
    print()
    print_FASTA_headers('../data/aa010.fasta')
