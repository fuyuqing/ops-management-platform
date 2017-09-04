#_*_coding:utf-8_*_
__author__ = 'FYQ'
import tornado.web
from SaltApi import SaltApi
import json
from Login import BaseHandler
import os

saltapi = SaltApi('fuyuqing','salt_pass')

class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        dh_data = "active"
        return self.render('admin.html',dh = dh_data)

class UserHandler(BaseHandler):
    '''
    此类处理用户信息表单，包括用户注册、用户信息修改等
    '''
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        return self.render('user.html')

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        user_name = self.get_argument("username")
        user_email = self.get_argument('email')
        user_website = self.get_argument('website')
        user_language = self.get_argument('language')
        self.render("user.html",username=user_name,email=user_email,
                    website=user_website,language=user_language)

class ExecutionCommandHandler(BaseHandler):
    '''
    @:parameter 页面执行shell命令，指定主机名
    '''
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        return self.render('command.html',result = '')

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        '''
        如果你使用 authenticated 装饰 post() 方法并且用户没有登录, 服务将返回一个 403 响应.
        :param args:
        :param kwargs:
        :return:
        '''
        command = self.get_argument('command')
        target_host = self.get_argument('target_host')
        if ',' in target_host:
            result_list = {}
            host_list = target_host.split(',')
            for host in host_list:
                result = json.loads( \
                    json.dumps(saltapi.list_all_key(target=host, args=command)))[0] \
                    [host].split('\n')
                result_list[host] = list(result)
            result = result_list
        else:
            result = json.loads( \
                json.dumps(saltapi.list_all_key(target=target_host, args=command)))[0] \
                [target_host].split('\n')
        return self.render('command.html',result = json.dumps(result,indent=3))

class FileUploadHandler(BaseHandler):
    '''
    此处理器实现了tornado的文件上传下载
    '''
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        dirName = os.path.join(os.path.dirname(__file__),'files')
        fileList = os.listdir(dirName)
        return self.render('file.html',fileList = fileList)

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        upload_path = os.path.join(os.path.dirname(__file__),'files')
        print self.request.files
        file_metas = self.request.files['file']
        for meta in file_metas:
            filename = meta['filename']
            filepath = os.path.join(upload_path,filename)
            with open(filepath,'wb') as up:
                up.write(meta['body'])
            self.write('finished')
            return self.redirect('/file')
