import requests

url = 'http://ged.ip3366.net/api/?key=20190820084107625&getnum=1&isp=1&anonymoustype=3&filter=1&area=1&order=1&proxytype=2'

rsp = requests.get(url)
num = 0
for i in rsp.text.split(','):
    num += 1
    print(i)
    print(num)


