### Example 5-7: Factoring out common code to a superclass

class BaseSequence:

    @classmethod
    def invalid_chars(self, seqstring):
        return {char for char in seq if char not in self.ValidChars}

    def __init__(self, seqstring):
        invalid = self.invalid_chars(seqstring)
        if invalid:
            raise Exception(
                type(self).__name__ +
                'Sequence contains one or more invalid characters: ' +
                str(invalid))
        self.__seq = seqstring

    def get_sequence(self):
        return self.__seq

    def gc_content(self):
        """"Return the percentage of G and C characters in the sequence"""
        seq = self.get_sequence().upper()
        return (seq.count('G') + seq.count('C')) / len(seq)

class RNASequence(BaseSequence):

    ValidChars = 'UCAGucag'
    CodonTable = {'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',
                   # . . .
                   }

    @classmethod
    def translate_codon(self, codon):
        return self.CodonTable[codon.upper()]

    def __init__(self, seqstring):
        super().__init__(seqstring)

    def translate(self, frame=1):
        """Produce a protein sequence by translating this RNA
        sequence starting at frame 1, 2, or 3"""
        return ''.join([self.translate_codon(self.get_sequence()[n:n+3])
                        for n in
                        range(frame-1,
                              # ignore 1 or 2 bases after last triple
                              len(self.get_sequence()) -
                              (len(self.get_sequence()) - (frame-1)) % 3,
                              3)])

class DNASequence(BaseSequence):

    ValidChars = 'TCAGtcag'
    # construct a string translation table for use with str.translate
    TranslationTable = str.maketrans('TCAGtcag', 'AGUCaguc')

    def __init__(self, seqstring):
        super().__init__(seqstring)             # note absence of self

    def transcribe(self):
        """Produce an instance of RNASequence that is the transcribed
        complement of this sequence"""
        return RNASequence(
            self.get_sequence().translate(self.TranslationTable))
