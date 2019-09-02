#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/6/6 17:15
# @Author  : vivid
# @FileName: MySQLDB.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
import os,sys
class SystemOs:
    def __init__(self):
        pass

    def is_file(self, filepath):
        """

        :param filepath:
        :return:
        """
        pathBoolean = False
        try:
            if os.path.isfile(filepath):
                pathBoolean = True
        except Exception as e:
            print(e)
        return pathBoolean

    def remove_file(self, filepath):
        """
        删除指定文件
        :param filepath:
        :return:
        """
        isfile = self.isFile(filepath) #isfile()函数判断是否为一般文件
        msg = ""
        try:
            if isfile:
                os.remove(filepath)
                msg = "文件删除成功"
            else:
                msg = "文件不存在"
        except Exception as e:
            print(e)
        return msg

    def mkdirs_file(self, dirpath):
        """
        创建文件目录，先判断文件目录是否存在
        :param dirpath:
        :return:
        """
        if os.path.isdir(dirpath):
            print("目录已经存在，不用创建")
        else:
            os.mkdir(dirpath)

    """
        获取文件路径操作,建议使用sys_path函数进行操作。
    """
    def project_path(self):
        """
        返回项目的根目录 ，
        :return:
        """
        # 获取根项目路径  os.path.dirname(__file__)的作用是 返回脚本的路径，即文件路径中所在的目录（不包含文件名），如果文件名只写的是test.py，则返回空
        curPath = os.path.dirname(__file__)
        #print("curPath==============",curPath)
        rootPath = curPath[:curPath.find("DestroyerRobot") + len("DestroyerRobot/")]
        #print("rootPath==============",rootPath)
        return rootPath

    def sys_path(self, *paths):
        """
        将多个路径组合后返回，第一个绝对路径之前的参数将被忽略，为空 返回rootPath路径， "/"为分隔符
        :param paths:
        :return:返回文件路径
        """
        sysPath = os.path.join(self.project_path(), *paths)
        sysOsPath = sysPath.replace('\\', '/')
        return sysOsPath

if __name__ == "__main__":
    s = SystemOs()
    paths="automation/datas/config.cfg"
    print(s.sys_path())

    #print(s.project_path())


