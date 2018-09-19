### Example 5-6: A basic subclass

class RNASequence(BaseSequence):

    CodonTable = {'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',
                  # . . .
                 }

    @classmethod
    def translate_codon(self, codon):
        return self.CodonTable[codon.upper()]

    def __init__(self, seqstring):
        super().__init__(seqstring)   # note that super does not use self

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


    @classmethod
    def invalid_chars(self, seqstring):
        return {char for char in seq if char not in 'UCAGucag'}

    def __init__(self, seqstring):
        invalid = self.invalid_chars(seqstring)
        if invalid:
            raise Exception(
                'Sequence contains one or more invalid character]: ' +
                str(invalid))
        super().__init__(seqstring)

class DNASequence(BaseSequence):

    #construct a string translation table for use with str.translate
    TranslationTable = str.maketrans('TCAGtcag', 'AGUCaguc')

    @classmethod
    def invalid_chars(self, seqstring):
        return {char for char in seq if char not in 'TCAGtcag'}

    def __init__(self, seqstring):
        invalid = self.invalid_chars(seqstring)
        if invalid:
            raise Exception(
                'Sequence contains one or more invalid characters: ' +
                str(invalid))
        super().__init__(seqstring)

    def transcribe(self):
        """Produce an instance of RNASequence that is the transcribed
        complement of this sequence"""
        return RNASequence(    # use string translation table to transcribe
            self.get_sequence().translate(self.TranslationTable))
