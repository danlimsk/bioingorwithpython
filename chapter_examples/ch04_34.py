### Example 4-34: Translating RNA sequences, step 3

from ch04_32 import *
from ch04_33 import *

def translate_in_frame(seq, framenum):
    """Return the translation of seq in framenum 1, 2, or 3"""
    return translate(seq[framenum-1:])

def print_translation_in_frame(seq, framenum, prefix):
    """Print the translation of seq in framenum preceded by prefix"""
    print(prefix,
          framenum,
          ' ' * framenum,
          translate_in_frame(seq, framenum),
          sep='')

def print_translations(seq, prefix=''):
    """Print the translations of seq in all three reading frames,
    each preceded by prefix"""
    print('\n' ,' ' * (len(prefix) + 2), seq, sep='')
    for framenum in range(1,4):
        print_translation_in_frame(seq, framenum, prefix)

def test():
    print_translations('ATGCGTGAGGCTCTCAA')
