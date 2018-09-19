### Example 02-01: A simple function for recognizing a binding site

def recognition_site(base_seq, recognition_seq):
    return base_seq.find(recognition_seq)
    
    
### Example 02-02: Some function definition details

def validate_base_sequence(base_sequence): 
    seq = base_sequence.upper() 
    return len(seq) == (seq.count('T') + seq.count('C') + 
                        seq.count('A') + seq.count('G')) 

### Example 02-03: Using backslash for line continuations

def validate_base_sequence(base_sequence):
    seq = base_sequence.upper()
    return len(seq) == \
                seq.count('A') + seq.count('G') + \
                seq.count('T') + seq.count('C')
    
    
### Example 02-04: Documentation of a function with commented lines

# A short example illustrating various details of function definitions. Given a string ostensibly
# representing a base sequence, return True or False according to whether the string is composed 
# entirely of upper- or lowercase T, C, A, and G characters
def validate_base_sequence(base_sequence):
    # argument should be a string
    seq = base_sequence.upper()
    # ensure all uppercase characters
    return len(seq) == (seq.count('T') + seq.count('C') +
                        seq.count('A') + seq.count('G'))
    
    
### Example 02-05: A function definition with a docstring

def validate_base_sequence(base_sequence):
    """Return True if the string base_sequence contains only
    upper- or lowercase T, C, A, and G characters, otherwise False"""
    seq = base_seq.upper()
    return len(seq) == (seq.count('T') + seq.count('C') +
                        seq.count('A') + seq.count('G'))
    
### Example 02-07: Defining a function to compute GC content

def gc_content(base_seq):
    """"Return the percentage of G and C characters in base_seq"""
    seq = base_seq.upper()
    return (seq.count('G') + seq.count('C')) / len(seq)
    
    
### Example 02-10: Adding an assertion to the gc_content function

def gc_content(base_seq):
    """Return the percentage of G and C characters in base_seq"""
    assert validate_base_sequence(base_seq), \
           'argument has invalid characters'
    seq = base_seq.upper()
    return ((base_seq.count('G') + base_seq.count('C')) /
            len(base_seq))
    
    
### Example 02-11: Adding a “flag” parameter

def validate_base_sequence(base_sequence, RNAflag):
    """Return True if the string base_sequence contains only upper- or lowercase 
    T (or U, if RNAflag), C, A, and G characters, otherwise False""" 
    seq = base_sequence.upper()
    return len(seq) == (seq.count('U' if RNAflag else 'T') +
                        seq.count('C') +
                        seq.count('A') +
                        seq.count('G'))

### Example 02-12: Adding a default value for the flag parameter

def validate_base_sequence(base_sequence, RNAflag=False):
    """Return True if the string base_sequence contains only upper- or lowercase
    T (or U, if RNAflag), C, A, and G characters, otherwise False"""
    seq = base_sequence.upper()
    return len(seq) == (seq.count('U' if RNAflag else 'T') +
                        seq.count('C') +
                        seq.count('A') +
                        seq.count('G'))

### Example 02-14: Generating a random codon

from random import randint

def random_base(RNAflag = False):
    return ('UCAG' if RNAflag else 'TCAG')[randint(0,3)]

def random_codon(RNAflag = False):
    return random_base(RNAflag) + random_base(RNAflag) + random_base(RNAflag)
    
    
### Example 02-15: Naming intermediate results in a function definition

from random import randint

def replace_base_randomly_using_names(base_seq):
    """Return a sequence with the base at a randomly selected position of base_seq replaced
    by a base chosen randomly from the three bases that are not at that position"""
    position = randint(0, len(base_seq) - 1)      # −1 because len is one past end
                                             
    base = base_seq[position]
    bases = 'TCAG'
    bases.replace(base, '')                       # replace with empty string!
    newbase = bases[randint(0,2)]
    beginning = base_seq[0:position]              # up to position
    end = base_seq[position+1:]                   # omitting the base at position
    return beginning + newbase + end
    
    
### Example 02-16: The same function without intermediate result names

def replace_base_randomly_using_expression(base_seq):
    position = randint(0, len(base_seq) - 1)
    return (base_seq[0:position] +
            'TCAG'.replace(base_seq[position], '')[randint(0,2)] +
            base_seq[position+1:])
    
    
### Example 02-17: A function definition with some intermediate names

def replace_base_randomly(base_seq):
    position = randint(0, len(base_seq) - 1)
    bases = 'TCAG'.replace(base_seq[position], '')
    return (base_seq[0:position] +
            bases [randint(0,2)] +
            base_seq[position+1:])
    
    
### Example 02-18: A Python file

def validate_base_sequence(base_sequence, RNAflag = False):
    """Return True if the string base_sequence contains only upper- or lowercase
    T (or U, if RNAflag), C, A, and G characters, otherwise False"""
    seq = base_sequence.upper()
    return len(seq) == (seq.count('U' if RNAflag else 'T') +
                        seq.count('C') +
                        seq.count('A') +
                        seq.count('G'))

def gc_content(base_seq):
    """Return the percentage of bases in base_seq that are C or G"""
    assert validate_base_sequence(base_seq), \
           'argument has invalid characters'
    seq = base_seq.upper()
    return (base_seq.count('G') +
            base_seq.count('C')) / len(base_seq)

def recognition_site(base_seq, recognition_seq):
   """Return the first position in base_seq where recognition_seq
   occurs, or −1 if not found"""
   return base_seq.find(recognition_seq)

def test():
    assert validate_base_sequence('ACTG')
    assert validate_base_sequence('')
    assert not validate_base_sequence('ACUG')

    assert validate_base_sequence('ACUG', False)
    assert not validate_base_sequence('ACUG', True)
    assert validate_base_sequence('ACTG', True)

    assert .5 == gc_content('ACTG')
    assert 1.0 == gc_content('CCGG')
    assert .25 == gc_content('ACTT')

    print('All tests passed.')

test()
    
