### Example 5-5: Defining a subclass

class BaseSequence:

    def __init__(self, seqstring):
        self.seq = seqstring

    def get_sequence(self):
        return self.seq

    def gc_content(self):
        """"Return the percentage of G and C characters in
        base_seq"""
        seq = self.get_sequence.upper()
        return (seq.count('G') + seq.count('C')) / len(seq)

class RNASequence(BaseSequence):      # subclass
    # . . .
    pass
