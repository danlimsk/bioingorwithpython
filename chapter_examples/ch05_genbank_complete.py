from utilities import expect_equal

class GenBankEntry:

    Instances = {}

    def __init__(self, accession, gid, source, features, sequence):
        self.accession, self.version = accession.split('.')
        self.gid = gid
        self.sequence = sequence
        self.source = source
        self.features = features
        self.Instances[self.gid] = self

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

    def get_feature_qualifier(self, n, propname):
        return self.features[n][2].get(propname, None)

    def feature_counts(self):
        """Return a dictionary showing the number of each type of
        feature in this GenBank entry"""
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

class GenBankFeature:

    # interesting use of a class field!
    FeatureNameOrder = ('gene', 'promoter', 'RBS', 'CDS')

# Fundamental Methods

    def __init__(self, feature_type, locus, qualifiers):
        self.type = feature_type
        self.locus = locus
        self.qualifiers = qualifiers

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
