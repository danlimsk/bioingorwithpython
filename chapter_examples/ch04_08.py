### Example 4-8: Doing something to (print) each element

from ch03_random_codons import random_codons

def print_collection(collection):
    for item in collection:
        print(item)
    print()

def test():
    codon_lists = [random_codons() for n in range(6)]
    print(codon_lists)
    print()
    print_collection(codon_lists)
