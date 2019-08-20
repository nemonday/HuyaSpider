import requests

url = 'http://ged.ip3366.net/api/?key=20190820084107625&getnum=10&isp=1&anonymoustype=4&filter=1&area=1&order=2&proxytype=012'

rsp = requests.get(url)

list1 = rsp.text.split(',')

for proxies in list1:
    print(proxies)

