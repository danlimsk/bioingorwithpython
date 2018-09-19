### Example 8-18: Getting content from all occurrences of a tag

import sys
import xml.parsers.expat

class GenomeProteinNameParser:

    def __init__(self):
        self.titleflag = False
        self.proteins = []                      # a form of collect iteration
        self.count = 0                          # just for user feedback
        self.parser = xml.parsers.expat.ParserCreate()
        self.parser.buffer_text = True
        # don't break text content at line breaks

        self.parser.StartElementHandler = self.start_element
        self.parser.EndElementHandler = self.end_element
        self.parser.CharacterDataHandler = self.char_data

    def start_element(self, name, attrs):
        """Keep a count of all Seqdesc_title tags and print a period
        to the terminal every 250 tags; if name == 'Seqdesc_title',
        turn on titleflag & ignore attrs"""
        if name == 'Seqdesc_title':
            self.titleflag = True
            self.count += 1
            if not self.count % 250:
                print(self.count, file=sys.stderr)
                # sys.stderr so not buffered

    def end_element(self, name):
        """Set titleflag to False as soon as any end element is encountered"""
        self.titleflag = False # regardless of close tag

    def char_data(self, text):
        """If last start tag was a Seqdesc_title, then add text to the list of protein names"""
        if self.titleflag:                      # turned on by start_element
            self.proteins.append(text.strip())

    def get_protein_names_from_file(self, filename):
        print('Parsing...')
        with open(filename, 'rb') as file:      # ParseFile requires bytes
            self.parser.ParseFile(file)         # parse entire file
        return self.proteins

def print_protein_names(filename, number):
    p = GenomeProteinNameParser()
    protein_names = p.get_protein_names_from_file(filename)
    print('\n\nFound {} proteins; the first {} are:\n'.
          format(len(protein_names), number))
    for protein_name in protein_names[:10]:
        print(protein_name)

if __name__ == '__main__':
    default_filename = '../data/Acidobacterium-capsulatum.xml'
    print_protein_names(sys.argv[1] if len(sys.argv) > 1
                        else default_filename,
                        sys.argv[2] if len(sys.argv) > 2 else 10)
