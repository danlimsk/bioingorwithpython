### Example 4-22: A two-function nested iteration

def list_sequences_in_files(filelist):
    """For each file whose name is contained in filelist, list the
    description of each sequence it contains"""
    for filename in filelist:
        print(filename)
        with open(filename) as file:
            list_sequences_in_file(file)

def list_sequences_in_file(file):
    for line in file:
        if line[0] == '>':
            print('\t', line[1:-1])


def test():
    filenames = ('../data/nadh.fasta',
                 '../data/aa003.fasta',
                 '../data/BacillusSubtilisPlastmidP1414.fasta'
                 )
    print()
    list_sequences_in_files(filenames)
