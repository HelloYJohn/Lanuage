#!/usr/bin/python
import json
import requests

key = "97b994a815c5413db829191289188e03"
id = 616519

api_url = "http://openapi.tuling123.com/openapi/api/v2"
text_input = "你好呀"

req = {
    "perception":
    {
        "inputText":
        {
            "text": text_input
        }
    },
    "userInfo": 
    {
        "apiKey": key,
        "userId": id
    }
}
req2 = {'reqType': 0, 'perception': {'inputText': {'text': '你好'}}, 'userInfo': {'apiKey': '97b994a815c5413db829191289188e03', 'userId': 616519}}
req2 = json.dumps(req2).encode('utf-8')
ret = requests.post(api_url, req2)
content = ret.text

jsons = json.loads(content, encoding='utf-8')
print(jsons)
if jsons['intent']['code'] >= 10000:
    print(jsons['results'][0]['values']['text'])
