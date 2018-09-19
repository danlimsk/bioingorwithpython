### Example 5-9: Generalized Sequence class and its subclasses

class Sequence:

    @classmethod
    def invalid_chars(self, seqstring):
        return {char for char in seq if char not in self.ValidChars}

    def __init__(self, seqstring):
        invalid = self.invalid_chars(seqstring)
        if invalid:
            raise Exception(
                type(self).__name__ +
                " contains one or more invalid characters: " +
                str(invalid))
        self.__seq = seqstring

    def get_sequence(self):
        return self.__seq

class BaseSequence(Sequence):

    def __init__(self, seqstring):
        super().__init__(seqstring)

    def gc_content(self):
        """"Return the percentage of G and C characters in the
        sequence"""
        seq = self.get_sequence.upper()
        return (seq.count('G') + seq.count('C')) / len(seq)

class ProteinSequence(Sequence):

    ThreeLetterCodes = { # including ambiguity codes B, X, and Y
                'A': 'Ala', 'B': 'Asx', 'C': 'Cys', 'D': 'Asp',
                'E': 'Glu', 'F': 'Phe', 'G': 'Gly', 'H': 'His',
                'I': 'Ile', 'K': 'Lys', 'L': 'Leu', 'M': 'Met',
                'N': 'Asn', 'P': 'Pro', 'Q': 'Gln', 'R': 'Arg',
                'S': 'Ser', 'T': 'Thr', 'V': 'Val', 'W': 'Trp',
                'X': 'Xxx', 'Y': 'Tyr', 'Z': 'Glx'}

    ValidChars = ''.join(ThreeLetterCodes.keys())
    ValidChars += ValidChars.lower()
    TranslationTable = str.maketrans(ThreeLetterCodes)

    def long_str(self):
        return self.get_sequence().translate(self.TranslationTable)
        # or ''.join([ThreeLetterCodes[key]
        #              for key in self.get_sequence()])

    def __init__(self, seqstring):
        super().__init__(seqstring)

class RNASequence(BaseSequence):

    ValidChars = 'ucagUCAG'

    CodonTable = {'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',
                   # . . .
                   }

    @classmethod
    def translate_codon(self, codon):
        return self.CodonTable[codon.upper()]

    def __init__(self, seqstring):
        super().__init__(seqstring)

    def translate(self, frame=1):
        return ProteinSequence(
            ''.join((self.translate_codon(self.get_sequence()[n:n+3])
                     for n in
                     range(frame-1,
                           len(self.get_sequence()) -
                           ((len(self.get_sequence()) - (frame-1)) % 3),
                           3))))

class DNASequence(BaseSequence):

    ValidChars = 'TCAGtcag'
    # construct a string translation table for use with str.translate
    TranslationTable = str.maketrans('TCAGtcag', 'AGUCaguc')

    def __init__(self, seqstring):
        super().__init__(seqstring)   # note absence of self

    def transcribe(self):
        """Produce an instance of RNASequence that is the transcribed
        complement of this sequence"""
        return RNASequence(
            self.get_sequence().translate(self.TranslationTable))

class AmbiguousDNASequence(DNASequence):

    ValidChars = 'TCAGBDHKMNSRWVY'
    ValidChars += ValidChars.lower()

    def __init__(self, seqstring):
        super().__init__(seqstring)


class BaseSequence(Sequence):
    # . . .

    def complement(self):
        return self(self.get_sequence().translate(self.ComplementTable))

    def gc_content(self):
        """"Return the percentage of G and C characters in the
        sequence"""
        seq = self.get_sequence.upper()
        return (seq.count('G') + seq.count('C')) / len(seq)

class RNASequence(BaseSequence):

    ComplementTrans = str.maketrans('UCAGucag', 'AGUCaguc')
    # . . .

class DNASequence(BaseSequence):

    ComplementTable = str.maketrans('TCAGtcag', 'AGTCagtc')
    # . . .

class AmbiguousDNASequence(DNASequence):

    ComplementTable = str.maketrans('TCAGRYMKSWNBVDH', 'AGTCYRKMSWNVBHD')
    # . . .


class AmbiguousDNASequence(DNASequence):
#### Added to what is shown in the book's example
    def gc_content(self):
        """"Return the percentage of G and C characters in the
        sequence, counting only bases that are either definitely G or
        C or definitely A or T"""
        seq = self.get_sequence.upper()
        gc_count = (seq.count('G') + seq.count('C') + seq.count('S'))
        at_count = (seq.count('A') + seq.count('T') + seq.count('W'))
        return gc_count / (gc_count + at_count)

    # . . .
