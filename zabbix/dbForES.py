#_*_coding:utf-8_*_

from elasticsearch import Elasticsearch as ES
from datetime import datetime
from host_get import Host_get

class Es_storage(object):
    def __init__(self):
        self.es = ES(hosts="10.0.0.4")
        self.data = Host_get.getHostItem()

    @classmethod
    def insert_data(cls):
        result = cls().es(index="disk_usage",doc_type="OS",body={"any":cls().data,"timestamp":datetime.now()})
        print result

if __name__ == '__main__':
    Es_storage.insert_data()