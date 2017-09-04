#_*_coding:utf-8_*_
__author__ = "FYQ"
import urllib
import urllib2
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class saltApi(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.url = "https://10.0.0.2:8000/"
        self.header = {'Accept':'application/json'}
#        self.args = None
#        self.target = "*"

    def getToken(self,prefix='login'):
        '''
        此方法用于获取用户的登录token
        :param prefix: 获取token时所需的url
        :return: token_id
        '''
        url = self.url + prefix
        data = urllib.urlencode({'username':self.username,'password':self.password,'eauth':'pam'})
        header = self.header
        request = urllib2.Request(url,data,header)
        response = urllib2.urlopen(request).read()
        result = json.loads(response)
        return result['return'][0]['token']

    def list_all_key(self,target='*', args="test.ping"):
        '''
        此方法允许从控制台向目标主机发送可执行命令,基于 cmd.run
        @:param   target 默认是所有主机，可指定主机名，多个主机名逗号分隔，例，"host1,host2"
        @:param   args  指定向客户端执行的命令
        :return:  目标主机执行完后的输出，JSON
        '''
        data = json.dumps({'client':'local','tgt':target,'fun':'cmd.run','arg':args})
        header = {
            'Accept':'application/json',
            'Content-Type':'application/json',
            'X-Auth-Token': self.getToken()
        }
        request = urllib2.Request(self.url,data,header)
        response = urllib2.urlopen(request).read()
        result = json.loads(response)
        return result['return']

    def minion(self,prefix='minions'):
        '''
        :param
        :return:
        '''
        url = self.url + prefix
        data = json.dumps({'tgt':'*', 'fun':'status.diskusage'})
        header = {'Accept':'application/json',
                  'Content-Type': 'application/json',
                  'X-Auth-Token':self.getToken()}
        request = urllib2.Request(url,data=data,headers=header)
        response = urllib2.urlopen(request)
        result = json.loads(response.read())
        return result['return'][0]['jid']

    def job(self,prefix='jobs'):
        url = self.url + prefix + '/' + self.minion()
        print url
        header = {'Accept':'application/x-yaml','X-Auth-Token':self.getToken()}
        request = urllib2.Request(url,headers=header)
        response = urllib2.urlopen(request).read()
#        result = json.loads(response)
        return response

def main():
    saltapi = saltApi('fuyuqing','salt_pass')
    print saltapi.list_all_key()
    print saltapi.job()

if __name__ == '__main__':
    main()


