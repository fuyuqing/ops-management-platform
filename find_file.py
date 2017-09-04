#_*_coding:utf-8_*_

import os

class FindFile(object):
    def __init__(self):
        self.result_list = []

    def find_files(self,dir_name,filePrefix_list,exclude_dir=None):
        os.chdir(dir_name)
        for i in os.listdir('.'):
            if os.path.isdir(i) and exclude_dir is not None and i not in exclude_dir:
                self.find_files(i,filePrefix_list,exclude_dir)
            elif os.path.isfile(i) and i.split('.')[-1] in filePrefix_list:
                self.result_list.append(os.path.abspath(i))
        return self.result_list

    def orderByLatest(self):
        pass

    def orderByMaximum(self):
        pass

if __name__ == '__main__':
    find_file = FindFile()
    print find_file.find_files(u'D:\\360安全浏览器下载\\L007-老男孩教育-Python15期VIP视频-16节-avi',['avi','txt'],['day6计算机作业讲解'])