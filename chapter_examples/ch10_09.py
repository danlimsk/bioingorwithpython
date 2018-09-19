### Example 10-9: WHERE clauses in SELECT statements

import sqlite3

dbfilename = '../data/rebase.sqlite3'

conn = sqlite3.connect(dbfilename)

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
    '''SELECT COUNT(*) FROM Enzyme WHERE Prototype IS NULL''',

    '''SELECT DISTINCT Species FROM Organism
              WHERE Genus = 'Mycobacterium'
              ORDER BY Species''',
    ):
    execute(query)
conn.close()
