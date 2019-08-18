import json

import pymysql
import requests
import schedule as schedule

def GetNewProxy():
    proxy_url = 'http://http.tiqu.alicdns.com/getip3?num=1&type=2&pro=0&city=0&yys=0&port=2&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
    proxy = requests.get(proxy_url)
    print(proxy.text)
    proxy = json.loads(proxy.text)['data'][0]
    proxies = {
        'https': 'http://{0}:{1}'.format(proxy['ip'], proxy['port'])
    }
    connection = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='pythonman',
                db='proxy',
                charset='utf8')

    sql = "update zmproxy set proxy='%s' where id=1" % str(proxies['https'])

    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        connection.close()

        print('修改代理{}'.format(proxies['https']))
    except:
        connection.rollback()  # 发生错误时回滚!


# schedule.every(1).minutes.do(GetNewProxy)
#
#
# while True:
#     schedule.run_pending()

GetNewProxy()




