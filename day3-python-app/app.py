import os
import http.server
import socketserver

message = os.environ.get("MSG","Hello from DOcker")

PORT = int(os.environ.get("PORT",8080))

class Handler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()
		self.wfile.write(f"<h1>{message}</h1>".encode())

with socketserver.TCPServer(("0.0.0.0",PORT),Handler) as httpd:
	print(f"Serving on port{PORT}")
	httpd.serve_forever()

