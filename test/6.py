import json

import requests

url = 'https://proxy.horocn.com/api/proxies?order_id=DXSN1642674010105319&num=3&format=json&line_separator=win&can_repeat=no'
rsp = requests.get(url)
proxys = json.loads(rsp.text)

for proxy in proxys:
    host = proxy['host']
    port = proxy['port']

    print(host, port)