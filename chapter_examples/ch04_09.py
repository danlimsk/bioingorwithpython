### Example 4-9: A generalized do function

from ch03_random_codons import random_codons
from ch03_translate import translate_RNA_codon

def do(collection,  fn):
    for item in collection:
        fn(item)

def show_translation(codon):
    print('The translation of',
          codon,
          'is',
          translate_RNA_codon(codon))


def test():
    codons = random_codons(RNAflag = True)
    do(codons, print)
    print()
    do(codons, show_translation)
