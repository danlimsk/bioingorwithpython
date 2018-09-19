### Example 9-15: Reading Rebase data into a reversed dictionary
###
### See cgi/enzymes_for_site.py for the full example combining
### Examples 9-15 through 18

def read_table(filename):
    table = {}
    linenum = 0
    with open(filename) as fil:
        for line in fil:
            linenum += 1
            enzyme, sequence = line.split()
            sequence = sequence.replace('^', '')    # ignore cut sites
            if sequence in table:
                table[sequence].add(enzyme)
            else:
                table[sequence] = {enzyme} # first enzyme for sequence
            table.get(sequence, set()).add(enzyme)
    print(linenum)
    return table

if __name__ == '__main__':
    tbl = read_table('../data/rebase-simple-table.txt')
    print(len(tbl))

