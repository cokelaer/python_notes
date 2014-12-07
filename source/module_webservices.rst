Web Services
##############


simulate a web server
==========================

#!/usr/bin/python
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
HTTPServer((‘localhost’, 8000), SimpleHTTPRequestHandler).serve_forever()

Run the script and you’ll be able to access your new web server by visiting the URL http://
localhost:8000/.
