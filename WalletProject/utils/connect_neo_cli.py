import simplejson
import requests
import json


def connect_neo(request):
    """连接neo客户端"""
    req = simplejson.loads(request.body)
    jsonrpc = req['jsonrpc']
    method = req['method']
    params = req['params']
    id = req['id']
    data = {
        "jsonrpc": jsonrpc,
        "method": method,
        "params": params,
        "id": id
    }
    headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
    url = "http://127.0.0.1:10332"
    response_json = requests.post(url=url, headers=headers, data=json.dumps(data))
    return response_json.content.decode('utf-8')