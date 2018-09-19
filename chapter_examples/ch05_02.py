### Example 5-2: Definition of GenBankFeature

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
        return self.type + '@' + self.locus

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

# Access Methods

    def get_type(self):
        return type

    def get_locus(self):
        return locus

    def get_qualifier(self, name):
        return self.qualifiers.get(name, None)

# Private Support Methods

    def locus_lt(self, other):
        """Is this instance's locus "less than" that of other? This
        could be quite complicated.  This is just a simple
        demonstration that only looks for the first integer."""
        assert type(self) == type(other)     # insisting, not testing
        return ((extract_first_integer(self.get_locus()) or -1) <
                (extract_first_integer(other.get_locus()) or -1))
        # extract_first_integer defined elsewhere; not a method

    def type_lt(self, other):
        assert type(self) == type(other)     # insisting, not testing
        return (self.FeatureNameOrder.find(self.get_type()) <
                other.FeatureNameOrder.find(self.get_type()))

