import SimpleHTTPServer
import SocketServer

PORT = 1336

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print 'serving at port', PORT
httpd.serve_forever()