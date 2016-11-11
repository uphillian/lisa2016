#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urlparse
import urllib
import os

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    
  #Handler for the GET requests
  def do_GET(self):
    parsed_path = urlparse.urlparse(self.path)
    # if the path matches a file, return it.
    try:
      path = parsed_path.path.lstrip('/')
      if os.path.exists(path):
        self.send_response(200)
        self.send_header('Content-type','image/png')
        self.end_headers()
        f = open(path,'r')
        self.wfile.write(f.read())
        return
    except:
      pass

    params = {
      'title': 'Demo',
      'text': 'Sample text here'
    }
    try:
      params.update(dict([p.split('=') for p in parsed_path[4].split('&')]))
    except:
      pass
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    # Send the html message
    title=urllib.unquote(params['title'])
    text=urllib.unquote(params['text'])
    self.wfile.write('''
<html>
<head><title>%s</title></head>
<body>
 <h1>%s</h1>
 <blockquote>%s<blockquote><br>
 <iframe src="http://localhost:8081/tmux" width=90%% height=70%%></iframe><br>
 <img src="http://localhost:8080/lisa2016.png" height=5%%>
</body>
</html>
''' % ( title, title, text ) )
    return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER
    
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
