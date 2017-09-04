#_*_coding:utf-8_*_

from basic_token import Basic
import json
import requests

class Host_get(Basic):
    def __init__(self):
        super(Host_get,self).__init__()
        self.tokenid = self.getToken()
        self.data = {
            "jsonrpc":"2.0",
            "method":"host.get",
            "params": {
                "output":["hostid","host"],
                "selectInterfaces":["interfaceid","ip"]
            },
            "id":2,
            "auth": self.tokenid
        }

    def getHost(self):
        host_dict = {}
        try:
            response = requests.post(url=self.url,json=self.data,headers=self.header)
        except Exception,e:
            return e
        for i in json.loads(response.text)['result']:
            host_dict[i['host']] = i['hostid']
        return host_dict

    @classmethod
    def getHostItem(cls):
        tokenid = cls().tokenid
        hostmessage = cls().getHost()
        result_data = {}
        for hostname,hostid in hostmessage.items():
            data = {
                "jsonrpc":"2.0",
                "method":"item.get",
                "params": {
                    "output": "extend",
                    "hostids":hostid,
                    "search":{
                        "key_":"vfs.fs.size"
                    },
                    "sortfied":"name"
                },
                "auth":tokenid,
                "id":1
            }
            response = requests.post(url=cls().url,json=data,headers=cls().header)
            value = {}
            for i in json.loads(response.text)['result']:
                if 'pfree' in i['key_']:
                    value[i['key_']] = i['lastvalue']
            result_data[hostname] = [value]
        return json.dumps(result_data,indent=3)

if __name__ == '__main__':
    host_get = Host_get()
    print json.dumps(host_get.getHost(),indent=3)
    print Host_get.getHostItem()