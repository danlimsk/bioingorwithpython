### Example 3-15: Reading FASTA entries from a file, binding names

def read_FASTA(filename):
    with open(filename) as file:
        contents = file.read()            # only statement inside the with
    entries = contents.split('>')[1:]     # skip blank first entry
    partitioned_entries = [entry.partition('\n') for entry in entries]
    pairs = [(entry[0], entry[2]) for entry in partitioned_entries]  # omit '>'
    pairs2 = [(pair[0], pair[1].replace('\n', '')) for pair in pairs]
    result = [(pair[0].split('|'), pair[1]) for pair in pairs2]
    return result

print(read_FASTA('../data/aa003.fasta'))
