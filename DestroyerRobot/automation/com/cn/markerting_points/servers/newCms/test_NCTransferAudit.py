from DestroyerRobot.automation.com.cn.markerting_points.servers.MPTree.test_mptree import test_mptree
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.com.cn.markerting_points.servers.newCms.NCTransferAudit import NCTransferAudit
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPTree.MPTree import MPTree
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
import traceback

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


    def get_parent_transfer_audit(self):
        """
        父节点银行转账审核
        :return:
        """
        # 获取XML中相关信息
        bys_pAudit, values_pAudit = self.childConfigXML("银行转账菜单", "父节点银行转账审核")
        mptree = NCTransferAudit(self.driver)
        try:
            # mptree.points_shopping(bys_pAudit, values_pAudit)
            mptree.oper(bys_pAudit, values_pAudit)
            mpdriver = mptree.page.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.page.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

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


