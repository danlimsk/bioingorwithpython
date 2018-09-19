### Example 9-18: Code for the recognition site script

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
    print_response(read_table('../data/rebase-simple-table.txt'),
                   cgi.FieldStorage().getfirst('site'))

if __name__ == "__main__":
    respond()
