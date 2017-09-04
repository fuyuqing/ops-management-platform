#_*_coding:utf-8_*_

from __future__ import  division
import psutil

class ProcessMonitor(object):
    '''
    进程监控方法，获取当前资源占用（cpu、内存、I/O）前十的进程
    '''
    def __init__(self):
        self.pids = psutil.pids()

    def processObject(self,pid):
        '''
        接收pid,返回进程对象。
        :param  pid
        :return:
        '''
        p = psutil.Process(pid)
        return p

    def TopItem(self):
        '''
        通过循环获取每个进程的资源信息，进行对比，返回资源占用前十的进程
        :return:
        '''
        value = {}
        for process in self.pids:
            try:
                obj = self.processObject(process)
                value[obj.name()] = obj.cpu_percent()  #此处获取的是该进程的cpu占用百分比
            except psutil.NoSuchProcess as e:
                pass
        result = sorted(value.items(), lambda x, y: cmp(x[1], y[1]), reverse=False)
        return result[:10]

if __name__ == '__main__':
    processMonitor = ProcessMonitor()
    print processMonitor.TopItem()