from utilities import expect_equal

"""Extend GenBankFeature and GenBankSequence as necessary to implement
GenBankFeature.get_bases, which retrieves the portion of the
GenBankEntry's base sequence corresponding to the feature's
locus. This requires adding the inverse of the GenBankEntry --
GenBankFeature relationship so that a GenBankFeature can access the
GenBankEntry of which it is a part."""

# The steps are described as follows and marked in the code as ##n##,
# where n is the step number. In some cases, what is at those marks
# is often the code corrected as described by the step notes rather
# than the problem the note says was fixed.

# Step 1: parse locus into a pair of (start, stop) integers (inclusive);
#         test, find off by 1 bug, fix, test.

# Step 2: begin definition of get_bases

# Step 3: realize the base sequence is part of GenBankEntry and the
#         feature doesn't have access to that.
#
#         One way to do this would be to add an argument to
#         GenBankFeature.__init__ to pass it the GenBankEntry, and
#         add that to the call where GenBankFeatures are created.
#         However, if you look at where that call is you can see that
#         all the features are created before the GenBankEntry is, so
#         there is a problem with this approach.
#
#         What we'll do instead is to add code to
#         GenBankEntry.__init__ to tell each feature in the list of
#         features it gets as a parameter value that it is the
#         feature's entry. This is also an example of setting a field
#         from a method not in the instance's class, which in general
#         should be avoided. We could add a set_entry method, but we
#         don't want to give the impression that this is something
#         that could be done arbitrarily. There are sophisticated
#         Python mechanisms for dealing with this issue, but we
#         aren't using them.

# Step 4: Finish definition of get_bases.

# Step 5: Test; off by 1 error, since sequences start at 1 but
#         strings at 0; also it turns out that the locus includes the
#         stop codon, so it is 3 bases longer than expected.

# Step 6: Discover error in simplistic handling of complement sequences:
#         (a) sequence[higher:lower] needs a -1 as a third part of the slice
#         (b) have to complement the sequence on return
#

class GenBankEntry:

    Instances = {}

    def __init__(self, accession, gid, source, features, sequence):
        self.accession, self.version = accession.split('.')
        self.gid = gid
        self.sequence = sequence
        self.source = source
        self.features = features
        self.Instances[self.gid] = self
        for feature in features:    ##3##
            feature.entry = self

    def __str__(self):
        return "GenBankEntry-" + self.get_gid()

    def __repr__(self):
        return "<GenBankEntry {} {} '{}'>".format(self.get_gid(),
                                                  self.get_accession(),
                                                  self.organism()
                                               )

    def get_accession(self):
        return self.accession

    def get_version(self):
        return self.version

    def get_gid(self):
        return self.gid

    def get_sequence(self):
        return self.sequence

    def sequence_length(self):
        return len(self.sequence)

    def get_feature(self, n):
        return self.features[n]

    ##added##
    def get_features_by_locus_tag(self, tag):
        return [feature for feature in self.features
                if feature.get_qualifier('locus_tag') == tag]

    def get_feature_qualifier(self, n, propname):
        return self.features[n][2].get(propname, None)

    def feature_counts(self):
        counts = {}
        for feature in self.features:
            counts[feature.get_type()] = 1 + counts.get(feature.get_type(), 0)
        return counts

    def feature_count(self, feature_name):
        return self.feature_counts().get(feature_name, 0)

    def number_of_genes(self):
        return self.feature_count('gene')

    def genes(self):
        return [(feature[1], feature[2]['gene'])
                for feature in self.features
                if feature[0] == 'gene']

    def feature_ranges(self):
        return [(feature[0], feature[1]) for feature in self.features]

    def organism(self):
        return self.source.get_qualifier('organism')

    def chromosome(self):
        return self.source.get_qualifier('chromosome')

    def is_base_sequence(self):
        return set(self.get_sequence()) <= {'a', 'c', 't', 'g'}

    def gc_content(self):
        return round((100 * ((self.sequence.count('g') +
                              self.sequence.count('c'))) /
                      len(self.sequence)),
                     2)

##7##
complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
               'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
def complement(sequence):
    return ''.join([complements[base] for base in sequence])

class GenBankFeature:

    # interesting use of a class field!
    FeatureNameOrder = ('gene', 'promoter', 'RBS', 'CDS')

# Fundamental Methods

    def __init__(self, feature_type, locus, qualifiers):
        """locus is assumed to be in one of the following forms,
        even though the notation is somewhat richer:
                start..stop
                complement(start..stop)
        """
        self.type = feature_type
        self.qualifiers = qualifiers
        ##1##
        self.locus_string = locus   # we'll keep both forms around
        dotpos = locus.find('..') # local, not field
        try:
            self.locus = ((int(locus[dotpos+2:-1]), int(locus[11:dotpos]))
                          if locus.startswith('complement')
                          else (int(locus[:dotpos]), int(locus[dotpos+2:])))
        except:
            print('Ignoring unrecognized locus form in',
                  'GenBankFeature.__init__:')
            print('\t', locus)

    def __repr__(self):
        """Return a true __repr__ string"""
        return ('GenBankFeature' +
                 repr((self.type, self.locus, self.qualifiers)))
                # repr of the list of arguments __init__ would take

    def __str__(self):
        return self.get_type() + '@' + self.locus()

# Predicates

    def __lt__(self, other):
        if type(self) != type(other):
            raise Exception('Incompatible argument to __lt__: ' +
                            str(other))
        return self.locus_lt(other) and self.type_lt(other)

    def is_gene(self):
        return 'gene' == self.get_type()

    def is_cds(self):
        return 'CDS' == self.get_type()

    def is_base_sequence(self):
        return set(self.get_sequence()) <= {'a', 'c', 't', 'g'}

# Access Methods

    def get_type(self):
        return self.type

    def get_locus(self):
        return self.locus

    def get_qualifier(self, name):
        return self.qualifiers.get(name, None)

    ##2##, with just pass for the body
    ##4##  real definition
    ##6##  fix reverse, and complement
    def get_bases(self):
        """Get the bases corresponding to the locus of the feature"""
        if self.locus:
            seq = self.entry.get_sequence()
            if self.locus[0] < self.locus[1]: # not complement
                return seq[self.locus[0]-1:self.locus[1]-3]
                              ##5## sequence starts at 1, strings start at 0
                              ##5## don't include stop codon
            else:             ##7## complement
                return complement(seq[self.locus[0]-1:self.locus[1]+1:-1])
            # locus[0] - 1 because squences start at 1 and strings at 0
            # since we are going backwards we want to go through locus[1],
            # but slices go "to" not "through". So we subtract 1 to go through.
            # We subtract another 1 sequences start at 1 but strings at 0,
            # so that gives us locus[1]-2. Now we add 3 to not include the
            # stop codon. Whew.

# Private Support Methods

    def locus_lt(self, other):
        """Is this instance's locus "less than" that of other?
        This could be quite complicated. This is just a simple
        demonstration that only looks for the first integer."""
        assert type(self) == type(other)     # insisting, not testing
        return ((extract_first_integer(self.get_locus()) or -1) <
                (extract_first_integer(other.get_locus()) or -1))
        # extract_first_integer defined elsewhere; not a method

    def type_lt(self, other):
        assert type(self) == type(other)     # insisting, not testing
        return (self.FeatureNameOrder.find(self.get_type()) <
                other.FeatureNameOrder.find(self.get_type()))


class GenBankParser:
    """Parse a GenBankEntry file, returning a GenBankEntry instance"""

    def __init__(self):
        self.line = None
        self.linenum = 0            # for debugging
        self.src = None

    # interesting use of a class field!
    AttributePrefix = (21 * ' ') + '/'

# Predicates

    def is_at_version(self):
        return self.line and self.line.startswith('VERSION')

    def is_at_features(self):
        return self.line and self.line.startswith('FEATURES')

    def is_at_attribute_start(self):
        return self.line and self.line.startswith(self.AttributePrefix)

    def is_at_feature_start(self):
        return len(self.line) > 5 and self.line[5] != ' '

    def is_at_sequence_start(self):
        return self.line and self.line.startswith('ORIGIN')

    def is_at_sequence_end(self):
        return self.line and self.line.startswith('//')

# Action

    def parse(self, filename):
        """Use the data in file named filename to create and
        return an instance of GenBankEntry"""
        with open(filename) as self.src:
            accession, gid = self.get_ids()
            feature_generator = self.make_feature_generator()
            source = next(feature_generator)
            features = list(feature_generator) # remainder after source
            seq = self.get_sequence()
            return GenBankEntry(accession, gid, source, features, seq)

# Action Support

    def read_next_line(self):
        """Better to call this than write its one line of code"""
        self.line = self.src.readline() # no need to return, just assign
        self.linenum += 1		   # for debugging

    def get_ids(self):
        """Return the accession and GenInfo IDs"""
        self.read_next_line()
        while not self.is_at_version():
            self.read_next_line()
        parts = self.line.split()
        giparts = parts[2].partition(':')
        return parts[1], giparts[2]

    def skip_intro(self):
        """Skip text that appears in self.src before the first feature"""
        self.read_next_line()
        while not self.is_at_features():
            self.read_next_line()
        self.read_next_line()

    def get_sequence(self):
        """Return sequence at end of file"""
        seq = ''
        self.read_next_line()
        while not self.is_at_sequence_end():
            seq += self.line[10:-1].replace(' ', '')
            self.read_next_line()
        return seq

    def make_feature_generator(self):
        """Return a generator that produces instances of GenBankFeature
        using the data found in the features section of the file"""
        self.skip_intro()
        while not self.is_at_sequence_start():
            yield self.read_feature()

    def read_feature(self):
        """Return an instance of GenBankFeature created from the
        data in the file for a single feature"""
        feature_type, feature_locus = self.line.split()
        self.read_next_line()
        return GenBankFeature(feature_type,
                              feature_locus,
                              self.read_qualifiers())

    def read_qualifiers(self):
        qualifiers = {}
        while not self.is_at_feature_start():
            parts = self.line.strip()[1:].split('=')
            key = parts[0]
            value = '' if len(parts) < 2 else parts[1]
            assert len(parts) < 3, parts
            if value and value[0] == '"':
                value = value[1:]   # remove first quote; last removed later
            qualifiers[key] = self.read_qualifier_value(value)
        return qualifiers

    def read_qualifier_value(self, value):
        """With value the string after a qualifier name and its
        equal and quote, keep reading lines and removing leading
        and trailing whitespace, adding to value until the final
        quote is read, then return the accumulated value"""
        self.read_next_line()
        while (not self.is_at_attribute_start() and
               not self.is_at_feature_start()):
            value += self.line.strip()
            self.read_next_line()
        if value and value[-1] == '"':
            value = value[:-1]  # remove final quote
        return value

if __name__ == '__main__':

    gbe = GenBankParser().parse('../data/Acidobacterium-capsulatum.gbk')
    print(gbe)
    expect_equal(6988, sum(gbe.feature_counts().values()))
    assert expect_equal(gbe.get_features_by_locus_tag('ACP_0033'),
                        [gbe.get_feature(64), gbe.get_feature(65)])
    ##5##
    f65 = gbe.get_feature(65)
    expect_equal((45764, 46003), f65.get_locus())
    f11 = gbe.get_feature(11)
    #print(f65.get_bases())
    expect_equal((4694, 4515), f11.get_locus())

    expect_equal(f65.get_qualifier('translation'),
                 translate_sequence(f65.get_bases()))

    expect_equal(f11.get_qualifier('translation'),
                 translate_sequence(f11.get_bases()))
