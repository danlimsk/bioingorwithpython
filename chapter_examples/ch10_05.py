### Example 10-5: Loading the Rebase database

import sqlite3

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
                   recognition_info(data[4]) +       # recognition sequence
                   ('',)                             # methylation site
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
    return (seq, 0, 0, 0, 0)
    
