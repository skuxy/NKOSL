#! /usr/bin/python

import BaseHTTPServer
import os
import sys

class SimpleRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print self.path
        sys.stdout.flush()
        if self.path == '/crash':
                os._exit(1337)
        self.wfile.write('HTTP-1.0 200 Okay\r\n\r\nHere is your output for '+self.path)

def run(server_class=BaseHTTPServer.HTTPServer,
    handler_class=SimpleRequestHandler):
    server_address = ('', 1337)
    httpd = server_class(server_address, handler_class)
    print "Starting webserver service"
    httpd.serve_forever()

run()