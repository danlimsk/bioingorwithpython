### Example 4-33: Translating DNA sequences, step 2

from ch04_32 import *

def translate(seq):
    """Return the animo acid sequence corresponding to the DNA
    sequence seq"""
    translation = ''
    for n in range(0, len(seq) - (len(seq) % 3), 3): # every third base
        translation += translate_DNA_codon(seq[n:n+3])
    return translation

def test():
    assert 'IleProAlaTyrAsnArg' == translate('ATACCGGCCTATAACCGGAA')
    assert 'IleProAlaTyrAsnArg' == translate('ATACCGGCCTATAACCGGA')
    assert 'IleProAlaTyrAsnArg' == translate('ATACCGGCCTATAACCGG')
    print('All tests passed.')
