#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'FYQ'
import os
import commands
import time

class LogCompress(object):
    def __init__(self,logpath):
        self.logPath = logpath
        self.fileList = self.getFileList()
        self.compress_record = "/opt/scripts/compress_record.txt"

    def getFileList(self):
        '''
        确定筛选条件，拼接到shell命令中
        :return:  经过筛选后的文件列表
        '''
        timefmt1 = time.strftime('%Y%m%d', time.localtime(time.time()))
        timefmt2 = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        cmd = "find " + self.logPath + " -name '*.log' | egrep -v '(" + timefmt1 + "|" + timefmt2 + "|nginx|cannon|eslog|gc.log)'"
        status,result = commands.getstatusoutput(cmd)
        if status != 0:
            with open(self.compress_record,'a') as f:
                f.write("文件列表获取失败 \n")
        else:
            fileList = result.split('\n')
            return fileList

    def logCompress(self):
        '''
        读取文件列表，将文件名与路径分割，避免压缩时全路径
        :return: None
        '''
        for file in self.getFileList():
            path,filename = os.path.split(file)
            os.chdir(path)
            cmd = "tar zcf " + filename + ".tgz" + " " + filename + " && chown deploy:deploy " + filename + ".tgz" \
                  + " && rm -f " + filename
            status,result = commands.getstatusoutput(cmd)
            if status != 0:
                with open(self.compress_record,'a') as f:
                    f.write(filename +" 文件压缩失败！ \n")

if __name__ == '__main__':
    logpath = "/mnt/logs"
    log_compress = LogCompress(logpath)
    print log_compress.getFileList()
    #log_compress.logCompress()