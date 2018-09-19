### Example 4-23: Printing the codon table

from ch03_translate import translate_RNA_codon

DNA_bases = ('T', 'C', 'A', 'G')

def translate_DNA_codon(codon):
    return DNA_codon_table[codon]

def print_codon_table():
    """Print the DNA codon table in a nice, but simple,
    arrangement"""
    for base1 in DNA_bases:            # horizontal section (or "group")
        for base3 in DNA_bases:        # line (or "row")
            for base2 in DNA_bases:    # vertical section (or "column")
                # the base2 loop is inside the base3 loop!
                print(base1+base2+base3,
                      translate_DNA_codon(base1+base2+base3),
                      end='  ')
            print()
        print()

def test():
    print()
    print_codon_table()
