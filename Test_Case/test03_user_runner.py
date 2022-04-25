'''
用户管理功能测试分为以下几种情况:
(1)点击系统设置下的用户管理,查看能否正常进入用户管理界面
(2)点击用户管理中添加用户按钮,查看能否正常加载添加用户弹窗
(3)在添加用户弹窗中全部输入栏为空,直接点击保存,查看是否提示用户名不能为空
(4)在添加用户弹窗中输入登录名,其他为空,查看是否提示登录密码不能为空
(5)在添加用户弹窗中输入登录名和登录密码,其他为空,查看是否提示两次密码不一样
(6)在添加用户弹窗中输入登录名,登录密码和确认密码输入不一致,其他为空,查看是否提示两次密码不一样
(7)在添加用户弹窗中输入登录名、登录密码和确认密码,其他为空,查看是否提示请输入姓名
(8)在添加用户弹窗中输入登录名、登录密码、确认密码、真实姓名,其他为空,查看是否提示请选择所在部门
(9)在添加用户弹窗中输入登录名、登录密码、确认密码、真实姓名、所在部门,其他为空,查看是否提示请选择用户角色
(10)在添加用户弹窗中输入登录名、登录密码、确认密码、真实姓名、所在部门、用户角色,其他为空,查看是否提示请输入手机号
(11)在添加用户弹窗中输入登录名、登录密码、确认密码、真实姓名、选择所在部门、选择用户角色、输入手机号,查看是否提示添加成功
(12)点击用户列表中某一行用户对应的编辑按钮,查看是否弹出编辑弹窗
(13)在编辑用户弹窗中修改用户真实姓名,查看是否修改成功
(14)在编辑用户弹窗中修改用户所在部门,查看是否修改成功
(15)在编辑用户弹窗中修改用户角色,查看是否修改成功
(16)在编辑用户弹窗中修改手机号,查看是否修改成功
(17)在用户管理搜索框中输入关键字查看是否完成筛选
(18)点击用户列表某一用户对应删除按钮,查看能否完成删除
'''

from lib2to3.pgen2 import driver
import unittest
from xml.dom.minidom import Document
from selenium import webdriver
from time import sleep
import sys
import time
from selenium.webdriver import ActionChains
from selenium import webdriver                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from BeautifulReport import BeautifulReport
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as Expect

class test03_UserCase(unittest.TestCase):
    """
    def setUp(self):
        self.dr = webdriver.Edge()

    def tearDown(self):
       self.dr.quit()

    """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('测试完成')

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass
      
#定义截图方法
    def save_img(self, img_name):  
        """
         传入一个img_name, 并存储到默认的文件路径下img
         :param img_name:
          :return:
         """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('./用户管理/img'), img_name))    #os.path.abspath('')截图存放路径
#打开浏览器至用户管理
    def User_management(self,username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        sleep(1)
        self.driver.find_element_by_id('input_username').send_keys(username)  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys(password)  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        sleep(3)
          #  #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        self.driver.find_element_by_link_text('系统设置').click()   #点击系统设置按钮
        sleep(2)
        self.driver.find_element_by_link_text('用户管理').click()   #点击用户管理按钮
        sleep(2)   

    def login(self, username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #登录页面
        sleep(2)
        self.driver.find_element_by_id('input_username').send_keys(username)  #定义用户名
        self.driver.find_element_by_id('input_password').send_keys(password)   #定义密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        sleep(1)

       
#用例1:点击系统设置下的用户管理,查看能否正常进入用户管理界面
    @BeautifulReport.add_test_img('用户管理界面')
    def test_01_page_user(self):
        '''点击系统设置下的用户管理,查看能否正常进入用户管理界面'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        #断言是否进入用户管理界面
        link1=self.driver.find_element_by_css_selector('#user_table thead th:nth-child(2)')   #定位用户列表表头
        self.assertIn('用户名',link1.text)
        self.add_img()
        self.save_img('用户管理主界面')
        sleep(1)

#用例2：点击用户管理中添加用户按钮,查看能否正常加载添加用户弹窗
    @BeautifulReport.add_test_img('添加用户弹窗')
    def test_02_add_user_popup(self):
        '''点击用户管理中添加用户按钮,查看能否正常加载添加用户弹窗'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_id('btn_user_add').click()   #点击添加用户弹窗
        self.driver.implicitly_wait(2)   #隐式等待2秒  
        #断言是否成功加载处添加用户弹窗
        sleep(2)
        link1=self.driver.find_element_by_css_selector('#modal_user_edit h5')  #定位添加用户弹窗
        self.assertIn('添加用户',link1.text)
        self.add_img()
        self.save_img('添加用户弹窗')
        sleep(1)

#用例3:在添加用户弹窗中全部输入栏为空,直接点击保存,查看是否提示用户名不能为空
    @BeautifulReport.add_test_img('添加用户信息为空')
    def test_03_popup_null(self):
        '''在添加用户弹窗中全部输入栏为空,直接点击保存,查看是否提示用户名不能为空'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_id('btn_user_add').click()   #点击添加用户弹窗
        self.driver.implicitly_wait(2)   #隐式等待2秒
        self.add_img()
        self.driver.find_element_by_id('btn_user_save').click()    #全部输入栏为空，点击保存按钮
        #断言是否提示用户名不能为空
        self.driver.implicitly_wait(2)   #隐式等待2秒
        link1=self.driver.find_element_by_id('alter_notify')   #定位提示弹框
        self.assertIn('请输入用户名',link1.text)
        self.add_img()
        self.save_img('请输入用户名')
        sleep(1)

#用例4:在添加用户弹窗中输入登录名,其他为空,查看是否提示登录密码不能为空
    @BeautifulReport.add_test_img('已输入用户名')
    def test_04_input_user_userName(self):
        '''在添加用户弹窗中输入登录名,其他为空,查看是否提示登录密码不能为空'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_id('btn_user_add').click()   #点击添加用户弹窗
        self.driver.implicitly_wait(2)   #隐式等待2秒
        el=self.driver.find_element_by_id('input_user_userName')
        el.click()
        sleep(1)
        el.send_keys('测试用户123')   #输入用户名
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_user_save').click()    #点击保存按钮
        sleep(1)
        #断言是否提示登录密码不能为空
        self.driver.implicitly_wait(2)   #隐式等待2秒
        link1=self.driver.find_element_by_id('alter_notify')   #定位提示弹框
        self.assertIn('请输入密码',link1.text)
        self.add_img()
        self.save_img('提示请输入密码')
        sleep(1)

#用例5:在添加用户弹窗中输入登录名和登录密码,其他为空,查看是否提示两次密码不一样
    @BeautifulReport.add_test_img('已输入登录密码')
    def test_05_input_user_password(self):
        '''在添加用户弹窗中输入登录名和登录密码,其他为空,查看是否提示两次密码不一样'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_id('btn_user_add').click()   #点击添加用户弹窗
        self.driver.implicitly_wait(2)   #隐式等待2秒
        el=self.driver.find_element_by_id('input_user_userName')
        el.click()
        sleep(1)
        el.clear()
        sleep(2)
        el.send_keys('测试用户123')   #输入用户名
        sleep(1)
        self.driver.find_element_by_id('input_user_password').send_keys('123456')   #输入登录密码
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_user_save').click()    #点击保存按钮
        sleep(1)
        #断言是否提示两次密码不一样
        self.driver.implicitly_wait(2)   #隐式等待2秒
        link1=self.driver.find_element_by_id('alter_notify')   #定位提示弹框
        self.assertIn('两次输入的密码不一致',link1.text)
        self.add_img()
        self.save_img('确认密码为空')
        sleep(1)

#用例6:在添加用户弹窗中输入登录名,登录密码和确认密码输入不一致,其他为空,查看是否提示两次密码不一样
    @BeautifulReport.add_test_img('输入错误确认密码')
    def test_06_input_user_repassword_error(self):
        '''在添加用户弹窗中输入登录名和登录密码,其他为空,查看是否提示两次密码不一样'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_id('btn_user_add').click()   #点击添加用户弹窗
          #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_user_form'))) 
        self.driver.implicitly_wait(2)   #隐式等待2秒
        a=self.driver.find_element_by_id('input_user_form')
        ActionChains(self.driver).move_to_element(a).pause(3).perform()#鼠标悬停在添加用户处
        el=self.driver.find_element_by_id('input_user_userName')
        el.click()
        el.clear()
        sleep(1)
        el.send_keys('测试用户123')   #输入用户名
        sleep(1)
        self.driver.find_element_by_id('input_user_password').send_keys('123456')   #输入登录密码
        sleep(1)
        self.driver.find_element_by_id('input_user_repassword').send_keys('123')    #在确认密码框内输入与登录密码不一致的密码
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_user_save').click()    #点击保存按钮
        sleep(1)
        #断言是否提示两次密码不一样
        self.driver.implicitly_wait(2)   #隐式等待2秒
        link1=self.driver.find_element_by_id('alter_notify')   #定位提示弹框
        self.assertIn('两次输入的密码不一致',link1.text)
        self.add_img()
        self.save_img('提示密码不一致')
        sleep(1)

#用例7:在添加用户弹窗中输入登录名、登录密码和确认密码,其他为空,查看是否提示请输入姓名
    @BeautifulReport.add_test_img('输入正确确认密码')
    def test_07_input_user_repassword_correct(self):
        '''在添加用户弹窗中输入登录名、登录密码和确认密码,其他为空,查看是否提示请输入姓名'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_id('btn_user_add').click()   #点击添加用户弹窗
        self.driver.implicitly_wait(2)   #隐式等待2秒
        el=self.driver.find_element_by_id('input_user_userName')
        el.click()
        sleep(2)
        el.send_keys('测试用户123')   #输入用户名
        sleep(1)
        self.driver.find_element_by_id('input_user_password').send_keys('123456')   #输入登录密码
        sleep(1)
        self.driver.find_element_by_id('input_user_repassword').send_keys('123456')    #在确认密码框内输入与登录密码一致的密码
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_user_save').click()    #点击保存按钮
        sleep(1)
        #断言是否提示请输入姓名
        self.driver.implicitly_wait(2)   #隐式等待2秒
        link1=self.driver.find_element_by_id('alter_notify')   #定位提示弹框
        self.assertIn('请输入姓名',link1.text)
        self.add_img()
        self.save_img('提示输入姓名')
        sleep(1)

#用例8:在添加用户弹窗中输入登录名、登录密码、确认密码、真实姓名、其他为空,查看是否提示请选择所在部门
    @BeautifulReport.add_test_img('输入真实姓名')
    def test_08_input_user_realName(self):
        '''在添加用户弹窗中输入登录名、登录密码、确认密码、真实姓名、其他为空,查看是否提示请选择所在部门'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_id('btn_user_add').click()   #点击添加用户弹窗
        self.driver.implicitly_wait(2)   #隐式等待2秒
        el=self.driver.find_element_by_id('input_user_userName')
        el.click()
        sleep(2)
        el.send_keys('测试用户123')   #输入用户名
        sleep(1)
        self.driver.find_element_by_id('input_user_password').send_keys('123456')   #输入登录密码
        sleep(1)
        self.driver.find_element_by_id('input_user_repassword').send_keys('123456')    #在确认密码框内输入与登录密码一致的密码
        sleep(1)
        self.driver.find_element_by_id('input_user_realName').send_keys('测试用户真实姓名')   #输入真实姓名
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_user_save').click()    #点击保存按钮 
        sleep(1)
        #断言是否提示请选择所在部门
        self.driver.implicitly_wait(2)   #隐式等待2秒
        link1=self.driver.find_element_by_id('alter_notify')   #定位提示弹框
        self.assertIn('请选择部门',link1.text)
        self.add_img()
        self.save_img('提示选择部门')
        sleep(1)

#用例9:在添加用户弹窗中输入登录名、登录密码、确认密码、真实姓名、选择所在部门,其他为空,查看是否提示请选择角色
    @BeautifulReport.add_test_img('选择所在部门')
    def test_09_input_user_department(self):
        '''在添加用户弹窗中输入登录名、登录密码、确认密码、真实姓名、选择所在部门,其他为空,查看是否提示请选择角色'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_id('btn_user_add').click()   #点击添加用户弹窗
        self.driver.implicitly_wait(2)   #隐式等待2秒
        el=self.driver.find_element_by_id('input_user_userName')
        el.click()
        sleep(2)
        el.send_keys('测试用户123')   #输入用户名
        sleep(1)
        self.driver.find_element_by_id('input_user_password').send_keys('123456')   #输入登录密码
        sleep(1)
        self.driver.find_element_by_id('input_user_repassword').send_keys('123456')    #在确认密码框内输入与登录密码一致的密码
        sleep(1)
        self.driver.find_element_by_id('input_user_realName').send_keys('测试用户真实姓名')   #输入真实姓名
        sleep(3)
        self.driver.find_element_by_css_selector('#input_user_form  div:nth-child(5) div:first-child ').click()   #点击所在部门选择框
        sleep(1)
        a=self.driver.find_element_by_css_selector('.modal-open div.cascader-dropdown-container ul:first-child')
        ActionChains(self.driver).move_to_element(a).pause(3).perform()#鼠标悬停在第一大部门处
        sleep(1)
        self.driver.find_element_by_css_selector('.modal-open div.cascader-dropdown-container ul:first-child li').click()#点击第一大部门的第一小组
        sleep(2)
        self.add_img()
        self.driver.find_element_by_id('btn_user_save').click()    #点击保存按钮 
        sleep(1)
        #断言是否提示请选择角色
        self.driver.implicitly_wait(2)   #隐式等待2秒
        link1=self.driver.find_element_by_id('alter_notify')   #定位提示弹框
        self.assertIn('请选择角色',link1.text)
        self.add_img()
        self.save_img('提示选择角色')
        sleep(1)

#用例10：添加用户弹窗中输入登录名、登录密码、确认密码、真实姓名、所在部门、用户角色,其他为空,查看是否提示请输入手机号
    @BeautifulReport.add_test_img('选择角色')
    def test_10_input_user_role(self):
        '''添加用户弹窗中输入登录名、登录密码、确认密码、真实姓名、所在部门、用户角色,其他为空,查看是否提示请输入手机号'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_id('btn_user_add').click()   #点击添加用户弹窗
        self.driver.implicitly_wait(2)   #隐式等待2秒
        el=self.driver.find_element_by_id('input_user_userName')
        el.click()
        sleep(2)
        el.send_keys('测试用户123')   #输入用户名
        sleep(1)
        self.driver.find_element_by_id('input_user_password').send_keys('123456')   #输入登录密码
        sleep(1)
        self.driver.find_element_by_id('input_user_repassword').send_keys('123456')    #在确认密码框内输入与登录密码一致的密码
        sleep(1)
        self.driver.find_element_by_id('input_user_realName').send_keys('测试用户真实姓名')   #输入真实姓名
        sleep(3)
        self.driver.find_element_by_css_selector('#input_user_form  div:nth-child(5) div:first-child ').click()   #点击所在部门选择框
        sleep(1)
        a=self.driver.find_element_by_css_selector('.modal-open div.cascader-dropdown-container ul:first-child')
        ActionChains(self.driver).move_to_element(a).pause(3).perform()#鼠标悬停在第一大部门处
        sleep(1)
        self.driver.find_element_by_css_selector('.modal-open div.cascader-dropdown-container ul:first-child li').click()#点击第一大部门的第一小组
        sleep(2)
        self.driver.find_element_by_id('select_user_role').click()  #点击角色输入框
        self.driver.find_element_by_css_selector('#select_user_role option:first-child').click() #选择角色列表中的第一个角色
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_user_save').click()    #点击保存按钮 
        sleep(1)
        #断言是否提示用户名不能为空
        self.driver.implicitly_wait(2)   #隐式等待2秒
        link1=self.driver.find_element_by_id('alter_notify')   #定位提示弹框
        self.assertIn('请输入手机号',link1.text)
        self.add_img()
        self.save_img('提示输入手机号')
        sleep(1)
     
#用例11：在添加用户弹窗中输入登录名、登录密码、确认密码、真实姓名、选择所在部门、选择用户角色、输入手机号,查看是否提示添加成功
    @BeautifulReport.add_test_img('输入手机号')
    def test_11_input_user_phone(self):
        '''在添加用户弹窗中输入登录名、登录密码、确认密码、真实姓名、选择所在部门、选择用户角色、输入手机号,查看是否提示添加成功'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_id('btn_user_add').click()   #点击添加用户弹窗
        self.driver.implicitly_wait(2)   #隐式等待2秒
        el=self.driver.find_element_by_id('input_user_userName')
        el.click()
        sleep(2)
        el.send_keys('测试用户123')   #输入用户名
        sleep(1)
        self.driver.find_element_by_id('input_user_password').send_keys('123456')   #输入登录密码
        sleep(1)
        self.driver.find_element_by_id('input_user_repassword').send_keys('123456')    #在确认密码框内输入与登录密码一致的密码
        sleep(1)
        self.driver.find_element_by_id('input_user_realName').send_keys('测试用户真实姓名')   #输入真实姓名
        sleep(3)
        self.driver.find_element_by_css_selector('#input_user_form  div:nth-child(5) div:first-child ').click()   #点击所在部门选择框
        sleep(1)
        a=self.driver.find_element_by_css_selector('.modal-open div.cascader-dropdown-container ul:first-child')
        ActionChains(self.driver).move_to_element(a).pause(3).perform()#鼠标悬停在第一大部门处
        sleep(1)
        self.driver.find_element_by_css_selector('.modal-open div.cascader-dropdown-container ul:first-child li').click()#点击第一大部门的第一小组
        sleep(2)
        self.driver.find_element_by_id('select_user_role').click()  #点击角色输入框
        self.driver.find_element_by_css_selector('#select_user_role option:first-child').click() #选择角色列表中的第一个角色
        sleep(1)
        self.driver.find_element_by_id('input_user_phone').send_keys('13317201307')   #输入手机号
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_user_save').click()    #点击保存按钮 
        sleep(1)
        #断言是否提示用户名不能为空
        self.driver.implicitly_wait(2)   #隐式等待2秒
        link1=self.driver.find_element_by_id('alter_notify')   #定位提示弹框
        self.assertIn('添加成功',link1.text)
        self.add_img()
        self.save_img('添加成功')
        sleep(1)
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#验证能否使用新增的用户登录
        self.login('测试用户123','123456')    #进入登录界面
        #显示等待时间到进入系统主界面
        sleep(3) 
        link2 = self.driver.find_element_by_id('navbarNav')
        self.assertIn('菜单', link2.text)
        self.add_img()
        sleep(1)

#用例12：点击用户列表中某一行用户对应的编辑按钮,查看是否弹出编辑弹窗
    @BeautifulReport.add_test_img('编辑弹窗')
    def test_12_edit_popup(self):
        '''点击用户列表中某一行用户对应的编辑按钮,查看是否弹出编辑弹窗'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_css_selector('#user_table tbody tr:last-child  span a:first-child').click() #点击用户列表最后一列用户对应的编辑按钮
        sleep(2)
        self.driver.implicitly_wait(2)   #隐式等待2秒 
        link1=self.driver.find_element_by_css_selector('#modal_user_edit h5')
        self.assertIn('编辑用户',link1.text)
        self.add_img()
        self.save_img('用户信息编辑弹窗')

#用例13：在编辑用户弹窗中修改用户真实姓名,查看是否修改成功
    @BeautifulReport.add_test_img('修改真实姓名')
    def test_13_editor_realName(self):
        '''在编辑用户弹窗中修改用户真实姓名,查看是否修改成功'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_css_selector('#user_table tbody tr:last-child  span a:first-child').click() #点击用户列表最后一列用户对应的编辑按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒 
        el1=self.driver.find_element_by_id('input_user_realName')  #定位真实姓名输入框
        el1.click() #点击输入框
        sleep(1)
        el1.clear()#清除输入框
        sleep(1)
        el1.send_keys('修改后姓名') #在输入框中输入修改后的内容
        self.add_img()
        self.driver.find_element_by_id('btn_user_save').click()  #点击保存
        sleep(1)
        link1=self.driver.find_element_by_id('alter_notify') 
        self.assertIn('修改成功',link1.text)
        self.add_img()
        sleep(3)
        link2=self.driver.find_element_by_css_selector('#user_table tbody tr:last-child td:nth-child(3)')
        self.assertIn('修改后姓名',link2.text)
        self.add_img()
        self.save_img('修改真实姓名成功')

#用例14：在编辑用户弹窗中修改用户所在部门,查看是否修改成功
    @BeautifulReport.add_test_img('修改所在部门')
    def test_14_editor_department(self):
        '''在编辑用户弹窗中修改用户所在部门,查看是否修改成功'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_css_selector('#user_table tbody tr:last-child  span a:first-child').click() #点击用户列表最后一列用户对应的编辑按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒 
        self.driver.find_element_by_css_selector('#input_user_form div:nth-child(5) div div:first-child').click()  #点击所在部门这一行
        #鼠标悬停
        el=self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(1) li:nth-child(2)')
        ActionChains(self.driver).move_to_element(el).pause(3).perform()#鼠标悬停在第二大部门处
        sleep(1)
        self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(2) li ').click()#点击第二大部门的第一小组
        sleep(2)
        self.add_img()
        self.driver.find_element_by_id('btn_user_save').click()  #点击保存
        sleep(1)
        link1=self.driver.find_element_by_id('alter_notify')   #定位提示弹框
        self.assertIn('修改成功',link1.text)
        self.add_img()
        self.save_img('修改所在部门成功')
        sleep(1)

#用例15：在编辑用户弹窗中修改用户角色,查看是否修改成功
#暂定还未修改
    @BeautifulReport.add_test_img('修改用户角色')
    def test_15_editor_role(self):
        '''在编辑用户弹窗中修改用户角色,查看是否修改成功'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_css_selector('#user_table tbody tr:last-child  span a:first-child').click() #点击用户列表最后一列用户对应的编辑按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒 
        self.driver.find_element_by_id('select_user_role').click()  #点击用户角色这一行
        self.driver.find_element_by_css_selector('#select_user_role option:last-child').click()   #点击选择用户角色最后一行
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_user_save').click()  #点击保存
        sleep(1)
        link1=self.driver.find_element_by_id('alter_notify')   #定位提示弹框
        self.assertIn('修改成功',link1.text)
        self.add_img()
        self.save_img('修改用户角色成功')
        sleep(1)

#用例16：在编辑用户弹窗中修改手机号,查看是否修改成功
    @BeautifulReport.add_test_img('修改手机号')
    def test_16_editor_phone(self):
        '''在编辑用户弹窗中修改手机号,查看是否修改成功'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_css_selector('#user_table tbody tr:last-child  span a:first-child').click() #点击用户列表最后一列用户对应的编辑按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒
        el=self.driver.find_element_by_id('input_user_phone')  #定位手机号输入框
        el.click()
        sleep(1)
        el.clear()
        sleep(1)
        el.send_keys('133172043096')
        sleep(2)
        self.add_img()
        self.driver.find_element_by_id('btn_user_save').click()  #点击保存
        sleep(1)
          #显示等待时间到出现保存成功提醒
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('修改成功',link1.text)
        self.add_img()
        sleep(2)
        #断言判定列表中的手机号是否已修改成功
        link2=self.driver.find_element_by_css_selector('#user_table tbody tr:last-child td:nth-child(6)')   
        self.assertIn('133172043096',link2.text)
        self.add_img()
        self.save_img('修改手机号成功')
        sleep(2)

#用例17：在编辑用户弹窗中测试修改的真实姓名、手机号输入框为空，查看是否提示不能为空
#已验证成功
    @BeautifulReport.add_test_img('修改输入框为空')
    def test_17_editor_null(self):
        '''在编辑用户弹窗中测试修改的真实姓名、手机号输入框为空,查看是否提示不能为空'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_css_selector('#user_table tbody tr:last-child  span a:first-child').click() #点击用户列表最后一列用户对应的编辑按钮
        self.driver.implicitly_wait(2)   #隐式等待2
#修改真实姓名为空
        el1=self.driver.find_element_by_id('input_user_realName')  #定位真实姓名输入框
        el1.click() #点击输入框
        sleep(1)
        el1.clear()#清除输入框
        sleep(1)
        self.add_img()
        # el1.send_keys('修改后姓名') #在输入框中输入修改后的内容
        self.driver.find_element_by_id('btn_user_save').click()  #点击保存
        sleep(1)
        link1=self.driver.find_element_by_id('alter_notify')  #断言是否提示不能为空
        self.assertIn('The RealName field is required.',link1.text)
        self.add_img()
        self.save_img('编辑真实姓名不能为空')
        el1.send_keys('修改后姓名') #在输入框中输入修改后的内容
        sleep(1)
#修改手机号为空
        el2=self.driver.find_element_by_id('input_user_phone')  #定位手机号输入框
        el2.click()
        sleep(1)
        el2.clear()
        sleep(2)
        self.add_img()
        self.driver.find_element_by_id('btn_user_save').click()  #点击保存
        sleep(1)
        #断言判定是否提示手机号不能空
        link2=self.driver.find_element_by_id('alter_notify')
        self.assertIn('The Phone field is required.',link2.text)
        self.add_img()
        self.save_img('修改手机号不能为空')
        sleep(2)
        el2.send_keys('13317204309')
        sleep(1)
        self.driver.find_element_by_id('btn_user_save').click()  #点击保存
        sleep(1)
        link3=self.driver.find_element_by_id('alter_notify')   #定位提示弹框
        self.assertIn('修改成功',link3.text)
        self.add_img()
        sleep(2)



#用例18：在用户管理搜索框中输入用户名、姓名、手机号关键字查看是否完成筛选
    @BeautifulReport.add_test_img('搜索查询')
    def test_18_user_search(self):
        '''在用户管理搜索框中输入关键字查看是否完成筛选'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        el=self.driver.find_element_by_id('input_user_search')
        el.click()
#测试搜索用户名关键字
        el.send_keys('ad')
        self.driver.find_element_by_id('btn_user_search').click()#点击搜索按钮
        self.driver.implicitly_wait(2)  #隐式等待2秒
        #断言筛选后的第一列用户名是否包含刚刚输入的关键字
        link1=self.driver.find_element_by_css_selector('#user_table tbody tr:first-child td:nth-child(2)')  #定位筛选后的第一列用户名
        self.assertIn('ad',link1.text)
        self.add_img()
        self.save_img('搜索用户名关键字')
        sleep(1)
        el.clear()#清除搜索输入框
#测试搜索姓名关键字
        el.send_keys('修改')
        self.driver.find_element_by_id('btn_user_search').click()#点击搜索按钮
        self.driver.implicitly_wait(2)  #隐式等待2秒
        #断言筛选后的第一列姓名是否包含刚刚输入的关键字
        link1=self.driver.find_element_by_css_selector('#user_table tbody tr:first-child td:nth-child(3)')  #定位筛选后的第一列姓名
        self.assertIn('修改',link1.text)
        self.add_img()
        self.save_img('搜索姓名关键字')
        sleep(1)
        el.clear()#清除搜索输入框
#测试搜索手机号关键字
        el.send_keys('133')
        self.driver.find_element_by_id('btn_user_search').click()#点击搜索按钮
        self.driver.implicitly_wait(2)  #隐式等待2秒
        #断言筛选后的第一列用户名是否包含刚刚输入的关键字
        link1=self.driver.find_element_by_css_selector('#user_table tbody tr:first-child td:nth-child(6)')  #定位筛选后的第一列手机号
        self.assertIn('133',link1.text)
        self.add_img()
        self.save_img('搜索手机号关键字')
        sleep(1)
        el.clear()#清除搜索输入框
        self.driver.find_element_by_id('btn_user_search').click()#点击搜索按钮

#用例19：点击用户列表某一用户对应删除按钮,查看能否完成删除
    @BeautifulReport.add_test_img('删除用户')
    def test_19_delete_user(self):
        '''在用户管理搜索框中输入关键字查看是否完成筛选'''
        self.User_management('admin','admin123456')    #进入用户管理界面
        self.driver.find_element_by_css_selector('#user_table tbody tr:last-child  span a:last-child').click()   #点击用户列表最后一列的删除按钮
        sleep(2)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取删除确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认删除
        sleep(2)
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link1.text)
        self.add_img()
        self.save_img('删除用户成功') 
        sleep(2)
#退出登录验证是否删除成功
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#验证能否使用新增的用户登录
        self.login('测试用户123','123456')    #进入用户管理界面
          #显示等待时间到出现报错提醒
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        # self. Explicit_Waits(By.ID,'alter_notify')       #显示等待时间到出现报错提醒
        link2 = self.driver.find_element_by_id('alter_notify')
        self.assertEqual(link2.text,'用户名或密码不正确') 
        self.add_img()
        sleep(1)
 



if __name__ == '__main__':
    unittest.main(argv=['ignored','-v'],exit=False)
    print('')


