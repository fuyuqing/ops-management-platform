#_*_coding:utf-8_*_

import requests
import json

class Basic(object):
    def __init__(self):
        '''api url
        '''
        self.url = 'http://10.0.0.4/api_jsonrpc.php'
        self.header = {
            'Content-Type':'application/json-rpc',
        }
        self.data = {
            "jsonrpc":"2.0",
            "method":"user.login",
            "params": {
                "user":"admin",
                "password":"testpasswd"
            },
            "id":0,
            "auth":None
        }

    def getToken(self):
        '''get auth token'''
        try:
            response = requests.post(url=self.url,json=self.data,headers=self.header)
        except Exception,e:
            return e
        return json.loads(response.text)['result']

    @classmethod
    def getHost(cls):
        '''get all host'''
        data = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": ["hostid", "host"],
                "selectInterfaces": ["interfaceid", "ip"]
            },
            "id": 0,
            "auth": cls().getToken()
        }
        try:
            response = requests.post(url=cls().url, json=data, headers=cls().header)
        except Exception, e:
            return e
        return response.text

    @classmethod
    def getItemId(cls):
        '''get specfied item'''
        data = {
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": "extend",
                "hostids": "10150",
                "search": {
                    "key_": "vfs.fs.size"
                },
                "sortfied": "name"
            },
            "auth": cls().getToken(),
            "id": 0
        }
        item_id = []
        try:
            response = requests.post(url=cls().url, json=data, headers=cls().header)
        except Exception, e:
            return e
        for i in json.loads(response.text)['result']:
            if 'pfree' in i['key_']:
                item_id.append(i['itemid'])
        return item_id

if __name__ == '__main__':
    a = Basic()
    print a.getToken()
    print Basic.getItemId()
    print Basic.getHost()

