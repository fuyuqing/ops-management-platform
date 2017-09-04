#_*_coding:utf-8_*_
__author__ = 'FYQ'
import json

class Traverse(object):
    '''
    此类实现了json串解析，暂未完成
    '''
    def __init__(self,obj):
        self.obj = obj

    def checkJsonType(self):
        '''
        检查是否为json类型，如果抛出异常说明不是
        :return: 对象为json为真，否则为假
        '''
        try:
            self.obj = json.loads(self.obj)
        except ValueError:
            return False
        return True

    def traverse(self):
        '''
        将类中传进来的obj解析，此处还未完成，正在DEBUG
        :return:
        '''
        if self.checkJsonType():
            for i in self.obj:
                if isinstance(i,list):
                    for a in i:
                        return self.traverse(a)
                elif isinstance(i,dict):
                    for k,v in i.items():
                        return k + '=' + self.traverse(v)
                else:
                    return i
