### Example 3-6: Reading FASTA sequences from a file, step 1

def read_FASTA_strings(filename):
    with open(filename) as file:
        return file.read().split('>')[1:]
    
### Example 3-10: Reading FASTA sequences from a file, step 2

def read_FASTA_entries(filename):
    return [seq.partition('\n') for seq in read_FASTA_strings(filename)]
    
    
### Example 3-11: Reading FASTA sequences from a file, step 3

def read_FASTA_sequences(filename):
    return [[seq[0], seq[2].replace('\n', '')]           # delete newlines
             for seq in read_FASTA_entries(filename)]
    
### Example 3-12: Reading FASTA sequences from a file, step 3, unpacked

def read_FASTA_sequences_unpacked(filename):
    return [(info, seq.replace('\n', ''))
            for info, ignore, seq in                     # ignore is ignored (!)
            read_FASTA_entries(filename)]
    
    
### Example 3-13: Reading FASTA sequences from a file, step 4

def read_FASTA_sequences_and_info(filename):
    return [[seq[0].split('|'), seq[1]] for seq in
            read_FASTA_sequences(filename)]

def test():
    filename = '../data/aa003.fasta'

    seqs = read_FASTA_strings(filename)
    assert '6693803' == seqs[0][3:10]

    seqs = read_FASTA_entries(filename)
    assert '6693803' == seqs[0][0][3:10]
    # extra [0] to accomodate 'deeper' structure returned

    seqs = read_FASTA_sequences(filename)
    assert '6693803' == seqs[0][0][3:10]

    seqs = read_FASTA_sequences_unpacked(filename)
    assert '6693803' == seqs[0][0][3:10]

    seqs = read_FASTA_sequences_and_info(filename)
    assert '6693803' == seqs[0][0][1]

    print('All tests passed.')

