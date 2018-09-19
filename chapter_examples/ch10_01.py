### Example 10-1: Reading Rebase "all enzyme" data

def read_enzymes_from_file(filename):
    with open(filename) as file:
        skip_intro(file)
        return (get_enzymes(file), get_references(file))

def skip_intro(file):
    """Skip through the documentation that appears at the beginning
    of file, leaving it positioned at the first line of the first
    enzyme"""
    line = ''
    while not line.startswith('<REFERENCES>'):
        line = file.readline()
    while len(line) > 1:                # always 1 for '\n'
        line = file.readline()
    return line

def get_enzymes(src):
    enzymes = {}
    enzyme = next_enzyme(src)
    while enzyme:
        enzymes[enzyme[0]] = enzyme     # dict key is enzyme's name
        enzyme = next_enzyme(src)
    return enzymes

def read_field(file):
    return file.readline()[3:-1]

def read_other_fields(file):
    """The name of the enzyme has already been read; read the rest of
    the fields, returning a 7-tuple"""
    return [read_field(file) for n in range(7)]       # read 7 fields

def next_enzyme(file):
    """Read the data for the next enzyme, returning a list of the
    form: [enzyme_name, prototype, source, recognition_tuple, (genus,
    species, subspecies), references_tuple]"""
    name = read_field(file)
    if name:                                 # otherwise last enzyme read
        fields = [name] + read_other_fields(file)
        fields[2] = parse_organism(fields[2])
        fields[7] = [int(num) for num in fields[7].split(',')]
        file.readline()                      # skip blank line
        return fields

def parse_organism(org):
    """Parse the organism details"""
    parts = org.split(' ')
    return (parts[0],
            parts[1],
            None if len(parts) == 2 else ' '.join(parts[2:]))

def skip_reference_heading(file):
    """Skip lines until the first reference"""
    line = file.readline()
    while not line.startswith('References:'):
        line = file.readline()
    file.readline()                           # skip following blank line

def next_reference(file):
    """Return tuple (refnum, reftext) or, if no more, (None, None)"""
    line = file.readline()
    if len(line) < 2:                         # end of file or blank line
        return (None, None)
    else:
        return (int(line[:4]), line[7:-1])

def get_references(file):
    """Return a dictionary of (refnum, reftext) items from the
    references section of file"""

    # using a dictionary here because there are many references
    # and an enzyme may reference several of them
    refs = {}
    skip_reference_heading(file)
    refnum, ref = next_reference(file)
    while refnum:
        refs[refnum] = ref
        refnum, ref = next_reference(file)
    return refs

if __name__ == "__main__":
    if len(sys.argv) < 2:
        filename = '../data/rebase-all-enzyme-data.txt'
    elif len(sys.argv == 2):
        filename = sys.argv[1]
    else:
        print('Usage: read_enzymes [filename]')
    enzymes, references = read_enzymes_from_file(filename)
    print('Read', len(enzymes), 'enzymes and',   # print len instead of
          len(references), 'references')         # contents of huge lists
