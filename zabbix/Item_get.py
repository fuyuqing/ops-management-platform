#_*_coding:utf-8_*_

from basic_token import Basic
from host_get import Host_get
import requests
import json

class Item_get(Basic):
    def __init__(self):
        super(Item_get,self).__init__()
        self.data = {
            "jsonrpc":"2.0",
            "method":"item.get",
            "params": {
                "output":"extend",
                "hostids":u"10150",
                "search": {
                    "key_":"vfs.fs.size[/,pfree]"
                },
                "sortfied":"name"
            },
            "auth":self.getToken(),
            "id":1
        }

    def getItemId(self):
        #host_get = Host_get()
        item_id = []
        try:
            response = requests.post(url=self.url,json=self.data,headers=self.header)
        except Exception,e:
            return e
        for i in json.loads(response.text)['result']:
            if 'pfree' in i['key_']:
                print json.dumps(i,indent=3)
        #return item_id

if __name__ == '__main__':
    item_get = Item_get()
    print item_get.getItemId()