### Example 10-4: sqlite3 code to create the Rebase database

import sqlite3
datafilename = '../data/rebase.sqlite3'

conn = sqlite3.connect(datafilename)
try:
    conn.executescript('''
DROP TABLE IF EXISTS Organism;
DROP TABLE IF EXISTS Reference;
DROP TABLE IF EXISTS Enzyme;
DROP TABLE IF EXISTS EnzymeReference;

CREATE TABLE Organism(
    OrgID integer PRIMARY KEY,
    Genus text NOT NULL,
    Species text NOT NULL,
    Subspecies text
    );

CREATE TABLE Reference(
    RefID integer PRIMARY KEY,
    Details text NOT NULL
    );

CREATE TABLE Enzyme(
    Name text PRIMARY KEY,
    Prototype text,
    OrgID integer NOT NULL REFERENCES Organism(OrgID),
    Source text NOT NULL,
    RecogSeq text NOT NULL,
    TopCutPos integer,
    BottomCutPos integer,
    TopCutPos2 integer,
    BottomCutPos2 integer
    );

CREATE TABLE EnzymeReference(
    Enzyme text NOT NULL REFERENCES Enzyme(Name),
    RefID integer NOT NULL REFERENCES Reference(RefID),
    PRIMARY KEY(Enzyme, RefID)
    );
''')

except sqlite3.OperationalError as err:
    print(err, file=sys.stderr)
    conn.rollback()               # abort changes
    raise
conn.commit()                         # commit changes
