### Example 4-18: Extracting sequences with matching descriptions

def extract_matching_sequences(filename, string):
    """From a FASTA file named filename, extract all sequences whose
    descriptions contain string"""
    sequences = []
    seq = ''
    with open(filename) as file:
        for line in file:
            if line[0] == '>':
                if seq:                        # not first time through
                    sequences.append(seq)
                seq = ''                       # next sequence detected
                includeflag = string in line   # flag for later iterations
            else:
                if includeflag:
                    seq += line[:-1]
        if seq:                        # last sequence in file is included
            sequences.append(seq)
    return sequences

def test():
    print()
    for seq in extract_matching_sequences('../data/aa010.fasta', 'factor'):
        print(seq)
