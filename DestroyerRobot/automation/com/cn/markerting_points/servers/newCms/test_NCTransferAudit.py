from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.com.cn.markerting_points.servers.newCms.NCTransferAudit import NCTransferAudit
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.com.cn.base.BasePage import BasePage
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
import traceback
import os
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

    # js操作滚动条
    def operation(self):
        js2="document.getElementsByClassName('el-menu-vertical-demo el-menu')[0].style='transition-timing-function: cubic-bezier(0.23, 1, 0.32, 1); transition-duration: 0ms; transform: translate(0px, -775px) scale(1) translateZ(0px);'"
        print(type(js2))
        NCTransferAudit(self.driver).opera(js2)

    def search(self):
        bys_pAudit2, values_pAudit2 = self.childConfigXML("银行转账菜单", "审核状态")
        bys_pAudit3, values_pAudit3 = self.childConfigXML("银行转账菜单", "未审核")
        bys_pAudit4, values_pAudit4 = self.childConfigXML("银行转账菜单", "查询")
        bys_pAudit5, values_pAudit5 = self.childConfigXML("银行转账菜单", "获取数据总条数")
        bys_pAudit6, values_pAudit6 = self.childConfigXML("银行转账菜单", "审核按钮")
        mptree = NCTransferAudit(self.driver)
        try:
            mptree.get_elements(bys_pAudit2, values_pAudit2)
            mptree.points_managers(bys_pAudit3, values_pAudit3)
            mptree.input_customer_name(bys_pAudit2, values_pAudit2)
            mptree.points_managers(bys_pAudit4, values_pAudit4)
            # test_NCTransferAudit(self.driver).audit(bys_pAudit6, values_pAudit6)
            global text
            text= BasePage(self.driver).getElementByElement(bys_pAudit5, values_pAudit5).text
            print("总条数是：", text)
            test_NCTransferAudit(self.driver).audit(bys_pAudit6, values_pAudit6)
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.page.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_parent_transfer_audit(self):
        """
        父节点银行转账审核
        :return:
        """
        # 获取XML中相关信息
        bys_pAudit, values_pAudit = self.childConfigXML("银行转账菜单", "父节点银行转账审核")
        bys_pAudit1, values_pAudit1 = self.childConfigXML("银行转账菜单", "子节点银行转账审核")
        mptree = NCTransferAudit(self.driver)
        try:
            mptree.points_managers(bys_pAudit, values_pAudit)
            mptree.points_managers(bys_pAudit1, values_pAudit1)
            test_NCTransferAudit(self.driver).search()
            time.sleep(3)

        except Exception:
            img_path = self.childConfigImgPath()
            mptree.page.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def uploadPic(self):
        bys_pAudit7, values_pAudit7 = self.childConfigXML("银行转账菜单", "上传图片按钮")

        mptree = NCTransferAudit(self.driver)
        try:
            mptree.points_managers(bys_pAudit7, values_pAudit7)
            time.sleep(2)
            os.system(SystemOs().sys_path() + "\\automation\\autoit\\auditUploadPic.exe")  #autoit上传图片

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
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.page.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def audit(self,bys,values):
        mptree = NCTransferAudit(self.driver)
        # bys_pAudit5, values_pAudit5 = self.childConfigXML("银行转账菜单", "获取数据总条数")
        try:
            ele = BasePage(self.driver).getElementByElements(bys, values)
            for i in range(len(ele)):
                BasePage(self.driver).click(ele[i])
                time.sleep(2)
                BasePage(self.driver).refresh()
                test_NCTransferAudit(self.driver).uploadPic()
                print("hjj")
                test_NCTransferAudit(self.driver).auditPass()
                time.sleep(3)
                test_NCTransferAudit(self.driver).search()
                time.sleep(3)
                if text=="共 0 条":
                    print("全部审核完成")
                    break
                else:
                    test_NCTransferAudit(self.driver).audit(bys,values)
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.page.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    #单条数据的审核
    # def audit(self,bys,values):
    #     # ele = self.page.getElementByElement(bys,values)
    #     ele = BasePage(self.driver).getElementByElement(bys,values)
    #     # for i in range(len(ele)):
    #     BasePage(self.driver).click(ele)




