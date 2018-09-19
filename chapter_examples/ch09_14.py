#!/usr/local/bin/python3

### Example 9-14: A CGI echo script
### A copy of this is in the cgi subdirectory, named cgi_echo.
### Run ch09_14.py, then type something like the following in a
### browser's address field (in one line, without the ###'s).
###     http://localhost:8000/cgi/cgi_echo.py?enzyme='EcoRI'& 
###     sequence=CCCC&sequence=CCGG&sequence=GGGG 

import cgi
import cgitb
cgitb.enable()

def respond():
    print("Content-Type: text/html")
    print()
    print("<html>\n<head>\n<title>title</title>\n</head>\n<body>")
    args = cgi.FieldStorage()

    # completing the template:
    print('<p>Enzyme:', args.getfirst('enzyme'), '</p>')
    print('<p>Sequences:', args.getlist('sequence'), '</p>')

    print("</body>\n</html>")

if __name__ == '__main__':
    respond()
