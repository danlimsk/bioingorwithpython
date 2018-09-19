### Example 10-6: Utilities to support Rebase database loading

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
