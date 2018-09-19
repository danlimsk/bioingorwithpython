### Example 10-8: Simple SELECT statements using the sqlite3 module

import sqlite3
import sys

dbname = '../data/rebase.sqlite3'
conn = sqlite3.connect(dbname)

def execute(query, args=[]):
    print()
    print(query)
    print()
    try:
        for result in conn.execute(query, args):
            print(result)
    except sqlite3.Error as ex:
        print(ex, file=sys.stderr)
        print('Attempted query:', query)
        raise

for query in (
    'SELECT Name, Prototype FROM Enzyme LIMIT 5',
    'SELECT * FROM Organism LIMIT 4 OFFSET 6',
    '''SELECT * FROM Organism
           ORDER BY Genus, Species, Subspecies
           LIMIT 4 OFFSET 6''',
    'SELECT COUNT(*) FROM Organism',
    'SELECT MAX(Name) FROM Enzyme',
    'SELECT COUNT(Subspecies) FROM Organism',
    'SELECT COUNT(DISTINCT Genus) FROM Organism',
    '''SELECT DISTINCT Species FROM Organism
              WHERE Genus = 'Mycobacterium'
              ORDER BY Species, Subspecies ''',
    ):
    execute(query)

conn.close()
