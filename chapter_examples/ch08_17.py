### Example 8-17: Getting the content of several XML tags

import xml.parsers.expat

class GenomeBinomialParser:

    ChunkSize = 4000                # number of bytes to read at a time

    def __init__(self):
        self.parser = xml.parsers.expat.ParserCreate()

        self.parser.buffer_text = True
        # don't break text content at line breaks

        # Install the three standard callbacks
        self.parser.StartElementHandler = self.start_element
        self.parser.EndElementHandler = self.end_element
        self.parser.CharacterDataHandler = self.char_text

    def start_element(self, name, attrs):
        """Record name of start tag just encountered"""
        self.current_tag = name     # ignore attrs

    def end_element(self, name):
        """Stop parsing when species name has been encountered"""
        if name == 'BinomialOrgName_species':
            raise StopIteration

    def char_text(self, text):
        """If current tag is for genus or species, record its
        content"""
        if not text.isspace():
        # checking for whitespace because this function gets called
        # for both tag content and whitespace between the  end of
        # one tag and the beginning of the next
            if self.current_tag == 'BinomialOrgName_genus':
                self.genus = text.strip()
            elif self.current_tag == 'BinomialOrgName_species':
                self.species = text.strip()
    def find_binomial(self, filename):
        """Return (genus, species) as found in the XML genome file
        named filename"""

        # read only ChunkSize characters at a time in case we find it
        # relatively early and to not take up an enormous amount of
        # memory with file contents
        with open(filename) as file:
            try:
                while True:
                    self.parser.Parse(file.read(self.ChunkSize))
            except StopIteration:
                pass
        return self.genus, self.species

if __name__ == '__main__':
    if len(sys.argv) < 2:
        filename = '../data/Acidobacterium-capsulatum-sequences.xml'
    else:
        filename = sys.argv[1]
    p = GenomeBinomialParser()
    print(p.find_binomial(filename))

