#_*_coding:utf-8_*_
__author__ = 'FYQ'
import tornado.options
import tornado.httpserver
import tornado.web
import tornado.ioloop
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from Login import LoginHandler,LogoutHandler
from Handlers import IndexHandler,ExecutionCommandHandler,UserHandler,FileUploadHandler
from tornado.options import options,define

define('port',default=8010,type=int,help="given port!")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/user', UserHandler),
            (r'/login',LoginHandler),
            (r'/logout',LogoutHandler),
            (r'/command',ExecutionCommandHandler),
            (r'/file',FileUploadHandler)
        ]
        '''
        注释：
        1、通过设置setting中的cookie_secret参数可以调用set_secure_cookie()，对浏览器中的cookie进行签名
        2、通过设置login_url参数，可以调用 @tornado.web.authenticated 装饰器，如果当前页面用户未登录自动定向到该参数
           指定的路由中做验证
           @authenticated 装饰器是 if not self.current_user: self.redirect() 的简写. 可能不适合非基于浏览器的登录方案.
        '''
        setting = dict(
            debug = True,
            template_path=os.path.join(os.path.dirname(__file__),'template'),
            static_path = os.path.join(os.path.dirname(__file__),'static'),
            cookie_secret = 'AopX1UDniYytT3TwKxdw',
            login_url = '/login'
        )
        tornado.web.Application.__init__(self,handlers=handlers,**setting)
        self.user_list = {
            '1': {'login':'fuyuqing','password':'testing.com','role':'root'},
        }

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    print "Listen on http://127.0.0.1:%d" % options.port
    tornado.ioloop.IOLoop.instance().start()
