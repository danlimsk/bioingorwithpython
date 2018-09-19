### Example 3-8: Generating a random list of codons

from ch03_translate import translate_RNA_codon
from random import randint

def random_base(RNAflag = False):
    return ('UCAG' if RNAflag else 'TCAG')[randint(0,3)]

def random_codon(RNAflag = False):
    return random_base(RNAflag) + random_base(RNAflag) + random_base(RNAflag)

def random_codons(minlength = 3, maxlength = 10, RNAflag = False):
    """Generate a random list of codons (RNA if RNAflag, else DNA)
    between minlength and maxlength, inclusive"""
    return [random_codon(RNAflag)
            for n in range(randint(minlength, maxlength))]
    
    
### Example 3-9: Translating random base sequences

def random_codons_translation(minlength = 3, maxlength = 10):
    """Generate a random list of codons between minlength and
    maxlength, inclusive"""
    return [translate_RNA_codon(codon) for codon in
            random_codons(minlength, maxlength, True)]
    
def test():
    print()
    print(random_base())
    print(random_base())
    print(random_base(False))
    print(random_base(False))
    print()
    print(random_base(True))
    print(random_base(True))
    print(random_base(True))
    print(random_base(True))
    print()
    print(random_codon())
    print(random_codon(False))
    print(random_codon(True))
    print()
    print(random_codons())
    print(random_codons())
    print(random_codons())
    print(random_codons())
    print()
    print(random_codons(6))
    print(random_codons(6, 15))
    print()
    print(random_codons(RNAflag = True))
    print(random_codons(RNAflag = True))
    print()
    print(random_codons_translation())
    print(random_codons_translation(5))
    print()
    print(random_codons_translation(8, 12))
    print(random_codons_translation(8, 12))

