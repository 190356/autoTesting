#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/6/14 13:43
# @Author  : vivid
# @FileName: testexcel04.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
import xlsxwriter
import xlrd
import re
from DestroyerRobot.automation.util.RandomUtil import TestRamdom
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
class xlsxoper():
    """
    操作excel文件如果判断文件不存在也不会主动创建新文件
    """
    def __init__(self,path):
        self.path = path

    #向表格内写入
    def writeXLS(self,headings,data=None,datanums=20,sheet1='Sheet1'):
        """
        对文件是否存在进行判断
        :param headings:    #headings = ['Number', 'testA', 'testB']
        :param datanums:    默认循环次数，如果数据为None将循环20次
        :param sheet1:      页表
        :param data:
        #42-51行 ：判断是否采用随机数操作写入文件
        :return:
        """
        testos = SystemOs()
        if testos.is_file(self.path):
            try:
                workbook = xlsxwriter.Workbook(self.path) #新建excel表
                worksheet = workbook.add_worksheet(sheet1) #新建sheet（sheet的名称为"sheet1"）
                # data = [
                #     ['2017-9-1', '2017-9-2', '2017-9-3', '2017-9-4', '2017-9-5', '2017-9-6'],
                #     [10, 40, 50, 20, 10, 50]
                # ]
                # worksheet.write_row('A1', headings)
                # worksheet.write_column('A2', data[0])
                # worksheet.write_column('B2', data[1])
                # worksheet.write_column('C2', data[2])
                if data is None:
                    data=[]
                    for j in range(len(headings)):
                        lists=[]
                        for i in range(datanums):
                            trandom = TestRamdom()
                            lists.append(trandom.RandomTest())
                        data.append(lists)
                else:
                    pass

                worksheet.write_row('A1', headings)
                column=[
                        'A2','B2','C2','D2','E2','F2',
                        'G2','H2','I2','J2','K2','L2',
                        'M2','N2','O2','P2','Q2','R2','S2',
                        'T2','U2','V2','W2','X2','Y2','Z2',
                        ]
                for i in range(len(headings)):
                    print(data[i])
                    worksheet.write_column(column[i], data[i])
            except Exception as e:
                print(e)
            finally:
                workbook.close()
        else:
            msg = "文件不存在"
            return msg

    #读取表格内数据
    def readerXLS(self,sheet1='Sheet1'):
        testos = SystemOs()
        if testos.is_file(self.path):
            workbook = xlrd.open_workbook(self.path)  #打开文件
            booksheet = workbook.sheet_by_name(sheet1)  #获取sheet内的汇总数据
            # print(booksheet.nrows)
            # print(booksheet.ncols)
            p = list()
            for row in range(booksheet.nrows):
                row_data = []
                for col in range(booksheet.ncols):
                    cel = booksheet.cell(row, col)
                    val = cel.value
                    try:
                        val = cel.value
                        '''
                        r\s 去除空格
                        re.sub(pattern, repl, string, count=0, flags=0)
                        re.sub
                        用于替换字符串的匹配项。如果没有匹配到规则，则原字符串不变。
                        第一个参数：规则
                        第二个参数：替换后的字符串
                        第三个参数：字符串
                        第四个参数：替换个数。默认为0，表示每个匹配项都替换
                        '''
                        val = re.sub(r'\s+', '', val)
                    except:
                        pass
                    if type(val) == float:
                        val = int(val)
                    else:
                        val = str(val)
                    row_data.append(val)
                p.append(row_data)
            return p
        else:
            msg = "文件不存在"
            return msg


if __name__=='__main__':
    file_addrec = 'E:\\python_workspace\\DestroyerRobot\\automation\\datas_template\\test_data.xlsx'
    xls=xlsxoper(file_addrec)
    p=xls.readerXLS('test_data')
    print(p)
    for i in p:
        print(i)
        for j in i:
            #print(j)
            pass

#    xls.do_excel()

#     data = [
#         ['2017-9-1', '2017-9-2', '2017-9-3', '2017-9-4', '2017-9-5', '2017-9-6'],
#         [10, 40, 50, 20, 10, 1000]
#     ]
#     xls.writeXLS(['序列号', '兑换码'],data)





