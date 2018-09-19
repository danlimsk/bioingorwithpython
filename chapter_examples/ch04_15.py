### Example 4-15: Collection Combine: sequence IDs from multiple files

def extract_gi_id(description):
    """Given a FASTA file description line, return its GenInfo ID if
    it has one"""
    if description[0] != '>':
        return None
    fields = description[1:].split('|')
    if 'gi' not in fields:
        return None
    return fields[1 + fields.index('gi')]

def get_gi_ids(filename):
    """Return a list of the GenInfo IDs of all sequences found in the
    file named filename"""
    with open(filename) as file:
        return [extract_gi_id(line) for line in file if line[0] == '>']

def get_gi_ids_from_files(filenames):
    """Return a list of the GenInfo IDs of all sequences found in the
    files whose names are contained in the collection filenames"""
    idlst = []
    for filename in filenames:
        idlst += get_gi_ids(filename)
    return idlst

def test():
    filenames = ('../data/nadh.fasta',
                 '../data/aa003.fasta',
                 '../data/BacillusSubtilisPlastmidP1414.fasta'
                 )
    print(get_gi_ids_from_files(filenames))

