### The main template for the recognition site script
###
### See cgi/enzymes_for_site.py for the full example combining
### Examples 9-15 through 18

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
