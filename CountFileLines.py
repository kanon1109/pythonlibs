#! /usr/bin/env python
#coding=utf-8
#计算文件内的行数
import datetime
import os
class CountFileLines():
    #行数信息字典
    lineList = []
    def __init__(self):
        return

    #查找目录下所有某个类型的文件
    def dirFilesLines(self, path, type):
        lineList = []
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
                continue
            elif s.endswith(type):
                #判断是否是某个后缀名
                #计算行数
                lines = self.fileLines(path + "\\" +s)
                count += lines
                self.lineList.append({"file": s, "lines":lines})
                print "file" , s , "lines", lines
        return count

    #打开某个文件并计算某个文件的行数
    def fileLines(self, name):
        f = open(name)
        c = f.readlines()
        f.close()
        return len(c)

    #根据文件的行数排序
    def sort(self):
        length = len(self.lineList)
        if length == 0:
            print "请先执行 dirFilesLines"
            return
        #根据第一个关键字排序
        self.lineList.sort(key=lambda obj:obj.get('lines'), reverse=True)
        print "len", length

        for o in self.lineList:
            print o


if __name__ == "__main__":
    starttime = datetime.datetime.now()
    cf = CountFileLines()
    print cf.dirFilesLines(r"E:\workspace\benbentiaotiao\src","as")
    endtime = datetime.datetime.now()
    print (endtime - starttime).seconds
    cf.sort()
