### Example 9-12: Running a CGI server

import sys
import http.server
import socket                       # for socket.error

http.server.CGIHTTPRequestHandler.cgi_directories.append('/cgi')

def open_port(hostname, startport, server_class, handler_class):
    for portnum in range(startport, startport+80):
        server_address = ('', portnum)
        try:
            return server_class(server_address, handler_class)
        except socket.error:
           pass

def run(port=8000,
        server_class=http.server.HTTPServer,
        handler_class=http.server.CGIHTTPRequestHandler):
    httpd = open_port('', 8000, server_class, handler_class)
    hostname, port = httpd.socket.getsockname()
    print("Serving HTTP, including CGIs, on",
          hostname,
          "port",
          port, "...")
    print('Serving HTTP documents and CGI requests on {}, port {}...'
         .format(hostname, port))
    print("CGI directories are:",
          http.server.CGIHTTPRequestHandler.cgi_directories)
    httpd.serve_forever()

run()
