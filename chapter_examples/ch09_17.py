### Example 9-17: Response Templates for the recognition site script
###
### See cgi/enzymes_for_site.py for the full example combining
### Examples 9-15 through 18

import string
import cgi

none_recognized_template = string.Template( 
    '''<i>No enzymes recognize <b>$seq</b>.</i>\n''') 

response_template = string.Template( 
    '''<p>Enzyme(s) recognizing <b>$seq</b> are: 
<ol> 
$items 
</ol> 
''')

