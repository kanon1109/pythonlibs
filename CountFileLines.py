#! /usr/bin/env python
#coding=utf-8
#计算文件内的行数
import datetime
import os
class CountFileLines(object):

    def __init__(self):
        return

    #查找目录下所有某个类型的文件
    def dirFilesLines(self, path, type):
        filesList = os.listdir(path)
        count = 0
        if len(filesList) == 0:
            return 0;
        for file in filesList:
            s = str(file)
            #判断起始字符串是否为.
            if s.startswith("."):
                continue
            #判断是否为目录
            if os.path.isdir(path+"\\"+s) == True:
                count += self.dirFilesLines(path+"\\"+s, type)
                print path+"\\"+s, len(os.listdir(path+"\\"+s))
                continue
            elif s.endswith(type):
                #判断是否是某个后缀名
                #计算行数
                #print "s" + s
                count += self.fileLines(path + "\\" +s)
        return count

    #打开某个文件并计算某个文件的行数
    def fileLines(self, name):
        f = open(name)
        c = f.readlines()
        f.close()
        return len(c)


if __name__ == "__main__":
    starttime = datetime.datetime.now()
    cf = CountFileLines()
    print cf.dirFilesLines(r"E:\workspace\yitongtianxia\src","as")
    endtime = datetime.datetime.now()
    print (endtime - starttime).seconds