#_*_coding:utf-8_*_
__author__ = 'FYQ'
import time

class ErrorLog(object):
    def __init__(self,fileLocation,fileSeek=0):
        '''
        初始化两个参数
        :param fileLocation: 要监控的文件位置
        :param fileSeek:  上一次监控的文件指针，默认为从该文件的开头
        '''
        self.fileObject = open(fileLocation,'r')
        self.fileSeek = fileSeek

    def checkError(self):
        '''
        创建对应错误日志的文件对象，seek到上次检测到的文件位置使用readline
        :return: 返回错误行的一个集合列表
        '''
        errorLogList = []
        self.fileObject.seek(self.fileSeek)
        for line in self.fileObject.readlines():
            if '[ERROR]' in line or 'Exception' in line:   #此处添加日志筛选条件
                errorLogList.append(line.strip())
        return errorLogList

    def getFileSeek(self):
        fileNowSeek = self.fileObject.tell()
        self.fileObject.close()
        return fileNowSeek

def main():
    '''
    /tmp/zabbix/errorlog/ 此目录需自行创建：
            mkdir -p /tmp/zabbix/errorlog/
    :return:
    '''
    now = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    fileLocation = '/usr/local/nginx19/logs/host.access.log'
    try:
        fileSeek = open('/tmp/zabbix/errorlog/' + now + '.txt', 'r')
    except IOError:
        fileSeek = open('/tmp/zabbix/errorlog/'+ now + '.txt', 'w')
        fileSeek.close()
        fileSeek = open('/tmp/zabbix/errorlog/' + now + '.txt', 'r')

    fileSeekRead = fileSeek.read()
    if fileSeekRead:
        errorLog = ErrorLog(fileLocation,int(fileSeekRead))
    else:
        errorLog = ErrorLog(fileLocation)
    fileSeek.close()

    fileSeek = open('/tmp/zabbix/errorlog/'+ now + '.txt', 'w')
    errMessage = errorLog.checkError()
    fileSeek.write(str(errorLog.getFileSeek()))
    fileSeek.close()
    return errMessage

if __name__ == '__main__':
    print main()