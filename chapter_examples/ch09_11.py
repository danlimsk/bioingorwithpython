### Example 9-11: Running a simple web server, finding a free port

import sys
import http.server
import socket                       # for socket.error

def open_port(hostname, startport, server_class, handler_class):
    for portnum in range(startport, startport+100):
        server_address = ('', portnum)
        try:
            return server_class(server_address, handler_class)
        except socket.error:
           pass

def run(port=8000,
        server_class=http.server.HTTPServer,
        handler_class=http.server.SimpleHTTPRequestHandler):
    httpd = open_port('', 8000, server_class, handler_class)
    hostname, portnumber = httpd.socket.getsockname()
    print('Serving HTTP documents on {}, port {}...'
         .format(hostname, port))
    httpd.serve_forever()

run()
