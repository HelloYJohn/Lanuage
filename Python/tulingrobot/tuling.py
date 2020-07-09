#!/usr/bin/python

import json
import urllib.request

key = "97b994a815c5413db829191289188e03"
id = 616519

api_url = "http://openapi.tuling123.com/openapi/api/v2"
text_input = input('我：')

req = {
    "perception":
    {
        "inputText":
        {
            "text": text_input
        },

    },

    "userInfo": 
    {
        "apiKey": key,
        "userId": id
    }
}
# print(req)
# 将字典格式的req编码为utf8
req = json.dumps(req).encode('utf8')
# print(req)

http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
response = urllib.request.urlopen(http_post)
response_str = response.read().decode('utf8')
# print(response_str)
response_dic = json.loads(response_str)
# print(response_dic)

intent_code = response_dic['intent']['code']
results_text = response_dic['results'][0]['values']['text']
print('Turing的回答：')
print('code：' + str(intent_code))
print('text：' + results_text)
