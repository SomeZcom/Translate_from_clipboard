# coding=utf-8
import requests
import json


headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}

post_data = {
    "query":'page',
    "from":"en",
    "to":"zh",
}

post_url = "http://fanyi.baidu.com/basetrans"

r = requests.post(post_url,data=post_data,headers=headers)

dict_ret = json.loads(r.content.decode())
with open('fanyi.txt', 'w', encoding='utf-8') as f:
    f.write(str(dict_ret))
ret = dict_ret["dict"]['symbols'][0]['parts']
print(type(ret))
for w in ret:
    wordmeans = w['part'] + ':'
    for m in w['means']:
        wordmeans += m + ','
    print(wordmeans)
print("result is :",ret)

