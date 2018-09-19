import sys
import inspect

def expect_equal(expected, result):
    """Return expected == result, printing an error message
    if not; use by itself or with assert in a statement such as:
        assert expect_equal(3438,
                            count_hypothetical_proteins(gbk_filename)"""
    if expected == result:
        return True
    print('Expected', expected, 'but got', result, file=sys.stderr)
    frm = inspect.getframeinfo(inspect.currentframe().f_back)
    print('\tLine', frm.lineno, 'of file', frm.filename)

DNA_complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
                   'a': 't', 't': 'a', 'c': 'g', 'g': 'c',}

RNA_complements = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C',
                   'a': 'u', 'u': 'a', 'c': 'g', 'g': 'c',}

DNA_codon_table = {
    'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C',
    'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C',
    'TTA': 'L', 'TCA': 'S', 'TAA': '-', 'TGA': '-',
    'TTG': 'L', 'TCG': 'S', 'TAG': '-', 'TGG': 'W',
    'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R',
    'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
    'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
    'CTG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
    'ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S',
    'ATC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
    'ATA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
    'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
    'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G',
    'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
    'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
    'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G',
    }

RNA_codon_table = {
    'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',
    'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',
    'UUA': 'L', 'UCA': 'S', 'UAA': '-', 'UGA': '-',
    'UUG': 'L', 'UCG': 'S', 'UAG': '-', 'UGG': 'W',
    'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R',
    'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
    'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
    'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
    'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',
    'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
    'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
    'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
    'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G',
    'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
    'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
    'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G',
    }

def complement(sequence, RNAflag = False):
    return ''.join(
        [(RNA_complements if RNAflag else DNA_complements)[base]
         for base in sequence])

def translate_sequence(sequence, RNAflag = False):
    return ''.join(
        ([(RNA_codon_table if RNAflag else DNA_codon_table)
          [sequence[n:n+3].upper()]
          for n in range(0, len(sequence), 3)]))

if __name__ == '__main__':
    test_seq = ''.join([base1 + base3 + base2
                        for base1 in 'TCAG'
                        for base2 in 'TCAG'
                        for base3 in 'TCAG'])

    expect_equal('TCAG', complement('AGTC'))

    expect_equal(
        translate_sequence(test_seq),
        'FSYCFSYCLS--LS-WLPHRLPHRLPQRLPQRITNSITNSITKRMTKRVADGVADGVAEGVAEG'
        )

### get_html_file_encoding(filename) ###

import re

encoding_pat = re.compile( 
    b'<meta [^>]*?content *= *[^>]*' +            # just to fit line 
    b'charset *= *([a-zA-Z0-9-]+)', 
    re.I | re.A) 

def get_html_encoding(html): 
    encoding = encoding_pat.search(html) 
    return encoding and encoding.group(1).decode() 

def get_html_file_encoding(filename): 
    with open(filename, 'rb') as file: 
        return get_html_encoding(file.read(2000)) 
