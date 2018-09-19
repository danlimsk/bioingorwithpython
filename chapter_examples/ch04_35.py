### Example 4-35: Translating DNA sequences, step 4

from ch04_32 import *
from ch04_33 import *
from ch04_34 import *

def translate_with_open_reading_frames(seq, framenum):
    """Return the translation of seq in framenum (1, 2, or 3), with
    ---'s when not within an open reading frame; assume the read is
    not in an open frame when at the beginning of seq"""
    open = False
    translation = ""
    seqlength = len(seq) - (framenum - 1)
    for n in range(framenum-1, seqlength - (seqlength % 3), 3):
        codon = translate_DNA_codon(seq[n:n+3])
        open = (open or codon == "Met") and not (codon == "---")
        translation += codon if open else "---"
    return translation

def print_translation_with_open_reading_frame(seq, framenum, prefix):
    print(prefix,
          framenum,
          ' ' * framenum,
          translate_with_open_reading_frames(seq, framenum),
          sep='')

def print_translations_with_open_reading_frames(seq, prefix=''):
    print('\n', ' ' * (len(prefix) + 2), seq, sep='')
    for frame in range(1,4):
        print_translation_with_open_reading_frame(seq, frame, prefix)

def test():
    print_translations_with_open_reading_frames('ATGCGTGAGGCTCTCAA')
    print_translations_with_open_reading_frames('ATGATATGGAGGAGGTAGCCGCGCGCCATGCGCGCTATATTTTGGTAT')
