import time
from random import choice
from threading import Thread

import pymysql
import requests

from Parameter import PC_USER_ANGENT_LIST


def getinfo():
    while True:
        try:
            time.sleep(3)
            connection = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='pythonman',
                db='proxy',
                charset='utf8')

            sql = 'select * from zmproxy where id=1'
            cursor = connection.cursor()
            cursor.execute(sql)
            proxys = cursor.fetchall()

            for proxy in proxys:
                proxies = {
                    'https': proxy[1]
                }


                user_angent = choice(PC_USER_ANGENT_LIST)

                headers = {
                    'User-Agent': user_angent

                }
                rep = requests.get('http://www.kkwwn.com/2019/08/15/hello-world/', proxies=proxies, headers=headers)
                print(rep)
        except:
            pass

thread_01 = Thread(target=getinfo)
thread_02 = Thread(target=getinfo)
thread_01.start()
thread_02.start()


