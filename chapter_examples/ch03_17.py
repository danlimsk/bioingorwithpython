### Example 3-17: Generating amino acid translations of codons

from ch03_translate import translate_RNA_codon

def aa_generator(rnaseq):
    """Return a generator object that produces an amino acid by
    translating the next three characters of rnaseq each time nextn
    is called on it"""
    return (translate_RNA_codon(rnaseq[n:n+3])
            for n in range(0, len(rnaseq), 3))

seq = 'AUUCGAUCCGGACCCAUGAUCCCG'

print()
print(seq)
gen = aa_generator(seq)
assert 'Ile' == next(gen)
assert 'Arg' == next(gen)
assert 'Ser' == next(gen)
assert 'Gly' == next(gen)
assert 'Pro' == next(gen)
assert 'Met' == next(gen)
assert 'Ile' == next(gen)

gen = aa_generator(seq)
print(''.join(list(gen)))
