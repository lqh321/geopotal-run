'''
部门管理功能测试,分为以下几种情况:
(1)点击添加部门,系统自动弹出添加部门弹窗;
(2)在添加部门弹窗中全部输入为空,点击保存,界面提示“请输入部门名称”;
(3)在其他输入框中输入对应内容,部门名称输入为空,点击保存,界面提示“请输入部门名称”
(4)在部门名称中输入对应名称,输入父部门名称,输入联系人,输入不符合联系方式的手机号,点击保存,界面提示“请输入正确手机号”
(5)在部门名称、父部门、联系人、联系方式输入对应内容,点击保存,界面提示“添加成功!”
(6)在添加部门界面,输入正确的部门名称、联系人、手机号,父部门选择刚刚新增的部门名称,点击保存,界面提示“添加成功!”
(7)在部门列表中选择新增的部门,点击删除按钮,界面弹出“确认是否删除”,选择否,界面关闭
(8)在部门列表中选择新增的部门,点击删除按钮,界面弹出“确认是否删除”,选择是,界面提示“删除成功”
'''

import unittest
from selenium import webdriver
from time import sleep
import sys
from HTMLTestRunner import HTMLTestRunner
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


class test05_DepartmentCase(unittest.TestCase):
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
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('./部门管理/img'), img_name))    #os.path.abspath('')截图存放路径
#封装的显示等待时间
    def Explicit_Waits(driver,way,path):
 
        try:
              ele = WebDriverWait(driver,40).until(EC.presence_of_element_located((way,path)))
              return ele
        
        except Exception as e:
              print('元素寻找失败: '+str(e))
#打开浏览器至添加部门弹窗
    def Popup(self,username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys(username)  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys(password)  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        sleep(3)
        #显示时间等待菜单列表加载完
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        self.driver.find_element_by_link_text('系统设置').click()   #点击系统设置按钮
        sleep(2)
        self.driver.find_element_by_link_text('部门管理').click()   #点击部门管理按钮
        sleep(2)  
       #显示时间等待进入部门管理界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_department_add'))) 
        sleep(1)
        self.driver.find_element_by_id('btn_department_add').click()   #点击添加部门按钮
        sleep(2) 


#用例1： 点击添加部门,系统自动弹出添加部门弹窗;
#已验证成功
    @BeautifulReport.add_test_img('添加部门弹窗')  
    def test_01_Popup_window(self):
        '''点击添加部门,系统自动弹出添加部门弹窗;'''
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys('admin')  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys('admin123456')  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        sleep(2)
        self.driver.find_element_by_link_text('系统设置').click()   #点击系统设置按钮
        sleep(2)
        self.driver.find_element_by_link_text('部门管理').click()   #点击部门管理按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒   
        self.driver.find_element_by_id('btn_department_add').click()   #点击添加部门按钮
        sleep(2) 
        link1 = self.driver.find_element_by_id('input_department_form')
        self.assertIn('部门名称', link1.text)
        sleep(1)
        self.add_img()
        self.save_img('添加部门弹窗')
       

#用例2：在添加部门弹窗中全部输入为空,点击保存,界面提示“请输入部门名称”;
#已验证成功
    @BeautifulReport.add_test_img('输入为空1') 
    def test_02_all_null(self):
        '''输入框为空,提示请输入部门名称'''
        self.Popup('admin','admin123456')    #进入添加部门弹窗
        self.driver.find_element_by_id('btn_department_save').click()    #点击弹窗中的保存按钮
        link2=self.driver.find_element_by_id('alter_notify')
        self.assertIn('请输入部门名称', link2.text)
        self.add_img()
        self.save_img('输入为空') 
        sleep(1)

#用例3：在其他输入框中输入对应内容,部门名称输入为空,点击保存,界面提示“请输入部门名称”
#已验证成功
    @BeautifulReport.add_test_img('输入为空2') 
    def test_03_name_null(self):
        '''部门名称为空,提示请输入部门名称'''
        self.Popup('admin','admin123456')    #进入添加部门弹窗
        self.driver.find_element_by_xpath('//*[@id="input_department_form"]/div[2]/div/div/div/input').send_keys('父部门——测试')    #在父部门输入框输入
        self.driver.find_element_by_id('input_department_contact').send_keys('测试人员')        #在联系人输入框输入
        self.driver.find_element_by_id('input_department_tel').send_keys('13317291307')        #在联系方式输入框中输入
        self.add_img()
        self.driver.find_element_by_id('btn_department_save').click()                          #点击弹窗中的保存按钮
        sleep(1)
        link3=self.driver.find_element_by_id('alter_notify')
        self.assertIn('请输入部门名称', link3.text)
        self.add_img()
        self.save_img('输入为空2') 
        sleep(1)

#用例4：在部门名称中输入对应名称,输入父部门名称,输入联系人,输入不符合联系方式的手机号,点击保存,界面提示“请输入正确手机号”
#待验证
    # @BeautifulReport.add_test_img('输入正确手机号') 
    # def test_04_tel_error(self):
    #     '''用例4:输入不符合联系方式的手机号,提示请输入正确手机号'''
    #     self.Popup('admin','admin123456')    #进入添加部门弹窗
    #     self.driver.find_element_by_id('input_department_name').send_keys('测试部门名称')      #在部门名称中输入
    #     self.driver.find_element_by_class_name('cascader-wrapper').send_keys('父部门——测试')   #在父部门输入框输入
    #     self.driver.find_element_by_id('input_department_contact').send_keys('测试人员')       #在联系人输入框输入
    #     self.driver.find_element_by_id('input_department_tel').send_keys('1331')       #在联系方式输入框中输入不符合格式的手机号
    #     self.driver.find_element_by_id('btn_department_save').click()                          #点击弹窗中的保存按钮
    #     link4=self.driver.find_element_by_id('alter_notify')
    #     self.assertIn('请输入正确手机号', link4.text)
    # self.add_img()
    #     self.save_img('输入正确手机号') 
    #   # self.driver.get_screenshot_as_file("C:/Users/ZAssitant/Desktop/Geoportal/部门管理/success_img/输入正确手机号.png")  #截图可自定义截图后的保存位置和图片命名
    #     sleep(2)

#用例5：在部门名称、父部门、联系人、联系方式输入对应内容,点击保存,界面提示“添加成功!”
#已验证成功
    @BeautifulReport.add_test_img('添加成功1') 
    def test_05_sucess(self):
        '''在部门名称、父部门、联系人、联系方式输入对应内容'''
        self.Popup('admin','admin123456')    #进入添加部门弹窗
        self.driver.find_element_by_id('input_department_name').send_keys('测试部门名称8')      #在部门名称中输入'测试部门名称4'
        self.driver.find_element_by_class_name('cascader-wrapper').click()  #点击父部门输入框
        self.driver.find_element_by_css_selector('#input_department_form div:nth-child(2) div div div input').send_keys('测试父部门6')    #在父部门输入框输入
        self.driver.find_element_by_id('input_department_contact').send_keys('测试人员4')       #在联系人输入框输入
        self.driver.find_element_by_id('input_department_tel').send_keys('13317201307')       #在联系方式输入框中输入符合格式的手机号
        self.add_img()
        self.driver.find_element_by_id('btn_department_save').click()                          #点击弹窗中的保存按钮
        sleep(1)
        link5=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功', link5.text)
        self.add_img()
        self.save_img('添加部门成功') 
#验证部门列表最后一列是否为新增的部门
        link1=self.driver.find_element_by_css_selector('#table_department tbody tr:last-child td:nth-child(1)')
        self.assertIn('测试部门名称8',link1.text)
# #回到用户管理中的添加用户界面查看所在部门可选择列表中最后一列是否为刚刚新增的部门名称
#         self.driver.refresh()   #刷新页面
#         sleep(1)
#         self.driver.find_element_by_link_text('系统设置').click()   #点击系统设置按钮
#         self.driver.find_element_by_link_text('用户管理').click()   #点击用户管理按钮
#         sleep(1)
#         self.driver.find_element_by_id('btn_user_add').click()           #点击添加用户
#         sleep(1)
#         # # self.driver.find_element_by_class_name('cascader-wrapper').click()    #点击添加用户弹窗中的所在部门输入框
#         # # self.save_img('添加所在部门')
#         # sleep(1)
#         self.driver.find_element_by_css_selector('#input_user_form  div:nth-child(5) div:first-child ').click()   #点击所在部门选择框
#         sleep(1)
#         a=self.driver.find_element_by_css_selector('.modal-open div.cascader-dropdown-container ul:first-child')
#         ActionChains(self.driver).move_to_element(a).pause(3).perform()#鼠标悬停在第一大部门处
#         self.driver.find_element_by_css_selector('.modal-open div.cascader-dropdown-container ul:first-child li:last-child').click()
#         # sleep(1)
#         # self.driver.find_element_by_css_selector('.modal-open div:nth-child(18) ul:nth-child(1) li:last-child').click()   #在所在部门输入框中选择最后一栏，即为刚刚新增的部门名称
#         link2=self.driver.find_element_by_css_selector('#input_user_form  div:nth-child(5) div:first-child ')
#         self.assertIn('测试部门名称8',link2.text)
        self.add_img()
        self.save_img('添加所在部门选择成功')
        sleep(2)


#用例6:在添加部门界面,输入正确的部门名称、联系人、手机号,父部门选择刚刚新增的部门名称,点击保存,界面提示“添加成功!”
#已验证成功
    @BeautifulReport.add_test_img('添加成功2') 
    def test_06_select_department(self):
        '''在添加部门界面,输入正确的部门名称、联系人、手机号,父部门选择刚刚新增的部门名称'''
        self.Popup('admin','admin123456')    #进入添加部门弹窗
        self.driver.find_element_by_id('input_department_name').send_keys('自动化测试部门名称4')      #在部门名称中输入
        self.driver.find_element_by_class_name('cascader-wrapper').click()                    #在父部门中下拉刚刚新增成功的部门
        self.driver.find_element_by_css_selector('.cascader-menu li:last-child').click()      #在父部门选择框中选择最后一列（即刚刚新增的部门）
        self.driver.find_element_by_id('input_department_contact').send_keys('自动化测试人员4')       #在联系人输入框输入
        self.driver.find_element_by_id('input_department_tel').send_keys('13317204396')       #在联系方式输入框中输入符合格式的手机号
        self.add_img()
        self.driver.find_element_by_id('btn_department_save').click()                          #点击弹窗中的保存按钮
        sleep(1)
        link6=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功', link6.text)
        self.add_img()
        self.save_img('添加成功2') 
        # self.driver.get_screenshot_as_file("C:/Users/ZAssitant/Desktop/Geoportal/部门管理/success_img/添加成功2.png")  #截图可自定义截图后的保存位置和图片命名
        sleep(2)

   
#用例7：在部门列表中选择删除父部门，查看是否提示有子部门
#已验证成功
    @BeautifulReport.add_test_img('取消删除') 
    def test_07_delete_dismiss(self):
        '''在部门列表中选择删除父部门，查看是否提示有子部门'''
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys('admin')  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys('admin123456')  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        self.driver.implicitly_wait(2)   #隐式等待2秒
        self.driver.find_element_by_link_text('系统设置').click()   #点击系统设置按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒
        self.driver.find_element_by_link_text('部门管理').click()   #点击部门管理按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒  
        #测试能否取消删除
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector('.fixed-table-body tbody tr:last-child td:last-child a:last-child')).perform()#使鼠标悬浮在删除按钮
        self.driver.find_element_by_css_selector('.fixed-table-body tbody tr:last-child td:last-child a:last-child').click()           #点击部门列表中的最后一列的删除按钮 
        sleep(1)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        sleep(3)
        print(alert.text)  # 打印窗口信息
        alert.dismiss()  # 点击弹窗取消按钮
#删除父部门
        self.driver.find_element_by_css_selector('.fixed-table-body tbody tr:first-child td:last-child a:last-child').click()           #点击部门列表中的第一列的删除按钮 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('该部门有子部门，请先删除子部门', link1.text)
        self.add_img()
        self.save_img('不能直接删除父部门')


#用例8：在部门列表中选择新增的部门,点击删除按钮,界面弹出“确认是否删除”,选择是,界面提示“删除成功”
#已验证成功
    @BeautifulReport.add_test_img('删除成功') 
    def test_08_delete_accept(self):
        '''在部门列表中选择新增的部门,点击删除按钮,界面弹出“确认是否删除”,选择是'''
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys('admin')  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys('admin123456')  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        self.driver.implicitly_wait(2)   #隐式等待2秒
        self.driver.find_element_by_link_text('系统设置').click()   #点击系统设置按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒
        self.driver.find_element_by_link_text('部门管理').click()   #点击部门管理按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒  
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector('.fixed-table-body tbody tr:last-child td:last-child a:last-child')).perform()#使鼠标悬浮在删除按钮
        sleep(2)
        self.driver.find_element_by_css_selector('.fixed-table-body tbody tr:last-child td:last-child a:last-child').click()           #点击部门列表中的最后一列的删除按钮
        sleep(2)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认
        sleep(1)
        link8=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link8.text)
        self.add_img()
        self.save_img('删除成功') 
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector('.fixed-table-body tbody tr:last-child td:last-child a:last-child')).perform()#使鼠标悬浮在删除按钮
        sleep(2)
        self.driver.find_element_by_css_selector('.fixed-table-body tbody tr:last-child td:last-child a:last-child').click()           #点击部门列表中的最后一列的删除按钮
        sleep(2)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认
        sleep(2)
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link1.text)
        self.add_img()
        


if __name__ == '__main__':
    unittest.main(argv=['ignored','-v'],exit=False)
    print('')
