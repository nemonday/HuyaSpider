import json
import pymysql
import requests
import lxml.html
from Parameter import *


class GetType(object):
    """
    获取虎牙全站的直播分类及地址
    """
    def __init__(self):
        self.connection = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USERNAME,
            password=MYSQL_PASSWORK,
            db=MYSQL_DATABASE,
            charset='utf8')

    def get_type_list(self):
        """
        获取分类列表
        :return: 出现错误，返回错误信息
        """
        try:
            type_infos = {}
            base_url = 'https://www.huya.com/g'
            etree = lxml.html.etree
            rsp = requests.get(base_url)
            eroot = etree.HTML(rsp.text)
            type_list = eroot.xpath('//*[@id="js-game-list"]/li')
            for type in type_list:
                type_infos['type'] = type.xpath('.//h3[@class="title"]/text()')[0]
                type_infos['url'] = type.xpath('./a/@href')[0]
                cursor = self.connection.cursor()
                cursor.execute('replace into type (type, type_url) values (%s, %s)', (type_infos['type'], type_infos['url']))
                self.connection.commit()

        except Exception as f:
            self.connection.rollback()
            return json.dumps({'message': '{}'.format(f)})

    def run(self):
        self.get_type_list()


if __name__ == '__main__':
    obj = GetType()
    obj.run()