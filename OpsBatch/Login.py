#_*_coding:utf-8_*_
__author__ = 'FYQ'
import os
import tornado.web
import binascii

class BaseHandler(tornado.web.RequestHandler):
    '''
    重写父类 RequestHandler的get_current_user()方法，并添加token验证
    '''
    __TOKEN_LIST = {}
    def __init__(self,application,request,**kwargs):
        super(BaseHandler,self).__init__(application,request,**kwargs)

    def new_token(self):
        '''
        生成一个unicode随机字符串，如果串已经存在，则重新生成
        :return: 返回一个唯一的token串
        '''
        while True:
            new_token = binascii.hexlify(os.urandom(16)).decode('utf-8')
            if new_token not in self.__TOKEN_LIST:
                return new_token

    def on_login_success(self,new_token,user_id):
        '''
        登录成功后设置 cookie中的_token为生成的token串，并添加到__TOKEN_LIST中，与用户id相对应
        :param new_token: 生成一个唯一的token串
        :param user_id:  根据 self.application.user_list认证通过将user_id 对应token串写入_TOKEN_LIST字典中
        :return:
        '''
        self.set_secure_cookie('_token',new_token)
        self.__TOKEN_LIST[new_token] = user_id

    def get_current_user(self):
        '''
        重写父类的get_current_user()方法，设置cookie值通过token验证
        :return: 如果token在 __TOKEN_LIST字典中，验证通过，返回该串对应的用户id否则验证失败
        '''
        token = self.get_secure_cookie('_token')
        if token and token in self.__TOKEN_LIST:
            user_id = self.__TOKEN_LIST[token]
            return self.application.user_list[user_id]
        return None

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
        requestData = self.request.body #获取post data数据
        requestuser = {}
        for i in requestData.split('&'):
            #根据客户端请求中的用户数据（username,password）,生成字典
            req_user,req_password = i.split('=')
            requestuser[req_user] = req_password

        login = requestuser['username']
        password = requestuser['password']

        #此下为用户名密码验证逻辑
        login_user_id = None
        for user_id in self.application.user_list:
            if login == self.application.user_list[user_id]['login']:
                login_user_id = user_id  #验证成功，赋值userid
                break
        if not login_user_id:
            #用户名验证失败
            return self.finish("用户名或者密码错误")
        if password != self.application.user_list[login_user_id]['password']:
            #用户密码验证失败
            return self.finish("用户名或者密码错误")

        #以上验证都成功则生成token串，并在cookie中写入 _token = new_token,回显ok，重定向至 r'/'
        new_token = self.new_token()
        self.on_login_success(new_token,login_user_id)
        self.write('ok')
        return self.redirect('/')

class LogoutHandler(BaseHandler):
    '''
    用户登出，重定向至 /login
    '''
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.clear_cookie('_token')
        self.write('退出登录！')
        return self.redirect('/login')