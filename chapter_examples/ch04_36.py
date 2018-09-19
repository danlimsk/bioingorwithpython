### Example 4-36: Translating DNA sequences, step 5

from ch04_32 import *
from ch04_33 import *
from ch04_34 import *
from ch04_35 import *

def print_translations_in_frames_in_both_directions(seq):
    print_translations(seq, 'FRF')
    print_translations(seq[::-1], 'RRF')

def print_translations_with_open_reading_frames_in_both_directions(seq):
    print_translations_with_open_reading_frames(seq, 'FRF')
    print_translations_with_open_reading_frames(seq[::-1], 'RRF')

def test():
    print_translations_with_open_reading_frames_in_both_directions('ATGCGTGAGGCTCTCAA')
    print_translations_with_open_reading_frames_in_both_directions('ATGATATGGAGGAGGTAGCCGCGCGCCATGCGCGCTATATTTTGGTAT')
