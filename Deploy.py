#_*_coding:utf-8_*_

import urllib
import urllib2
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class SaltApi:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.url = "https://10.0.0.2:8000/"
        self.header = {'Accept': 'application/json'}

    def getToken(self, prefix='login'):
        '''
        此方法用于获取用户的登录token
        :param prefix: 获取token时所需的url
        :return: token_id
        '''
        url = self.url + prefix
        data = urllib.urlencode({'username': self.username, 'password': self.password, 'eauth': 'pam'})
        header = self.header
        request = urllib2.Request(url, data, header)
        response = urllib2.urlopen(request).read()
        result = json.loads(response)
        return result['return'][0]['token']

    def getGrains(self,target='*',args=None):
        '''
        此方法验证了可以通过post data里的信息来指定salt请求内容
        :param target: 目标主机
        :param args:   执行的参数
        :return:  执行结果
        '''
        url = self.url
        data = json.dumps({
            'client': 'local','tgt': target,'fun': 'grains.items','arg': args,'output': 'pprint'
        })
        header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Auth-Token': self.getToken()
        }
        request = urllib2.Request(url,data,header)
        response = urllib2.urlopen(request).read()
        return response

    def golobalMethod(self,
                      client='local',
                      tgt='*',
                      fun='cmd.run',
                      arg=None,
                      output='pprint'):
        data = json.dumps({'client':client,'tgt':tgt,'fun':fun,'arg':arg,'output':output})
        header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Auth-Token': self.getToken()
        }
        response = urllib2.urlopen(urllib2.Request(self.url,data,header)).read()
        return response

if __name__ == '__main__':
    username = "fuyuqing"
    password = "salt_pass"
    saltapi = SaltApi(username,password)
    print saltapi.golobalMethod()
