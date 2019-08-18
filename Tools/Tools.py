import json
import lxml.html
import requests


class SpiderTool(object):
    def __init__(self):
        pass

    @staticmethod
    def xpath_match(url, xpath_dict):
        try:
            etree = lxml.html.etree
            rsp = requests.get(url)
            eroot = etree.HTML(rsp.text)
            data = {}

            if xpath_dict['match'] is 'True':
                for primary, xpath in xpath_dict['match_info'].items():
                    data[primary] = eroot.xpath(xpath)[0]

                return json.dumps(data)

            elif xpath_dict['matchs'] is 'True':
                info_list = eroot.xpath(xpath_dict['infos_xpath'])

                for info in info_list:
                    for key, xpath in xpath_dict['matchs_info'].items():
                        title = info.xpath(xpath_dict['key'])[0]
                        data[title] = {}
                        data[title][key] = info.xpath(xpath)[0]

                return json.dumps(data)

            else:
                return json.dumps({'message': '参数不全'})

        except Exception as f:
            return json.dumps({'message': '{}'.format(f)})

