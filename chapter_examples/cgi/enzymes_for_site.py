#! /usr/local/bin/python3

### Example 9-15 through 9-18 combined into a working program
### You can test this by typing something like this to the
### command line wth:
###     enzymes_for_site.py site=cccggg
###
### You can also run Example 9-12 in the parent directory of
### this file's and 

import string
import cgi
import os.path

table_directory = '../data/rebase-simple-table.txt'
if 'cgi' == os.path.split(os.getcwd())[1]:
    table_directory = '../' + table_directory

html_template = string.Template(    # second line is requisite empty line 
    '''Content-Type: text/html

<head> 
<title>Restriction Enzyme Search</title> 
</head> 
<body> 
<h2>Restriction Enzyme Search</h2> 
$response 
</body> 
</html> 
''') 

none_recognized_template = string.Template( 
    '''<i>No enzymes recognize <b>$seq</b>.</i>\n''') 

response_template = string.Template( 
    '''<p>Enzyme(s) recognizing <b>$seq</b> are: 
<ol> 
$items 
</ol> 
''')

def read_table(filename):
    table = {}
    linenum = 0
    with open(filename) as fil:
        for line in fil:
            linenum += 1
            enzyme, sequence = line.split()
            sequence = sequence.replace('^', '')    # ignore cut sites
            if sequence in table:
                table[sequence].add(enzyme)
            else:
                table[sequence] = {enzyme} # first enzyme for sequence
            table.get(sequence, set()).add(enzyme)
    return table

def make_html_body(table, seq):
    subst = {'seq': seq, 'items': [], 'response': ''}
    if not seq:                     # case 1 -- no value for seq
        subst['response'] = 'No value for site in query arguments'
    else:
        seq = seq.upper()           # doesn't change value in subst dict
        if seq not in table:        # case 2 -- no match found
            subst['response'] = \
                none_recognized_template.substitute({'seq': seq})
        else:                       # case 3 -- found, make list items
            items = '\n'.join(['<li>' + enzyme + '</li>'
                               for enzyme in table[seq]])
            subst['response'] = \
                response_template.substitute({'seq': seq, 'items': items})
    return subst

def print_response(table, seq):
    print(html_template.substitute(make_html_body(table, seq)))

def respond():
    print_response(read_table(table_directory),
                   cgi.FieldStorage().getfirst('site'))

if __name__ == "__main__":
    import os
    respond()
