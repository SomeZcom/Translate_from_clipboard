# coding=utf-8
import requests
import json

class BaiduFanyi:
    def __init__(self, trans_str, lg_from, lg_to):
        self.trans_str = trans_str
        self.language_from = lg_from
        self.language_to = lg_to
        self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
        self.url = 'http://fanyi.baidu.com/basetrans'
        self.post_data = {"query":self.trans_str,"from":self.language_from,"to":self.language_to,}
        self.trans_res = ''

    def response(self, url, data, headers):
        page = requests.post(url, data=data, headers=headers)
        response_json = json.loads(page.content.decode())

        with open('中文.txt', 'w', encoding='utf-8') as f:
            f.write(str(response_json))

        return response_json

    def get_translate(self, dict_ret):
        if 'keywords' in dict_ret:
            self.trans_res = dict_ret['trans'][0]['dst'] + '\n'
            for kw in dict_ret['keywords']:
                keyword = kw['word'] + ':'
                for mean in kw['means']:
                    keyword += mean + '；'
                self.trans_res += keyword + '\n'

        else: 
            ret = dict_ret["dict"]['symbols'][0]['parts']
            for w in ret:
                try:
                    wordmeans = w['part'] + ':'
                    for m in w['means']:
                        wordmeans += m + '；'
                except KeyError:
                    ret = dict_ret['dict']['word_means']
                    wordmeans = ''
                    for m in ret:
                        wordmeans += m + ';'
                
                self.trans_res += wordmeans + '\n'
        print(self.trans_res)

    def run(self):
        rj = self.response(self.url, self.post_data, self.headers)
        self.get_translate(rj)

if __name__ == '__main__':
    translate_str = 'page'
    B = BaiduFanyi(translate_str, 'en', 'zh')
    B.run()
