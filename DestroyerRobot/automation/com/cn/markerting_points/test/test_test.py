#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/15
# @Author  : vivid-XIEMENG
# @FileName: TestBaidu.py
# @Software: PyCharm
# @email    ：331597811@QQ.com

from selenium import webdriver
from BeautifulReport import BeautifulReport
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPLoing.test_mplogin import mplogin_test
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPTree.test_mptree import test_mptree
from DestroyerRobot.automation.com.cn.markerting_points.servers.newCms.test_NCLogin import Test_NCLogin
from DestroyerRobot.automation.com.cn.markerting_points.servers.newCms.test_NCTransferAudit import test_NCTransferAudit
import unittest
import time
class test_login(unittest.TestCase):
    """
    实现unittest操作，到 run目录运行对应脚本操作
    BeautifulReport记录操作失败截图报告
    """
    def setUp(self):
        self.driver = webdriver.Chrome()


    def tearDown(self):
        self.driver.quit()
    '''
    @BeautifulReport.add_test_img('test_01_mplogin')#失败后会有报告截图
    def test_01_mplogin(self):
        """
        用户登录
        :return:
        """
        mplogin = mplogin_test(self.driver)
        mplogin.test_login()

    @BeautifulReport.add_test_img('test_02_mptree')  # 失败后会有报告截图
    def test_02_mptree(self):
        """
        用户登录点击积分商城
        :return:
        """
        mplogin = mplogin_test(self.driver)
        login_drivers = mplogin.test_login()
        mptree = test_mptree(login_drivers)
        mptree.get_link_points_shopping()
    '''

    # @BeautifulReport.add_test_img('test_03_ncmslogin')  # 失败后会有报告截图
    # def test_03_ncmslogin(self):
    #     """
    #           用户登录新运营后台
    #     """
    #     mplogin =Test_NCLogin(self.driver)
    #     mplogin.test_login()

    @BeautifulReport.add_test_img('test_04_ncmslogin')  # 失败后会有报告截图
    def test_04_ncmsTransferAudit(self):
        """
              银行转账审核
        """
        mplogin = Test_NCLogin(self.driver)
        login_driver=mplogin.test_login()
        test_NCTransferAudit(login_driver).operation()
        # test_NCTransferAudit(login_driver).mouse_op()
        # test_NCTransferAudit(login_driver).execute_script("document.querySelector('.bscroll-indicator').scrollTop=10000")
        time.sleep(3)
        print("拖动滚动条成功")
        test_NCTransferAudit(login_driver).get_parent_transfer_audit()
        # test_NCTransferAudit(login_driver).get_child_transfer_audit()





if __name__=='__main__':
    unittest.main()
