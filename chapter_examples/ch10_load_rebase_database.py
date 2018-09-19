#!/usr/bin/env python3

import sqlite3
datafilename = '../data/rebase.sqlite3'

def read_enzymes_from_file(filename):
    with open(filename) as file:
        skip_intro(file)
        return (get_enzymes(file), get_references(file))

def skip_intro(file):
    """Skip through the documentation that appears at the beginning
    of file, leaving it positioned at the first line of the first
    enzyme"""
    line = ''
    while not line.startswith('<REFERENCES>'):
        line = file.readline()
    while len(line) > 1:                # always 1 for '\n'
        line = file.readline()
    return line

def get_enzymes(src):
    enzymes = {}
    enzyme = next_enzyme(src)
    while enzyme:
        enzymes[enzyme[0]] = enzyme     # dict key is enzyme's name
        enzyme = next_enzyme(src)
    return enzymes

def read_field(file):
    return file.readline()[3:-1]

def read_other_fields(file):
    """The name of the enzyme has already been read; read the rest of
    the fields, returning a 7-tuple"""
    return [read_field(file) for n in range(7)]       # read 7 fields

def next_enzyme(file):
    """Read the data for the next enzyme, returning a list of the
    form: [enzyme_name, prototype, source, recognition_tuple, (genus,
    species, subspecies), references_tuple]"""
    name = read_field(file)
    if name:                                 # otherwise last enzyme read
        fields = [name] + read_other_fields(file)
        fields[2] = parse_organism(fields[2])
        fields[7] = [int(num) for num in fields[7].split(',')]
        file.readline()                      # skip blank line
        return fields

def parse_organism(org):
    """Parse the organism details"""
    parts = org.split(' ')
    return (parts[0],
            parts[1],
            None if len(parts) == 2 else ' '.join(parts[2:]))

def skip_reference_heading(file):
    """Skip lines until the first reference"""
    line = file.readline()
    while not line.startswith('References:'):
        line = file.readline()
    file.readline()                           # skip following blank line

def next_reference(file):
    """Return tuple (refnum, reftext) or, if no more, (None, None)"""
    line = file.readline()
    if len(line) < 2:                         # end of file or blank line
        return (None, None)
    else:
        return (int(line[:4]), line[7:-1])

def get_references(file):
    """Return a dictionary of (refnum, reftext) items from the
    references section of file"""

    # using a dictionary here because there are many references
    # and an enzyme may reference several of them
    refs = {}
    skip_reference_heading(file)
    refnum, ref = next_reference(file)
    while refnum:
        refs[refnum] = ref
        refnum, ref = next_reference(file)
    return refs

def create_tables(dbname):
    conn = sqlite3.connect(dbname)
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


def load_data(dbname, enzymes, references):
    """Reorganize the information in the enzymes and references
    dictionaries in accordance with the dbname's schema and load the
    data into the database's tables"""
    try:
        conn = sqlite3.connect(dbname)
        load_reference_data(conn, references)
        organism_ids = load_organism_data(conn, enzymes)
        load_enzyme_data(conn, enzymes, organism_ids)
        load_enzyme_reference_data(conn, enzymes)
        conn.commit()
    except sqlite3.OperationalError as ex:
        print(ex, file=sys.stderr)
        raise            # reraise exception so Python can handle it

def load_reference_data(conn, references):
    for refid, ref in references.items():
        store_data(conn, 'Reference', (refid, ref))

def load_organism_data(conn, enzyme_data):
    """Return a 'reverse' dictionary keyed by the tuples in the list
    enzyme_data, which have the form (Genus, Species, Subspecies);
    the dictionary's values are sequentially generated integer IDs,
    which will be used as foreign keys in the Enzyme table"""
    organism_ids = {}
    for orgid, data in enumerate(enzyme_data.values()):
        # generating OrgIDs as we go
        org = data[2]
        # this is the only part of an enzyme's data that is relevant here
        if not org in organism_ids:
            store_data(conn, 'Organism', (orgid+1,) + org)
            organism_ids[org] = orgid+1
    return organism_ids

def load_enzyme_data(conn, enzymes, organism_ids):
    for data in enzymes.values():
        store_data(conn,
                   'Enzyme',
                   (data[0],                         # name
                    data[1] or None,                 # prototype (None if '')
                    organism_ids[data[2]],           # organism ID
                    data[3]) +                       # source
                   recognition_info(data[4])         # recognition sequence
                    )

def load_enzyme_reference_data(conn, enzymes):
    """For each reference of each element of enzymes add an entry to
    the M-N EnzymeReference table with the name of the enzyme and the
    ID of the reference"""
    for data in enzymes.values():
        for refid in data[7]:                        # refid list
            store_data(conn, 'EnzymeReference', (data[0], refid))

# temporary implementation: does nothing
def recognition_info(seqdata):
    """Parse the recognition sequence data seqdata, returning a tuple
    of the form:

        (sequence, top_cut_pos, bottom_cut_pos,
         top_cut_pos2, bottom_cut_pos2)"""
    return (seqdata, 0, 0, 0, 0)
    
def make_insert_string(tablename, n):
    """Return an INSERT statement for tablename with n columns"""
    return ('INSERT INTO ' + tablename + ' VALUES ' +
            '(' + ', '.join('?' * n) + ')')   # n comma-separated ?s

STORE_STMTS = {tablename: make_insert_string(tablename, ncols)
               for tablename, ncols in
               (('Organism', 4),
                ('Reference', 2),
                ('Enzyme', 9),
                ('EnzymeReference', 2))}

def store_data(conn, tablename, data):
    """Store data into tablename using connection conn"""
    try:
        conn.execute(STORE_STMTS[tablename], data)
    except Exception as ex:
        print(ex)
        raise

def create_database_from_filename(filename, dbname):
    enzyme_data, reference_data = read_enzymes_from_file(filename)
    create_tables(dbname)
    load_data(dbname, enzyme_data, reference_data)

# The purpose of this is to allow calling into functions at any point
def get_connection(db):
    """DB if a connection, new connection if a string"""
    if isinstance(db, str):
        return sqlite3.connect(db)
    elif isinstance(db, sqlite3.Connection):
        return db
    else:
        raise Exception(
            'get_connection: db must be a connection or a string')

def describe_db(db):
    conn = get_connection(db)
    print('\nDatabase', db, 'has the following tables:\n')
    for row in conn.execute(
        "select * from sqlite_master where type='table' order by name"):
        print('\t', row[1], sep='')
        for field in row[-1][(row[-1].find('(')+1):-1].split(', '):
            print('\t\t', field, sep='')
        print()
    describe_data(conn)

def table_count(db, tablename):
    conn = get_connection(db)
    for row in conn.execute("SELECT COUNT(*) FROM " + tablename):
        # even though there's only 1, only way to access
        return int(row[0])

def describe_data(db):
    print('The number of rows in each table is:')
    conn = get_connection(db)
    max_name_length = len(max(STORE_STMTS.keys(), key=len))
    try:
        print()
        for tablename in STORE_STMTS.keys():
            print("\t{1:{0}}{2}".format(
                    max_name_length+2,
                    tablename,
                    table_count(conn, tablename)))
    except Exception as ex:
        print(ex)
        raise
    else:
        conn.close()
# otherwise database locked errors while debugging

if __name__ == "__main__":
    data_filename = '../data/rebase-all-enzyme-data.txt'
    db_filename = '../data/rebase.sqlite3'
    create_database_from_filename(data_filename, db_filename)
    describe_db(db_filename)
