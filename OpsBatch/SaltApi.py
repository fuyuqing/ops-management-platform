#_*_coding:utf-8_*_
__author__ = "FYQ"
import urllib
import urllib2
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class SaltApi(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.url = "https://10.0.0.2:8000/"
        self.header = {'Accept':'application/json'}

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

    def getGrains(self,target='*',args=None):
        '''
        此方法获取主机 grains.items 的所有信息
        :param target: 目标主机
        :param args:   执行的参数
        :return:  执行结果
        '''
        data = json.dumps({'client':'local','tgt':target,'fun':'grains.items','arg':args,'output':'pprint'})
        header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Auth-Token': self.getToken()
        }
        request = urllib2.Request(self.url,data,header)
        response = urllib2.urlopen(request).read()
        result = json.loads(response)
        return result

    def globalMethod(self,
                          client='local',
                          tgt='*',
                          fun='cmd.run',
                          arg=None,
                          output='pprint'):
        data = json.dumps({'client': client, 'tgt': tgt, 'fun': fun, 'arg': arg, 'output': output})
        header = {
                 'Accept': 'application/json',
                 'Content-Type': 'application/json',
                 'X-Auth-Token': self.getToken()
                 }
        response = urllib2.urlopen(urllib2.Request(self.url, data, header)).read()
        return response

    def getMinions(self,host):
        '''
        此方法通过get方法加上客户端的主机名，直接获取客户端的grains.items信息
        :param host: 目标主机名
        :return: 返回目标的grains.items信息
        '''
        url = self.url + "minions/" + host
        header = {
                 'Accept': 'application/json',
                 'Content-Type': 'application/json',
                 'X-Auth-Token': self.getToken()
                 }
        request = urllib2.Request(url,headers=header)
        response = json.loads(urllib2.urlopen(request).read())
        return response

def main():
    username = 'fuyuqing'
    password = 'salt_pass'
    saltapi = SaltApi(username,password)
    print json.loads(json.dumps(saltapi.list_all_key('centos6','ls /etc')))[0]['centos6'].split('\n')
    # print json.dumps(saltapi.getMinions('centos6'),indent=3)
    # print json.dumps(saltapi.getGrains(target='centos6'),indent=3)
    # print json.dumps(saltapi.list_all_key(target='centos6',args='free -m'),indent=3)

if __name__ == '__main__':
    main()
