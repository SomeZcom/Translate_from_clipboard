# coding=utf-8
import requests
import json

class BaiduFanyi:
    def __init__(self, trans_str):
        self.trans_str = trans_str
        self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
        self.url = 'http://fanyi.baidu.com/basetrans'
        self.post_data = {"query":self.trans_str,"from":"en","to":"zh",}

    def response(self, url, data, headers):
        page = requests.post(url, data=data, headers=headers)
        response_json = json.loads(page.content.decode())

        return response_json

    def get_translate(self, dict_ret):
        ret = dict_ret["dict"]['symbols'][0]['parts']
        for w in ret:
            wordmeans = w['part'] + ':'
            for m in w['means']:
                wordmeans += m + ','
            print(wordmeans)

    def run(self):
        rj = self.response(self.url, self.post_data, self.headers)
        self.get_translate(rj)

if __name__ == '__main__':
    B = BaiduFanyi('mean')
    B.run()
