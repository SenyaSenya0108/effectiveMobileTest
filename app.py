import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        response_code = 200
        if path == "/":
            response_body = "Hello from Effective Mobile!\n".encode("utf-8")
        elif path == "/healthcheck":
            response_body = "OK\n".encode("utf-8")
        else:
            response_body = "Not Found\n".encode("utf-8")
            response_code = 404

        self.send_response_only(response_code)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(response_body)


hostName = "0.0.0.0"
port = os.environ.get("PORT", 8081)
server = HTTPServer((hostName, port), ServerHandler)
print(f"Сервер запущен: http://{hostName}:{port}")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Работа сервера прервана")

server.server_close()
print("Сервер остановлен...")
