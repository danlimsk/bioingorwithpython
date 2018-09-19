### Used by ch11_plot_histogram

"""Get and prepare data for barcharts of codon usage for a particular
species, in number per 1000 coding bases."""

# Uses the datafile gbbctspsum downloaded from
# ftp://ftp.kazusa.or.jp/pub/codon/current
# and saved in data/bacteria_codon_counts.txt

# Structure of file is simply:
# orgnum:Genus species[ subspecies]: N
# 64 integers

# orgnum is a number used for queries at the site

# N is the number of coding sequences.

# Example:
# 33075:Acidobacterium capsulatum: 2
# 3 71 15 4 2 0 0 21 56 5 1 6 4 6 21 4 11 1 3 25 22 2 5 10 25 8 7 38 38 4 7 39 14 6 4 20 37 2 5 54 15 12 4 41 10 9 41 41 46 25 13 9 6 0 14 11 0 32 29 27 11 1 1 0

# Numbers are bases per thousand in the identified genes of the organism.

# Must get code table info from somewhere else (genbank query for the
# genome, I guess). Here I am just assuming only bacterial -- in fact,
# I think the table only contains bacteria, though I don't think its
# web page says that.

# 11. The Bacterial, Archaeal and Plant Plastid Code (transl_table=11)

#     AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
#   Starts = ---M---------------M------------MMMM---------------M------------
#   Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
#   Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
#   Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

# WARNING: there were some lines with counts in the hundreds,
# thousands, or even tens of thousands; I have removed them.

# can't use a dictionary because the ordering of the codons is
# fixed, both within an animo acid group and the ordering of the groups
count_table = (
    ('R', 'CGA', 'CGC', 'CGG', 'CGT', 'AGA', 'AGG'),
    ('L', 'CTA', 'CTC', 'CTG', 'CTT', 'TTA', 'TTG'),
    ('S', 'TCA', 'TCC', 'TCG', 'TCT', 'AGC', 'AGT'),
    ('T', 'ACA', 'ACC', 'ACG', 'ACT'),
    ('P', 'CCA', 'CCC', 'CCG', 'CCT'),
    ('A', 'GCA', 'GCC', 'GCG', 'GCT'),
    ('G', 'GGA', 'GGC', 'GGG', 'GGT'),
    ('V', 'GTA', 'GTC', 'GTG', 'GTT'),
    ('K', 'AAA', 'AAG'),
    ('N', 'AAC', 'AAT'),
    ('Q', 'CAA', 'CAG'),
    ('H', 'CAC', 'CAT'),
    ('E', 'GAA', 'GAG'),
    ('D', 'GAC', 'GAT'),
    ('Y', 'TAC', 'TAT'),
    ('C', 'TGC', 'TGT'),
    ('F', 'TTC', 'TTT'),
    ('I', 'ATA', 'ATC', 'ATT'),
    ('M', 'ATG'),
    ('W', 'TGG'),
    ('*', 'TAA', 'TAG', 'TGA')
    )

# (Trivial) Collect + Combine
count_order = []
for aa in count_table:
    count_order.extend(aa[1:])

# The dists are unscaled; the data and sorted are scaled

# Manual example for Acidobacterium capsulatum:
ACCdist = [ 3, 71, 15,  4,  2,  0,  0, 21,
           56,  5,  1,  6,  4,  6, 21,  4,
           11,  1,  3, 25, 22,  2,  5, 10,
           25,  8,  7, 38, 38,  4,  7, 39,
           14,  6,  4, 20, 37,  2,  5, 54,
           15, 12,  4, 41, 10,  9, 41, 41,
           46, 25, 13,  9,  6,  0, 14, 11,
            0, 32, 29, 27, 11,  1,  1,  0
            ]

ACCSum = sum(ACCdist)
ACCData = {c: round(1000*v/ACCSum) for c, v in zip(count_order, ACCdist)}
ACCSorted = [(k, ACCData[k]) for k in sorted(ACCData.keys())]

SPastDist = [11, 6, 6, 31, 17, 6, 27, 10,
              15, 43, 47, 36, 39, 10, 11, 23,
              18, 22, 49, 12, 39, 26, 32, 6,
              14, 16, 50, 15, 27, 28, 46, 33,
              21, 56, 29, 23, 16, 47, 80, 27,
              33, 50, 44, 15, 11, 23, 112, 30,
              34, 69, 15, 49, 3, 14, 33, 54,
              16, 56, 93, 57, 25, 7, 0, 1
              ]

SPastSum = sum(SPastDist)
SPastData = {c: round(1000*v/SPastSum) for c, v in zip(count_order, SPastDist)}
SPastSorted = [(k, SPastData[k]) for k in sorted(SPastData.keys())]

default_data_filename = '../data/bacteria_codon_counts.txt'

import sys
from codes import all_codons

bases = 'TCAG'
codons = all_codons(bases)

def find_max_usage(threshold=0, data_filename=default_data_filename):
    maxval = 0
    linenum = 0
    with open(data_filename) as datafile:
        for line in datafile:
            #            divisor = eval(line.split(':')[-1])
            dataline = datafile.readline()
            numbers = [eval(s) for s in dataline[:-1].split()]
            total = sum(numbers)
            if total >= threshold:
                percentages = [round(100*cnt/total, 1) for cnt in numbers]
                linemax = max(percentages)
                if linemax > maxval:
                    maxval = linemax
                    maxline = linenum
                    maxcounts = numbers
                    what = line
            linenum += 2
            if not linenum % 250:
                print('{:>6}'.format(linenum), end = ' ', file=sys.stderr)
            if not linenum % 2500:
                print(file=sys.stderr)
    print(file=sys.stderr)
    return {'maxval': maxval,
            'maxline': maxline,
            'linecount': linenum+1,
            'what': what[:-1],
            'maxcounts': maxcounts}

bacteria_data_filename = '../data/bacteria_codon_counts.txt'

def show_usage_data(data):
    print('\nThe maximum per thousand is', max(data.values()))
    print('The sum of the per thousand data is',
          sum(data.values()),
          end="\n\n")
    for b1 in bases:
        for b2 in bases:
            for b3 in bases:
                print('     {:<4}{:>4}'.
                      format(b1+b2+b3, data[b1+b2+b3]),
                      end = ''
                      )
            print()
        print()

def get_usage_data(name,
                   count_threshold=0,
                   data_filename=bacteria_data_filename):
    """Fetch the usage data (64 integers) for the specified organism,
    e.g. 'Acidobacterium capsulatum' [must match exactly] --
    see list_organisms_matching to search data file for partial
    matches; return normalized to counts per thousand

    return dictionary of counts
    """
    # I thought the file DID have counts per thousands, but the
    # numbers are all over the place, perhaps having something to do
    # witht the last number on the line before the data
    # the usual file search, this time skipping every other line
    counts = []                 # in case we don't find it
    with open(data_filename) as datafile:
        for line in datafile:
            dataline = datafile.readline()
            if line.split(':')[1] == name:
                counts = [eval(s) for s in dataline[:-1].split()]
                break
    if not counts:
        return counts
    total = sum(counts)
    return (None if total < count_threshold
            else {count_order[n]: round(1000*counts[n]/total)
                 for n in range(len(counts))})

from string import Template

def show_max_usage(threshold=100, datafilename=default_data_filename):
    results = find_max_usage(threshold, default_data_filename)
    # using template because format works with attributes of args,
    # but not dictionary fields
    template = Template('''$filename has $linecount lines;
using a count total threshold of $threshold
the maximum percentage was $maxval, found on line $maxline:
$what
$maxcounts
''')
    print(template.substitute(results,
                              filename=datafilename,
                              threshold=threshold)
          # arbitrary extra keywords allowed
          )


if __name__ == '__main__':
    # data = get_usage_data('Acidobacterium capsulatum')
    # assert data  == ACCdist, data
    # done()
    print()
    show_max_usage()
