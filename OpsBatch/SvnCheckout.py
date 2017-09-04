#!/usr/bin/env python
# _*_coding:utf-8_*_
__author__ = "FYQ"
import os
import sys
import json
import shutil

try:
    from pexpect import run  #使用pexpect的run模块来实现命令执行
except ImportError as e:
    sys.stdout.write('''
    please install pexpect Module
    command:
        pip install pexpect
    ''')
    sys.exit(1);

class SvnCheckout(object):
    def __init__(self, projectName):
        self.url = "svn://10.0.0.2/repoistory/"
        self.projectName = projectName
        self.directory = '/data/deploy/'
        self.username = "fuyuqing"
        self.password = "Aibinong.com"
        self.path = self.directory + self.projectName + '/src/'

    def svnCheck(self):
        '''
        先查看是否有此项目目录，如果有就 svn update更新代码到最新版本
        如果没有该项目，则创建项目目录，并且 svn checkout最新代码到该目录
        :return:  返回svn执行结果
        '''
        if os.path.isdir(self.path + self.projectName) and os.path.isdir(
                                self.directory + self.projectName + '/webapps/'):
            try:
                os.chdir(self.path + self.projectName)
                cmd = "svn update"
                [result, status_code] = run(cmd, withexitstatus=True)
                return json.dumps([result, status_code], indent=3)
            except Exception as e:
                return e
        else:
            try:
                os.makedirs(self.path)
                os.mkdir(self.directory + self.projectName + '/webapps/')
                os.chdir(self.path)
                cmd = "svn checkout " + self.url + self.projectName + " --username "\
                      + self.username + " --password " + self.password
                [result, status_code] = run(cmd, withexitstatus=True)
                return json.dumps([result, status_code], indent=3)
            except OSError as e:
                return e

    def doMaven(self):
        '''
        1、判断svn执行结果，成功则执行maven编译打包，否则return错误信息
        2、判断Maven编译打包结果，成功则将打包好的项目到webapps目录，否则return mvn编译的错误信息
        3、拷贝最新编译的项目到webapps目录，失败则return错误信息，否则回显 ‘拷贝完成’
        :return:
        '''
        svncheck = json.loads(self.svnCheck())
        if svncheck[1] != 0:
            return svncheck[0]
        else:
            print svncheck[0]
            print '''
		    svn 更新 or checkout成功！
		    下面进行Maven编译打包。。。
	        '''
            try:
                os.chdir(self.path + self.projectName)
                cmd = "mvn package"
                result, status_code = run(cmd, withexitstatus=True)
                if status_code != 0:
                    return result
                else:
                    sys.stdout.write(result)
            except Exception as e:
                return e
        print '''
		Maven打包完成！
		正在拷贝至webapps目录。。。
	      '''
        try:
            src = self.path + self.projectName + '/target/'
            dst = self.directory + self.projectName + '/webapps/' + self.projectName
            shutil.copytree(src, dst)
        except Exception, e:
            return e
        print '拷贝完成'

if __name__ == '__main__':
    svncheckout = SvnCheckout('java')
    print svncheckout.doMaven()