### Example 4-16: Extracting a sequence by ID from a large FASTA file

def FASTA_search_by_gi_id(id, file):
    for line in file:
        if (line[0] == '>' and str(id) == get_gi_id(line)):
            return read_FASTA_sequence(file)

def FASTA_search_by_gi_id_loop(id, file):
    line = file.readline()
    while (line and not (line[0] == '>' and
                         (str(id) == get_gi_id(line)))):
        line = file.readline()
    return line and read_FASTA_sequence(fil)

def search_FASTA_file_by_gi_id(id, filename):
    """Return the sequence with the GenInfo ID ID from the FASTA file
    named filename, reading one entry at a time until it is found"""
    id = str(id)                      # user might call with a number
    with open(filename) as file:
        return FASTA_search_by_gi_id(id, file)

def read_FASTA_sequence(file):
    seq = ''
    for line in file:
        if not line or line[0] == '>':
            return seq
        seq += line[:-1]

def read_FASTA_sequence_loop(file):
    line = file.readline()
    while line and line[0] != '>':
        seq += line[:-1]
        line = file.readline()
    return seq

def get_gi_id(description):
    fields = description[1:].split('|')
    if fields and 'gi' in fields:
        return fields[(1 + fields.index('gi'))]

def get_gi_id_alternate(description):
    fields = description[1:].split('|')
    return (fields and 'gi' in fields and
            fields[1+fields.index('gi')])

def test():
    filename = '../data/Acidobacterium-capsulatum-coding-regions.fasta'
    seq = '''
MKMKAVSQKALRCAVVLAVALVTAVALPAQNKPYPTAAQLAPTPPMGWNSWNHFAGKVDEADVR
AAAKAMVDSGMAAAGYKYIVIDDTWQGKRDAQGFIHPNSKFPDMPGLIQYVHSLGLKFGIYSSP
GPQTCAGYEGSYGHVQQDAETYARWGVDYLKYDLCSYLGIMHKEAANNPAKALAMQQAAYLKMY
KALAAAGRPIVFSLCQYGIGDVWKWGPSVGGNLWRTTGDIQDNYARMATIGFGQAGLAKYAGPG
HWNDPDMLEVGNGGMTNEEYRTHMSLWALLAAPLIAGNDLSHMSPATLAILTNREVIAVDQDRL
GREGDRVSKNGALEIWAKPLTGGAKAVGLFNRDTQPHSMTLQLSVVNFPPHAHLRDLWRHKTVH
AHHGAYTVTVPAHGVVLLKLTR'''.replace('\n', '')
    assert seq == search_FASTA_file_by_gi_id('225793573', filename)
    print('All tests passed.')

                               
