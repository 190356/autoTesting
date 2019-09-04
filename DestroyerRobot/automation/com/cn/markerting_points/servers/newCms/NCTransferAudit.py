from DestroyerRobot.automation.com.cn.base.BasePage import BasePage
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPTree.MPTree import MPTree
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
import traceback
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


