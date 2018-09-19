### Example 4-11: Passing a lambda expression to do

from ch03_random_codons import random_codons
from ch04_09 import do

def test():
    collection =  random_codons()
    do(collection, lambda elt: print('\t', elt, sep=''))
