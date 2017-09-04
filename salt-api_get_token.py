#_*_coding:utf-8_*_

import urllib2
import urllib
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://10.0.0.4:1559/login"  #salt-api and salt-master in this server
header = {'Accept':'application/json'}
data = {'username':'fred','password':'aibinong','eauth':'pam'} #post args
data = urllib.urlencode(data)
request = urllib2.Request(url,data,header)
response = urllib2.urlopen(request).read()
result = json.loads(response)
print result['return'][0]['token']
