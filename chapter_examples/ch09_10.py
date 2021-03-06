### Example 9-10: Running a simple web server

import sys
import http.server

def run(port=8000,
        server_class=http.server.HTTPServer,
        handler_class=http.server.SimpleHTTPRequestHandler):
    httpd = server_class(('', port), handler_class)
    print('Serving on port', port, file=sys.stderr) # added to book example
    httpd.serve_forever()
run()
