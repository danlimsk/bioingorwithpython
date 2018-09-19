### Example 02-07: Defining a function to compute GC content

def gc_content(base_seq):
    """"Return the percentage of G and C characters in base_seq"""
    seq = base_seq.upper()
    return (seq.count('G') + seq.count('C')) / len(seq)
