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
        if ('png' in path.split('.')[-1]):
          self.send_header('Content-type','image/png')
        else:
          self.send_header('Cotnent-type','text/html')
          
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
    text="<blockquote>%s</blockquote>" % urllib.unquote(params['text'])
    try:
        html=urllib.unquote(params['html'])
        text=open(html,'r').read()
    except:
        pass
    self.wfile.write('''
<html>
<head>
  <title>%s</title>
  <link rel="stylesheet" href="demo.css">
  <link href="https://fonts.googleapis.com/css?family=Armata" rel="stylesheet">
</head>
<body>
 <h1>%s</h1>
 %s
 <div id=terminal><iframe src="http://127.0.0.1:8081/tmux" height=70%% width=95%%></iframe></div>
 <section id=bottom>
 <div id='left'><img src="http://127.0.0.1:8080/lisa2016.png" height=5%%></div>
 <div id='right'><a href="https://goo.gl/iqmPd7">https://goo.gl/iqmPd7</a></div>
 </section>
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
