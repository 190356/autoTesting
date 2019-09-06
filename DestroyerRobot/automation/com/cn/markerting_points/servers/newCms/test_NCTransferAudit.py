from DestroyerRobot.automation.com.cn.markerting_points.servers.MPTree.test_mptree import test_mptree
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.com.cn.markerting_points.servers.newCms.NCTransferAudit import NCTransferAudit
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPTree.MPTree import MPTree
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
import traceback
import time

class test_NCTransferAudit:
    def __init__(self,driver):
        """
        实现数据后，定位页面信息操作
        登录页面，操作数据
        """
        self.driver = driver

    # test_mptree(self.driver).rootChildConfigPath()
    def rootChildConfigPath(self):
        # 从主配置文件中获取子配置文件路径
        conf2 = Config("ConfigKIDs")
        # 获取子文件路径
        confFile = conf2.get_configPath("markerting_points_configs")
        return confFile

    def childConfigXML(self, Pageskeyword, UIElementkeyword):
        confFile = self.rootChildConfigPath()
        config2 = Config("XMLFilePath", confFile)
        filepath = config2.get_path_config("ncmsTree")
        filepath = SystemOs().sys_path(filepath)
        xmlspath = XmlUtil(filepath)
        # 获取XML中相关信息
        xmls = xmlspath.xml_parsing(Pageskeyword, UIElementkeyword)
        return xmls

    # test_mptree().childConfigImgPath()
    def childConfigImgPath(self):
        """
        获取图片路径，并新建以日期为基础的文件目录名 例如： img/2019-01-01/
        :return:
        """
        confFile = self.rootChildConfigPath()
        config3 = Config("ImgPath",confFile)
        img_path = config3.get_path_config("error_img")
        data_path = TestDateTime().local_day()
        img_path = SystemOs().sys_path(img_path,data_path)
        SystemOs().mkdirs_file(img_path)
        return img_path

    def operation(self):
        # js2 = "var q=document.documentElement.scrollTop=10000"
        js2="document.getElementsByClassName('el-menu-vertical-demo el-menu')[0].style='transition-timing-function: cubic-bezier(0.23, 1, 0.32, 1); transition-duration: 0ms; transform: translate(0px, -775px) scale(1) translateZ(0px);'"
        #js2="document.getElementsByClassName('bscroll-indicator')[0].style.top='1000px'"
        print(type(js2))
        NCTransferAudit(self.driver).opera(js2)

    # def search(self):
    #     bys_pAudit2, values_pAudit2 = self.childConfigXML("银行转账菜单", "审核状态")
    #     bys_pAudit3, values_pAudit3 = self.childConfigXML("银行转账菜单", "未审核")
    #     bys_pAudit4, values_pAudit4 = self.childConfigXML("银行转账菜单", "查询")
    #     bys_pAudit6, values_pAudit6 = self.childConfigXML("银行转账菜单", "审核按钮")
    #     mptree = NCTransferAudit(self.driver)
    #     try:
    #         mptree.get_elements(bys_pAudit2, values_pAudit2)
    #         mptree.points_managers(bys_pAudit3, values_pAudit3)
    #         mptree.points_managers(bys_pAudit4, values_pAudit4)
    #         mptree.audit(bys_pAudit6, values_pAudit6)
    #         mpdriver = mptree.page.get_driver()
    #         return mpdriver
    #     except Exception:
    #         img_path = self.childConfigImgPath()
    #         mptree.page.save_img(img_path, str(int(TestDateTime().time_stamp())))
    #         print(traceback.format_exc())

    def get_parent_transfer_audit(self):
        """
        父节点银行转账审核
        :return:
        """
        # 获取XML中相关信息
        bys_pAudit, values_pAudit = self.childConfigXML("银行转账菜单", "父节点银行转账审核")
        bys_pAudit1, values_pAudit1 = self.childConfigXML("银行转账菜单", "子节点银行转账审核")
        bys_pAudit2, values_pAudit2 = self.childConfigXML("银行转账菜单", "审核状态")
        bys_pAudit3, values_pAudit3 = self.childConfigXML("银行转账菜单", "未审核")

        bys_pAudit4, values_pAudit4 = self.childConfigXML("银行转账菜单", "查询")
        bys_pAudit5, values_pAudit5 = self.childConfigXML("银行转账菜单", "获取数据总条数")
        bys_pAudit6, values_pAudit6 = self.childConfigXML("银行转账菜单", "审核按钮")
        bys_pAudit7, values_pAudit7 = self.childConfigXML("银行转账菜单", "上传图片按钮")

        mptree = NCTransferAudit(self.driver)
        # nc=test_NCTransferAudit(self.driver)
        try:
            # mptree.points_shopping(bys_pAudit, values_pAudit)
            mptree.points_managers(bys_pAudit, values_pAudit)
            mptree.points_managers(bys_pAudit1, values_pAudit1)
            test_NCTransferAudit(self.driver).search()
            time.sleep(3)
            mptree.get_elements(bys_pAudit2, values_pAudit2)

            mptree.points_managers(bys_pAudit3, values_pAudit3)
            mptree.points_managers(bys_pAudit4, values_pAudit4)
            mptree.points_managers(bys_pAudit5, values_pAudit5)
            mptree.audit( bys_pAudit6, values_pAudit6)

            mpdriver = mptree.page.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.page.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def uploadPic(self):
        bys_pAudit7, values_pAudit7 = self.childConfigXML("银行转账菜单", "上传图片按钮")

        mptree = NCTransferAudit(self.driver)
        try:
            mptree.points_managers(bys_pAudit7, values_pAudit7)
            mpdriver = mptree.page.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.page.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def auditPass(self):
        bys_pAudit8, values_pAudit8 = self.childConfigXML("银行转账菜单", "通过按钮")

        mptree = NCTransferAudit(self.driver)
        try:
            mptree.points_managers(bys_pAudit8, values_pAudit8)
            time.sleep(2)
            mpdriver = mptree.page.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.page.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    '''
    def get_child_transfer_audit(self):
        """
        子节点银行转账审核
        :return:
        """
        # 获取XML中相关信息
        bys_pAudit, values_pAudit = self.childConfigXML("银行转账菜单", "子节点银行转账审核")
        mptree = NCTransferAudit(self.driver)
        try:
            # mptree.points_shopping(bys_pAudit, values_pAudit)
            mptree.points_managers(bys_pAudit, values_pAudit)
            mpdriver = mptree.page.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.page.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    '''
