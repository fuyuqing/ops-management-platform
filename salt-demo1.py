#_*_coding:utf-8_*_

import urllib
import urllib2
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://10.0.0.2:8000/login"
URI = None

def gettoken():
    data = urllib.urlencode({'username':'fuyuqing','password':'salt_pass','eauth':'pam'})
    header = {'Accept':'application/json',}
    req = urllib2.Request(url,data=data,headers=header)
    res = urllib2.urlopen(req)
    print json.loads(res.read())['return'][0]['token']

def ping():
    url = "https://10.0.0.2:8000/"
    data =  json.dumps({'fun':'test.ping','client':'local','tgt':'*'})
    header = {'Accept':'application/json', 'X-Auth-Token': gettoken(),
              'Content-Type':'application/x-www-form-urlencoded;charset=utf-8'}
    req = urllib2.Request(url,data=data,headers=header)
    res = urllib2.urlopen(req)
    return res.read()

def awd(a,b):
    if a == b:
        return b
    else:
        return a

print ping()