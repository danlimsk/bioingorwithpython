#!/usr/local/bin/python3

### Example 9-14: A CGI echo script

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
