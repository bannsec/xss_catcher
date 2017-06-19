#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import shlex
import os, os.path
import time
from urllib.parse import urlparse, parse_qs
import json
import argparse

def saveRequest(request):
    """
    Given an HTTPRequest class, save it
    """

    peerIP,peerPort = request.connection.getpeername()

    baseDir = os.path.join(request.headers['host'],peerIP,str(time.time()))
    baseDir = shlex.quote(baseDir).replace(".","_")

    os.makedirs(baseDir,exist_ok=True)

    # Save the path
    with open(os.path.join(baseDir,"path"),"w") as f:
        f.write(request.path)

    # Save Headers
    headerDir = os.path.join(baseDir,"headers")
    os.makedirs(headerDir,exist_ok=True)
    
    for header in request.headers:
        with open(os.path.join(headerDir,shlex.quote(header).replace(".","_")),"w") as f:
            f.write(request.headers[header])
    
    # Save GET arguments
    getDir = os.path.join(baseDir,"GET")
    os.makedirs(getDir,exist_ok=True)
    
    qs = parse_qs(urlparse(request.path).query)
    
    for arg in qs:
        with open(os.path.join(getDir,shlex.quote(arg).replace(".","_")),"w") as f:
            if len(qs[arg]) == 1:
                f.write(qs[arg][0])
            else:
                f.write(json.dumps(qs[arg]))
        
    


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        saveRequest(self)

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client. If we have the file, give it.
        path = os.path.abspath(os.path.join(os.path.abspath("."),self.path.lstrip("/")))

        # Make sure that the file to give is in a subfolder.
        if os.path.isfile(path) and path.startswith(os.path.abspath(".")):
            with open(path,"r") as f:
                message = f.read()
        else:
            message = ""

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
  print('starting server on {0}:{1} ... '.format(IP,PORT))

  # Server settings
  server_address = (IP, PORT)

  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)

  httpd.serve_forever()


def main():
    global IP
    global PORT

    parser = argparse.ArgumentParser(description='Catch XSS or just record who hits your port.')
    parser.add_argument('-ip', type=str, nargs=1, default='0.0.0.0',
                        help='IP Address to listen on (default 0.0.0.0)')
    parser.add_argument('-port', type=int, nargs=1, default=8000,
                    help='Port to listen on (default 8000)')    
    
    args = parser.parse_args()


    IP = args.ip
    PORT = args.port
    
    run()

if __name__ == "__main__":

    main()
