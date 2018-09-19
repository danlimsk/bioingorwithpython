### Example 4-12: Reading FASTA entries with a Collect iteration

def read_FASTA_iteration(filename):
    sequences = []
    descr = None
    with open(filename) as file:
        for line in file:
            if line[0] == '>':
                if descr:                               # have we found one yet?
                    sequences.append((descr, seq))
                descr = line[1:-1].split('|')
                seq = ''                                # start a new sequence
            else:
                seq += line[:-1]
        sequences.append((descr, seq))                  # add the last one found
    return sequences

def read_FASTA(filename):
    with open(filename) as file:
        return [(part[0].split('|'),
                 part[2].replace('\n', ''))
                for part in
                [entry.partition('\n')
                 for entry in file.read().split('>')[1:]]]

def read_FASTA_loop(filename):
    sequences = []
    descr = None
    with open(filename) as file:
        line = file.readline()[:-1]                     # always trim newline
        while line:
            if line[0] == '>':
                if descr:                               # any sequence found yet?
                    sequences.append((descr, seq))
                descr = line[1:].split('|')
                seq = ''                                # start a new sequence
            else:
                seq += line
            line = file.readline()[:-1]
        sequences.append((descr, seq))                  # easy to forget!
    return sequences


def test():
    filename = '../data/aa003.fasta'
    result1 = read_FASTA_iteration(filename)
    result2 = read_FASTA(filename)
    result3 = read_FASTA_loop(filename)
    assert result1 == result2 == result3
    print('All tests passed')

