#_*_coding:utf-8_*_

__author__ = 'FYQ'

import tornado.options
import tornado.httpserver
import tornado.web
import tornado.ioloop
import os
from OpsBatch.SaltApi import SaltApi
import binascii
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from tornado.options import options,define
define('port',default=8010,type=int,help="given port!")

'''
class BaseHandler(tornado.web.RequestHandler):
'''
'''
此类重写了父类 RequestHandler 的 get_current_user()方法，基于cookie的值，返回当前登录的用户
原因:
   为了在所有的应用程序中实现用户认证需要在请求处理函数中复写 get_current_user()
   方法来判断当前用户, 比如可以基于cookie的值.
'''
'''
    def get_current_user(self):
        return self.get_secure_cookie('user') #获取cookie中user值
'''
class BaseHandler(tornado.web.RequestHandler):
    __TOKEN_LIST = {}
    def __init__(self,application,request,**kwargs):
        super(BaseHandler,self).__init__(application,request,**kwargs)

    def new_token(self):
        while True:
            new_token = binascii.hexlify(os.urandom(16)).decode('utf-8')
            if new_token not in self.__TOKEN_LIST:
                return new_token

    def on_login_success(self,new_token,user_id):
        self.set_secure_cookie('_token',new_token)
        self.__TOKEN_LIST[new_token] = user_id

    def get_current_user(self):
        token = self.get_secure_cookie('_token')
        if token and token in self.__TOKEN_LIST:
            user_id = self.__TOKEN_LIST[token]
            return self.application.user_list[user_id]
        return None

class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('index.html')

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
        self.render("user.html",username=user_name,email=user_email,website=user_website,language=user_language)

class LoginHandler(BaseHandler):
    '''
    @:parameter 登录验证，portal页面使用，未完成
    @:parameter 需要实现用户注册功能、登录token获取、用户信息存储
    '''
    def get(self, *args, **kwargs):
        return self.render('login.html')

    def post(self, *args, **kwargs):
        '''
        获取从login.html页面post过来的几个参数，判断用户名是否正确，正确的话将cookie中user的值设置成对应的用户。
        :param args:
        :param kwargs:
        :return:
        '''
        requestData = json.loads(self.request.body.decode())
        login = requestData['login']
        password = requestData['password']

        login_user_id = None
        for user_id in self.application.user_list:
            if login == self.application.user_list[user_id]['login']:
                login_user_id = user_id
                break
        if not login_user_id:
            return self.finish("用户名或者密码错误")
        if password != self.application.user_list[login_user_id]['password']:
            return self.finish("用户名或者密码错误")

        new_token = self.new_token()
        self.on_login_success(new_token,login_user_id)
        return self.finish('ok')

class ExecutionCommandHandler(BaseHandler):
    '''
    @:parameter 页面执行shell命令，指定主机名
    '''
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        return self.render('command.html')

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
        return self.render('result.html',result = json.dumps(result,indent=3))

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/user', UserHandler),
            (r'/login',LoginHandler),
            (r'/command',ExecutionCommandHandler)
        ]
        '''
        注释：
        1、通过设置setting中的cookie_secret参数可以调用set_secure_cookie()，对浏览器中的cookie进行签名
        2、通过设置login_url参数，可以调用 @tornado.web.authenticated 装饰器，如果当前页面用户未登录自动定向到该参数
           指定的路由中做验证
           @authenticated 装饰器是 if not self.current_user: self.redirect() 的简写. 可能不适合非基于浏览器的登录方案.
        '''
        setting = dict(
            template_path=os.path.join(os.path.dirname(__file__),'template'),
            static_path = os.path.join(os.path.dirname(__file__),'static'),
            cookie_secret = 'AopX1UDniYytT3TwKxdw',
            login_url = '/login'
        )
        tornado.web.Application.__init__(self,handlers=handlers,**setting)
        self.user_list = {
            '1': {'login':'fuyuqing','password':'Aibinong.com','role':'root'},
        }

saltapi = SaltApi('fuyuqing','salt_pass')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
