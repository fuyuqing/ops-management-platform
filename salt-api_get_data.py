#_*_coding:utf-8_*_

import urllib
import urllib2
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://10.0.0.4:1559"
header = {
    'Content-Type':'application/json',
    'Accept':'application/x-yaml',
    'X-Auth-Token':'9a1d2b93fa7b3bfadb551597559cf3168ddb8c73'
}
data = [{'client':'local','tgt':'*','fun':'test.ping'}]
data = json.dumps(data)

request = urllib2.Request(url,data,header)
response = urllib2.urlopen(request).read()
#result = json.loads(response.read())
print response