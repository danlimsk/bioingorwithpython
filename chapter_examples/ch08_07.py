### Example 8-7: Filtering span tags from HTML

pattern = re.compile(r'''
<h(\d)[^>]*?>  # a header start tag, such as <h2>
\s*            # optional whitespace
([^<]*)        # header text before the span
(<span[^>]*>)? # optional span start tag -- a '<span', followed by
               # characters other than > until the first >
(.*?)          # header text after the span
(</span>)?     # optional span end (we aren't checking that this
               # ends the span tag found previously)
\s*            # optional whitespace
</h            # header end tag (we aren't checking that this ends
               # the one just started)
                     ''',
                     re.IGNORECASE | re.DOTALL | re.VERBOSE)

def print_outline(filename):
    with open(filename) as fil:
        for level, pretag, optstart, posttag, optclose in \
            pattern.findall(fil.read()):
            print("{0}{1}{2}".format(' '*3*(int(level) - 1), pretag, posttag))
