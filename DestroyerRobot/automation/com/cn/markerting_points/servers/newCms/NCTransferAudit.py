from DestroyerRobot.automation.com.cn.base.BasePage import BasePage
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPTree.MPTree import MPTree
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
import traceback
import os
import time
# from DestroyerRobot.automation.com.cn.markerting_points.servers.newCms.test_NCTransferAudit import test_NCTransferAudit
# from DestroyerRobot.automation.com.cn.markerting_points.servers.newCms.test_NCTransferAudit import test_NCTransferAudit
from DestroyerRobot.automation.com.cn.markerting_points.servers.newCms import test_NCTransferAudit

class NCTransferAudit:
    def __init__(self,driver):
        self.page = BasePage(driver)

    # def oper(self,bys,values):
    #     MPTree(self.page).points_managers(bys,values)
    def points_managers(self,bys,values):
        """
        积分管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.page.getElementByElement(bys,values)
        self.page.click(ele)

    def get_elements(self,bys,values):
        ele = self.page.getElementByElements(bys, values)
        self.page.sendkeys(ele[2],"366858096589")
        time.sleep(2)
        self.page.click(ele[7])

    def opera(self,js1):
        self.page.get_js(js1)
        self.page.implicitly_wait()

    # def audit(self,bys,values):
    #     ele = self.page.getElementByElements(bys, values)
    #     for i in range(len(ele)):
    #         self.page.click(ele[i])
    #
    #         test_NCTransferAudit(self.driver).uploadPic()
    #         print("hjj")
    #         os.system(os.getcwd()+"\\autoit\\auditUploadPic.exe")
    #         test_NCTransferAudit(self.driver).auditPass()
    #         test_NCTransferAudit(self.driver).search()
    #         # self.page.refresh()
    def audit(self,bys,values):
        # ele = self.page.getElementByElements(bys, values)
        # for i in range(len(ele)):
        #     self.page.click(ele[i])

        test_NCTransferAudit(self.driver).uploadPic()
        print("hjj")
        os.system(os.getcwd()+"\\autoit\\auditUploadPic.exe")
        test_NCTransferAudit(self.driver).auditPass()
        test_NCTransferAudit(self.driver).search()
        # self.page.refresh()
