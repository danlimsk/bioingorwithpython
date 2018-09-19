### Example 4-10: Redefining print_collection using a generalized do

def print_collection(collection):
    do(collection, print)

def test():
    codon_lists = [random_codons() for n in range(6)]
    print(codon_lists)
    print()
    print_collection(codon_lists)

