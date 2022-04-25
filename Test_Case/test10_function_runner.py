''''
功能配置功能测试分为以下情况:
(1)点击功能配置按钮,查看是否进入功能配置页面
添加模块
(2)点击功能配置下的添加模块,查看是否弹出添加模块弹窗
(3)在添加模块弹窗中输入框输入空,点击保存,查看是否提示请输入模块名称
(4)在添加模块弹窗中输入模块名称,点击保存,查看是否保存成功（验证模块名称是否一致）
(5)在添加模块弹窗中输入模块名称、父模块,点击保存,查看是否保存成功(验证是否存在于刚刚的父模块下)
(6)在添加模块弹窗中输入模块名称、父模块、前端页面,点击保存,查看是否保存成功(验证前端页面是否名称对的上)
(7)在添加模块弹窗中输入模块名称、父模块、前端页面、前端标识,查看是否保存成功
(8)在添加模块弹窗中输入模块名称、父模块、前端页面、前端标识、后端标识,查看是否保存成功
(9)在添加模块弹窗中输入模块名称、父模块、前端页面、前端标识、后端标识、图标,查看是否保存成功
(10)在添加模块弹窗中输入模块名称、父模块、前端页面、前端标识、后端标识、图标、序号,查看是否保存成功
添加功能
(11)不选择任何模块,点击添加功能,查看是否提示需要选择模块
(12)点击添加功能,查看是否有弹窗弹出
(13)在添加功能弹窗输入空,点击确定,查看是否提示请输入功能名称
(14)在添加功能弹窗输入功能名称,点击确定,查看是否提示请输入DOM关键字
(15)在添加功能弹窗输入功能名称、DOM关键字,点击确定,查看是否添加成功
编辑模块
(16)点击某一模块对应编辑按钮,查看是否弹出模块编辑弹窗
(17)在编辑模块弹窗中依次分别修改模块名称、父模块、前端页面、前端标识、后端标识、图标、序号,查看是否分别修改成功
(18)在编辑模块弹窗中修改模块名称为空,查看是否提示模块名称不能为空
编辑功能
(19)点击某一模块下功能对应编辑按钮,查看是否弹出功能编辑弹窗
(20)在编辑功能弹窗中依次分别修改功能名称、DOM关键字,查看是否分别修改成功
(21)在编辑功能弹窗中对功能名称、DOM关键字修改为空,查看是否提示不能为空
删除
(22)点击某一模块对应的删除按钮,查看是否提示删除成功
(23)点击某一模块下功能对应的删除按钮,查看是否提示删除成功
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
from BeautifulReport import BeautifulReport
import os
import win32gui
import win32con
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from selenium.webdriver.support.expected_conditions import alert_is_present


class test10_function_Case(unittest.TestCase):

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
        # pass

    @classmethod
    def tearDownClass(cls):
        '''资源释放'''
        sleep(2)
        print('测试完成')
        cls.driver.quit()
        # pass

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass

    
#定义错误截图方法
    def save_img(self, img_name):  
        """
         传入一个img_name, 并存储到默认的文件路径下img
         :param img_name:
          :return:
         """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('./功能配置/img'), img_name))    #os.path.abspath('')截图存放路径

#定义登录方法进入功能配置界面
    def menu_s_function(self,username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys(username)  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys(password)  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        sleep(3)
         #显示等待时间到进入系统主界面
        # wait=WebDriverWait(self.driver,40,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        self.driver.find_element_by_link_text('系统设置').click()   #点击系统设置按钮
        sleep(2)
        self.driver.implicitly_wait(2)   #隐式等待2秒
        self.driver.find_element_by_link_text('功能配置').click()   #点击功能配置按钮
         #显示等待时间到进入用户管理界面
        # wait=WebDriverWait(self.driver,40,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_function_addmodule')))  
        sleep(2)

#用例1：点击功能配置按钮,查看是否进入功能配置页面
    @BeautifulReport.add_test_img('功能配置界面')
    def test_01_page_function(self):
        '''点击功能配置按钮,查看是否进入功能配置页面'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        #断言是否进入功能配置界面
        link1=self.driver.find_element_by_id('table_module')   #定位用户列表表头
        self.assertIn('模块名称',link1.text)
        self.add_img()
        self.save_img('功能配置主界面')
        sleep(1)

# 添加模块
#用例2：点击功能配置下的添加模块,查看是否弹出添加模块弹窗
    @BeautifulReport.add_test_img('添加模块弹窗')
    def test_02_add_module_pop(self):
        '''点击功能配置下的添加模块,查看是否弹出添加模块弹窗'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_id('btn_function_addmodule').click()  #点击添加模块按钮
        sleep(1)
        #显示等待时间到进入添加模块弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_module_form'))) 
        #断言是否弹出添加模块弹窗
        link1=self.driver.find_element_by_css_selector('#modal_module_edit  h5')   #定位添加模块位置
        self.assertIn('添加模块',link1.text)
        self.add_img()
        self.save_img('添加模块弹窗')

#用例3：在添加模块弹窗中输入框输入空,点击保存,查看是否提示请输入模块名称
    @BeautifulReport.add_test_img('请输入模块名称')
    def test_03_add_module_null(self):
        '''在添加模块弹窗中输入框输入空,点击保存,查看是否提示请输入模块名称'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_id('btn_function_addmodule').click()  #点击添加模块按钮
        sleep(1)
        #显示等待时间到进入添加模块弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_module_form'))) 
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_module_save').click()  #点击保存按钮
        #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('请输入模块名称',link1.text)
        self.add_img()
        self.save_img('请输入模块名称')

#用例4：在添加模块弹窗中输入模块名称,点击保存,查看是否保存成功（验证模块名称是否一致）
    @BeautifulReport.add_test_img('添加模块名称')
    def test_04_add_module_name(self):
        '''在添加模块弹窗中输入模块名称,点击保存,查看是否保存成功（验证模块名称是否一致）'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_id('btn_function_addmodule').click()  #点击添加模块按钮
        sleep(1)
        #显示等待时间到进入添加模块弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_module_form'))) 
        sleep(1)
        self.driver.find_element_by_id('input_module_name').send_keys('测试模块名称1')
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_module_save').click()  #点击保存按钮
        #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示保存成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功',link1.text)
        self.add_img()
        sleep(2)
        #断言是否添加在列表中
        link2=self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(2) td:nth-child(2)')  #定位添加的模块位置
        self.assertIn('测试模块名称1',link2.text)
        self.add_img()
        self.save_img('成功添加模块名称')

#用例5：在添加模块弹窗中输入模块名称、父模块,点击保存,查看是否保存成功(验证是否存在于刚刚的父模块下)
    @BeautifulReport.add_test_img('添加模块名称')
    def test_05_select_module_parent(self):
        '''在添加模块弹窗中输入模块名称、父模块,点击保存,查看是否保存成功(验证是否存在于刚刚的父模块下)'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_id('btn_function_addmodule').click()  #点击添加模块按钮
        sleep(1)
        #显示等待时间到进入添加模块弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_module_form'))) 
        sleep(1)
        self.driver.find_element_by_id('input_module_name').send_keys('测试模块名称2')
        sleep(1)
#选择父模块为用例4中新增的模块
        self.driver.find_element_by_css_selector('#input_module_form div:nth-child(2) div div').click()   #点击父模块按钮
        a=self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(1)')
        ActionChains(self.driver).move_to_element(a).pause(3).perform()#鼠标悬停在第一模块处
        self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(1) li:nth-child(2)').click()  #点击用例4新增的模块
        sleep(2)
        self.add_img()
        self.driver.find_element_by_id('btn_module_save').click()  #点击保存按钮
        #断言是否提示保存成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功',link1.text)
        self.add_img()
        sleep(2)
          #断言是否添加在列表中
        link2=self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(3) td:nth-child(2)')  #定位添加的模块位置
        self.assertIn('测试模块名称2',link2.text)
        self.add_img()
        self.save_img('成功选择父模块')

#用例6：在添加模块弹窗中输入模块名称、父模块、前端页面,点击保存,查看是否保存成功(验证前端页面是否名称对的上)
    @BeautifulReport.add_test_img('选择模块前端页面')
    def test_06_select_module_page(self):
        '''在添加模块弹窗中输入模块名称、父模块、前端页面,点击保存,查看是否保存成功(验证前端页面是否名称对的上)'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_id('btn_function_addmodule').click()  #点击添加模块按钮
        sleep(1)
        #显示等待时间到进入添加模块弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_module_form'))) 
        sleep(1)
        self.driver.find_element_by_id('input_module_name').send_keys('测试模块名称3')
        sleep(1)
#选择父模块为用例5中新增的模块
        self.driver.find_element_by_css_selector('#input_module_form div:nth-child(2) div div').click()   #点击父模块按钮
        a=self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(1) li:nth-child(2)')
        ActionChains(self.driver).move_to_element(a).pause(3).perform()#鼠标悬停在第一模块处
        self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(2) li').click()  #点击用例5新增的模块
        sleep(2)
        #选择前端页面
        self.driver.find_element_by_id('select_module_page').click() 
        self.driver.find_element_by_css_selector('#select_module_page option:last-child').click()  #选择最后一列前端页面
        sleep(2)
        self.add_img()
        self.driver.find_element_by_id('btn_module_save').click()  #点击保存按钮
        #断言是否提示保存成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功',link1.text)
        self.add_img()
        sleep(2)
 #断言是否添加在列表中
        link2=self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(4) td:nth-child(2)')  #定位添加的模块位置
        self.assertIn('测试模块名称3',link2.text)
        self.add_img()
        self.save_img('成功选择前端页面')

#用例7：在添加模块弹窗中输入模块名称、父模块、前端页面、前端标识,查看是否保存成功
    @BeautifulReport.add_test_img('模块前端标识')
    def test_07_input_module_fkey(self):
        '''在添加模块弹窗中输入模块名称、父模块、前端页面、前端标识,查看是否保存成功'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_id('btn_function_addmodule').click()  #点击添加模块按钮
        sleep(1)
        #显示等待时间到进入添加模块弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_module_form'))) 
        sleep(1)
        self.driver.find_element_by_id('input_module_name').send_keys('测试模块名称4')
        sleep(1)
#选择父模块为用例5中新增的模块
        self.driver.find_element_by_css_selector('#input_module_form div:nth-child(2) div div').click()   #点击父模块按钮
        a=self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(1) li:nth-child(2)')
        ActionChains(self.driver).move_to_element(a).pause(3).perform()#鼠标悬停在第一模块处
        self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(2) li').click()  #点击用例5新增的模块
        sleep(2)
        #选择前端页面
        self.driver.find_element_by_id('select_module_page').click() 
        self.driver.find_element_by_css_selector('#select_module_page option:last-child').click()  #选择最后一列前端页面
        sleep(2)
        #输入前端标识
        self.driver.find_element_by_id('input_module_fkey').send_keys('cs1')
        self.add_img()
        self.driver.find_element_by_id('btn_module_save').click()  #点击保存按钮
        #断言是否提示保存成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功',link1.text)
        self.add_img()
        sleep(2)
#断言添加的模块标识是否正确
        link2=self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(5) td:nth-child(4)')
        self.assertIn('cs1',link2.text)
        self.save_img('模块前端标识')
        self.add_img()

#用例8：在添加模块弹窗中输入模块名称、父模块、前端页面、前端标识、后端标识,查看是否保存成功
    @BeautifulReport.add_test_img('模块后端标识')
    def test_08_input_module_bkey(self):
        '''在添加模块弹窗中输入模块名称、父模块、前端页面、前端标识、后端标识,查看是否保存成功'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_id('btn_function_addmodule').click()  #点击添加模块按钮
        sleep(1)
        #显示等待时间到进入添加模块弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_module_form'))) 
        sleep(1)
        self.driver.find_element_by_id('input_module_name').send_keys('测试模块名称5')
        sleep(1)
#选择父模块为用例5中新增的模块
        self.driver.find_element_by_css_selector('#input_module_form div:nth-child(2) div div').click()   #点击父模块按钮
        a=self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(1) li:nth-child(2)')
        ActionChains(self.driver).move_to_element(a).pause(3).perform()#鼠标悬停在第一模块处
        self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(2) li').click()  #点击用例5新增的模块
        sleep(2)
        #选择前端页面
        self.driver.find_element_by_id('select_module_page').click() 
        self.driver.find_element_by_css_selector('#select_module_page option:last-child').click()  #选择最后一列前端页面
        sleep(2)
        #输入前端标识
        self.driver.find_element_by_id('input_module_fkey').send_keys('cs2')
        #输入后端标识
        self.driver.find_element_by_id('input_module_bkey').send_keys('bkey_cs2')
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_module_save').click()  #点击保存按钮
        #断言是否提示保存成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功',link1.text)
        self.add_img()
        sleep(2)
#断言添加的模块标识是否正确
        link2=self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(6) td:nth-child(5)')
        self.assertIn('bkey_cs2',link2.text)
        self.save_img('模块后端标识')
        self.add_img()

#用例9：在添加模块弹窗中输入模块名称、父模块、前端页面、前端标识、后端标识、图标,查看是否保存成功
    @BeautifulReport.add_test_img('模块图标')
    def test_09_input_module_icon(self):
        '''在添加模块弹窗中输入模块名称、父模块、前端页面、前端标识、后端标识、图标,查看是否保存成功'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_id('btn_function_addmodule').click()  #点击添加模块按钮
        sleep(1)
        #显示等待时间到进入添加模块弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_module_form'))) 
        sleep(1)
        self.driver.find_element_by_id('input_module_name').send_keys('测试模块名称6')
        sleep(1)
#选择父模块为用例5中新增的模块
        self.driver.find_element_by_css_selector('#input_module_form div:nth-child(2) div div').click()   #点击父模块按钮
        a=self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(1) li:nth-child(2)')
        ActionChains(self.driver).move_to_element(a).pause(3).perform()#鼠标悬停在第一模块处
        self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(2) li').click()  #点击用例5新增的模块
        sleep(2)
        #选择前端页面
        self.driver.find_element_by_id('select_module_page').click() 
        self.driver.find_element_by_css_selector('#select_module_page option:last-child').click()  #选择最后一列前端页面
        sleep(2)
        #输入前端标识
        self.driver.find_element_by_id('input_module_fkey').send_keys('cs3')
        #输入后端标识
        self.driver.find_element_by_id('input_module_bkey').send_keys('bkey_cs3')
        sleep(1)
        #输入图标
        self.driver.find_element_by_id('input_module_icon').send_keys('bi bi-book-half')
        self.add_img()
        self.driver.find_element_by_id('btn_module_save').click()  #点击保存按钮
        #断言是否提示保存成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功',link1.text)
        self.add_img()
        sleep(2)
        self.save_img('模块图标')

#用例10：在添加模块弹窗中输入模块名称、父模块、前端页面、前端标识、后端标识、图标、序号,查看是否保存成功
    @BeautifulReport.add_test_img('模块序号')
    def test_10_input_module_index(self):
        '''在添加模块弹窗中输入模块名称、父模块、前端页面、前端标识、后端标识、图标、序号,查看是否保存成功'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_id('btn_function_addmodule').click()  #点击添加模块按钮
        sleep(1)
        #显示等待时间到进入添加模块弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_module_form'))) 
        sleep(1)
        self.driver.find_element_by_id('input_module_name').send_keys('测试模块名称7')
        sleep(1)
#选择父模块为用例5中新增的模块
        self.driver.find_element_by_css_selector('#input_module_form div:nth-child(2) div div').click()   #点击父模块按钮
        a=self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(1) li:nth-child(2)')
        ActionChains(self.driver).move_to_element(a).pause(3).perform()#鼠标悬停在第一模块处
        self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(2) li').click()  #点击用例5新增的模块
        sleep(2)
        #选择前端页面
        self.driver.find_element_by_id('select_module_page').click() 
        self.driver.find_element_by_css_selector('#select_module_page option:last-child').click()  #选择最后一列前端页面
        sleep(2)
        #输入前端标识
        self.driver.find_element_by_id('input_module_fkey').send_keys('cs4')
        #输入后端标识
        self.driver.find_element_by_id('input_module_bkey').send_keys('bkey_cs4')
        sleep(1)
        #输入图标
        self.driver.find_element_by_id('input_module_icon').send_keys('bi bi-book-half')
        #输入序号
        el=self.driver.find_element_by_id('input_module_index')
        el.clear()
        el.send_keys('6')
        sleep(2)
        self.add_img()
        self.driver.find_element_by_id('btn_module_save').click()  #点击保存按钮
        #断言是否提示保存成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功',link1.text)
        self.add_img()
        sleep(2)
#断言添加的模块序号是否正确
        link2=self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(7)')   #定位新增模块序号位置
        self.assertIn('6',link2.text)
        self.add_img()
        self.save_img('模块序号')

# 添加功能
#用例11：不选择任何模块,点击添加功能,查看是否提示需要选择模块
    @BeautifulReport.add_test_img('模块序号')
    def test_11_addfunction(self):
        '''不选择任何模块,点击添加功能,查看是否提示需要选择模块'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_id('btn_function_addfunction').click()    #点击添加功能按钮
        sleep(1)
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('请选择一个模块',link1.text)
        self.add_img()
        self.save_img('请输入模块名称')

#用例12：选择新增的某一模块，点击添加功能,查看是否有弹窗弹出
    @BeautifulReport.add_test_img('模块序号')
    def test_12_addfunction_pop(self):
        '''选择新增的某一模块，点击添加功能,查看是否有弹窗弹出'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(1)').click()    #选择新增的模块
        sleep(1)
        self.driver.find_element_by_id('btn_function_addfunction').click()    #点击添加功能按钮
        sleep(1)
          #显示等待时间直到添加功能弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_function_form'))) 
        #断言是否弹出添加功能弹窗
        link1=self.driver.find_element_by_css_selector('#modal_function_edit h5')
        self.assertIn('添加功能',link1.text)
        self.add_img()
        self.save_img('添加功能弹窗')

#用例13：在添加功能弹窗输入空,点击确定,查看是否提示请输入功能名称
    @BeautifulReport.add_test_img('功能名称为空')
    def test_13_addfunction_null(self):
        '''在添加功能弹窗输入空,点击确定,查看是否提示请输入功能名称'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(1)').click()    #选择新增的模块
        sleep(1)
        self.driver.find_element_by_id('btn_function_addfunction').click()    #点击添加功能按钮
        self.add_img()
        self.driver.find_element_by_id('btn_function_save').click()  #点击保存按钮
          #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否弹出添加功能弹窗
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('请输入功能名称',link1.text)
        self.add_img()
        self.save_img('功能名称为空')

#用例14：在添加功能弹窗输入功能名称,点击确定,查看是否提示请输入DOM关键字
    @BeautifulReport.add_test_img('DOM关键字为空')
    def test_14_addfunction_name(self):
        '''在添加功能弹窗输入功能名称,点击确定,查看是否提示请输入DOM关键字'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(1)').click()    #选择新增的模块
        sleep(1)
        self.driver.find_element_by_id('btn_function_addfunction').click()    #点击添加功能按钮
        self.driver.find_element_by_id('input_function_name').send_keys('测试功能名称')  #输入功能名称
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_function_save').click()  #点击保存按钮
        sleep(1)
          #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否弹出添加功能弹窗
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('请输入DOM关键字',link1.text)
        self.add_img()
        self.save_img('DOM关键字为空')

#用例15：在添加功能弹窗输入功能名称、DOM关键字,点击确定,查看是否添加成功
    @BeautifulReport.add_test_img('DOM关键字为空')
    def test_15_addfunction_name(self):
        '''在添加功能弹窗输入功能名称,点击确定,查看是否提示请输入DOM关键字'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(1)').click()    #选择新增的模块
        sleep(1)
        self.driver.find_element_by_id('btn_function_addfunction').click()    #点击添加功能按钮
        self.driver.find_element_by_id('input_function_name').send_keys('测试功能名称')  #输入功能名称
        sleep(1)
        self.driver.find_element_by_id('input_function_domkey').send_keys('btn delete')   #输入DOM关键字
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_function_save').click()  #点击保存按钮
          #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否弹出添加功能弹窗
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功',link1.text)
        self.add_img()
#回到列表中判断是否刚刚新增的功能存在于列表中
        self.driver.refresh()   #刷新页面
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(1)').click()    #选择新增的模块
        sleep(1)
        link2=self.driver.find_element_by_css_selector('#table_function tbody tr td:nth-child(1)')
        self.assertIn('测试功能名称',link2.text)
        self.add_img()
        self.save_img('添加功能成功')

# 编辑模块
#用例16：点击某一模块对应编辑按钮,查看是否弹出模块编辑弹窗
    @BeautifulReport.add_test_img('DOM关键字为空')
    def test_16_edit_module_pop(self):
        '''点击某一模块对应编辑按钮,查看是否弹出模块编辑弹窗'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td a:first-child').click()   #点击新增模块的编辑按钮
        sleep(1)
         #显示等待时间到进入编辑模块弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_module_form'))) 
        #断言是否弹出添加模块弹窗
        link1=self.driver.find_element_by_css_selector('#modal_module_edit  h5')   #定位添加模块位置
        self.assertIn('编辑功能',link1.text)
        self.add_img()
        self.save_img('编辑模块弹窗')

#用例17：在编辑模块弹窗中依次分别修改模块名称、父模块、前端页面、前端标识、后端标识、图标、序号,查看是否分别修改成功
    @BeautifulReport.add_test_img('编辑模块')
    def test_17_edit_module(self):
        '''在编辑模块弹窗中依次分别修改模块名称、父模块、前端页面、前端标识、后端标识、图标、序号,查看是否分别修改成功'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td a:first-child').click()   #点击新增模块的编辑按钮
        sleep(1)
        #显示等待时间到进入编辑模块弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_module_form'))) 
        self.add_img()
#修改模块名称 
        self.driver.find_element_by_id('input_module_name').clear()  #清空模块名称编辑框
        self.driver.find_element_by_id('input_module_name').send_keys('修改后模块名称')  #输入模块名称
        sleep(1)
        self.add_img()
#修改父模块
        self.driver.find_element_by_css_selector('#input_module_form div:nth-child(2) div div').click()   #点击父模块按钮
        a=self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(1)')
        ActionChains(self.driver).move_to_element(a).pause(3).perform()#鼠标悬停在第一模块处
        self.driver.find_element_by_css_selector('.cascader-dropdown-container ul:nth-child(1) li:nth-child(2)').click()  #点击用例4新增的模块
        sleep(1)
        self.add_img()
#修改前端页面
        self.driver.find_element_by_id('select_module_page').click() 
        self.driver.find_element_by_css_selector('#select_module_page option:first-child').click()  #选择最后一列前端页面
        sleep(1)
        self.add_img()
#修改前端标识 
        self.driver.find_element_by_id('input_module_fkey').clear()
        self.driver.find_element_by_id('input_module_fkey').send_keys('edit-fkey-cs')
        self.add_img()
#修改后端标识
        self.driver.find_element_by_id('input_module_bkey').clear()
        self.driver.find_element_by_id('input_module_bkey').send_keys('edit-bkey-cs')
        self.add_img()
#修改图标
        self.driver.find_element_by_id('input_module_icon').clear()
        self.driver.find_element_by_id('input_module_icon').send_keys('bi bi-bookmarks-fill')
        self.add_img()
#修改序号
        self.driver.find_element_by_id('input_module_index').clear()
        self.driver.find_element_by_id('input_module_index').send_keys('2')
        sleep(2)
        self.add_img()
        self.driver.find_element_by_id('btn_module_save').click()   #点击保存按钮
        #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否弹出添加功能弹窗
        lin=self.driver.find_element_by_id('alter_notify')
        self.assertIn('编辑成功',lin.text)
        self.add_img()
    #回到列表查看模块名称是否修改
        link1=self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(2)')   #定位刚刚修改的模块名称位置
        self.assertIn('修改后模块名称',link1.text)
    #回到列表查看前端标识是否修改
        link2=self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(4)')    #定位刚刚修改的模块前端标识位置
        self.assertIn('edit-fkey-cs',link2.text)
    #回到列表查看后端标识是否修改
        link3=self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(5)')    #定位刚刚修改的模块后端标识位置
        self.assertIn('edit-bkey-cs',link3.text)
    # #回到列表查看图标是否修改
    #     link4=self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(6)')    #定位刚刚修改的模块图标位置
    #     self.assertIn('bi bi-bookmarks-fill',link4.text)
    #回到列表查看序号是否修改
        link5=self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(7)')    #定位刚刚修改的模块序号位置
        self.assertIn('2',link5.text)
        self.add_img()
        self.save_img('成功编辑模块')

#用例18：在编辑模块弹窗中修改模块名称为空,查看是否提示模块名称不能为空
    @BeautifulReport.add_test_img('编辑模块名称为空')
    def test_18_edit_module_name_null(self):
        '''在编辑模块弹窗中修改模块名称为空,查看是否提示模块名称不能为空'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td a:first-child').click()   #点击新增模块的编辑按钮
        sleep(1)
        #显示等待时间到进入编辑模块弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_module_form'))) 
        #修改模块名称为空
        self.driver.find_element_by_id('input_module_name').clear()  #清空模块名称编辑框
        self.add_img()
        self.driver.find_element_by_id('btn_module_save').click()   #点击保存按钮
        sleep(1)
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否弹出添加功能弹窗
        lin=self.driver.find_element_by_id('alter_notify')
        self.assertIn('请输入模块名称',lin.text)
        self.add_img()
        self.save_img('编辑模块输入框不能为空')

# 编辑功能
#用例19：点击某一模块下功能对应编辑按钮,查看是否弹出功能编辑弹窗
    @BeautifulReport.add_test_img('编辑功能弹窗')
    def test_19_edit_addfunction_pop(self):
        '''点击某一模块下功能对应编辑按钮,查看是否弹出功能编辑弹窗'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(1)').click()    #选择新增的模块
        sleep(1)
        self.driver.find_element_by_css_selector('#table_function tbody tr td a:first-child').click()    #点击新增模块下第一个功能的编辑按钮
        sleep(1)
        #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_function_form'))) 
        #断言是否弹出添加功能弹窗
        link1=self.driver.find_element_by_css_selector('#modal_function_edit h5')
        self.assertIn('编辑功能',link1.text)
        self.add_img()
        self.save_img('编辑功能弹窗')

#用例20：在编辑功能弹窗中依次分别修改功能名称、DOM关键字,查看是否分别修改成功
    @BeautifulReport.add_test_img('编辑功能成功')
    def test_20_edit_addfunction(self):
        '''点击某一模块下功能对应编辑按钮,查看是否弹出功能编辑弹窗'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(1)').click()    #选择新增的模块
        sleep(1)
        self.driver.find_element_by_css_selector('#table_function tbody tr td a:first-child').click()  #点击新增模块下第一个功能的编辑按钮
        sleep(1)
        #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_function_form'))) 
#修改功能名称
        self.driver.find_element_by_id('input_function_name').send_keys('修改')
#修改DOM关键字
        self.driver.find_element_by_id('input_function_domkey').send_keys(' edit')
        self.add_img()
        self.driver.find_element_by_id('btn_function_save').click()   #点击保存按钮
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否弹出添加功能弹窗
        lin=self.driver.find_element_by_id('alter_notify')
        self.assertIn('编辑成功',lin.text)
        self.add_img()
    #断言判定修改的功能名称和关键字是否为修改后的
        #判定功能名称
        link1=self.driver.find_element_by_css_selector('#table_function tbody tr td:nth-child(1)')
        self.assertIn('修改',link1.text)
        #判定DOM关键字
        link2=self.driver.find_element_by_css_selector('#table_function tbody tr td:nth-child(2)')
        self.assertIn('edit',link2.text)
        self.add_img()
        self.save_img('成功编辑功能')

#用例21：在编辑功能弹窗中对功能名称、DOM关键字修改为空,查看是否提示不能为空
    @BeautifulReport.add_test_img('编辑功能为空')
    def test_21_edit_addfunction_null(self):
        '''在编辑功能弹窗中对功能名称、DOM关键字修改为空,查看是否提示不能为空'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(1)').click()    #选择新增的模块
        sleep(1)
        self.driver.find_element_by_css_selector('#table_function tbody tr td a:first-child').click()  #点击新增模块下第一个功能的编辑按钮
        sleep(1)
        #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_function_form'))) 
#修改功能名称为空
        el1=self.driver.find_element_by_id('input_function_name')
        el1.clear()
        self.add_img()
        self.driver.find_element_by_id('btn_function_save').click()   #点击保存按钮
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否弹出添加功能弹窗
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('请输入功能名称',link1.text)
        self.add_img()
        self.save_img('修改功能名称不能为空')
        sleep(1)
        el1.send_keys('修改功能名称不能为空')
        sleep(2)
#修改DOM关键字
        el2=self.driver.find_element_by_id('input_function_domkey')
        el2.clear()
        self.add_img()
        self.driver.find_element_by_id('btn_function_save').click()   #点击保存按钮
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否弹出添加功能弹窗
        link2=self.driver.find_element_by_id('alter_notify')
        self.assertIn('请输入DOM关键字',link2.text)
        self.add_img()
        self.save_img('修改DOM不能为空')
        sleep(1)
        el2.send_keys(' DOM_null')
        sleep(2)
        self.driver.find_element_by_id('btn_function_save').click()   #点击保存按钮
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否弹出添加功能弹窗
        lin=self.driver.find_element_by_id('alter_notify')
        self.assertIn('编辑成功',lin.text)
        self.add_img()
        sleep(1)

#用例22：点击有子模块或功能的模块对应删除按钮,查看是否提示有子模块不能删除
    @BeautifulReport.add_test_img('删除父模块')
    def test_22_delete_module_parent(self):
        '''点击有子模块或功能的模块对应删除按钮,查看是否提示有子模块不能删除'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(2) td a:last-child').click()   #点击新增模块的删除按钮
        # #显示等待时间直到提示弹窗出现
        # wait=WebDriverWait(self.driver,40,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        sleep(1)
        #断言是否弹出添加功能弹窗
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('该模块有子模块，无法删除',link1.text)
        self.add_img()
        self.save_img('无法删除有子模块的模块')
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) a:last-child').click()    #选择最后一列新增模块的删除按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取删除确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认删除
        link2=self.driver.find_element_by_id('alter_notify')
        self.assertIn('模块下存在功能，无法删除',link2.text)
        self.add_img()
        self.save_img('无法删除有功能的模块')
        sleep(1)


#删除
#用例23：点击某一模块下功能对应的删除按钮,查看是否提示删除成功
    @BeautifulReport.add_test_img('删除功能')
    def test_23_delete_addfunction(self):
        '''点击某一模块下功能对应的删除按钮,查看是否提示删除成功'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td:nth-child(1)').click()    #选择新增的模块
        sleep(1)
        self.driver.find_element_by_css_selector('#table_function tbody tr td a:last-child').click()  #点击新增模块下第一个功能的删除按钮
        sleep(1)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取删除确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认删除
        sleep(2)
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link1.text)
        self.add_img()
        self.save_img('删除功能成功') 
        sleep(2)



#用例24：点击某一模块对应的删除按钮,查看是否提示删除成功
    @BeautifulReport.add_test_img('删除子模块')
    def test_24_delete_module(self):
        '''点击某一模块对应的删除按钮,查看是否提示删除成功'''
        self.menu_s_function('admin','admin123456')    #进入功能配置界面
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(8) td a:last-child').click()   #点击新增模块的删除按钮
        sleep(2)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取删除确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认删除
        sleep(2)
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link1.text)
        self.add_img()
        self.save_img('删除子模块成功') 
        sleep(2)
#删除以上新增的所有功能模块
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(7) td a:last-child').click()   #点击新增模块的删除按钮
        sleep(2)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取删除确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认删除
        sleep(2)
        self.add_img()
        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(6) td a:last-child').click()   #点击新增模块的删除按钮
        sleep(2)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取删除确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认删除
        sleep(2)
        self.add_img()

        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(5) td a:last-child').click()   #点击新增模块的删除按钮
        sleep(2)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取删除确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认删除
        sleep(2)
        self.add_img()

        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(4) td a:last-child').click()   #点击新增模块的删除按钮
        sleep(2)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取删除确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认删除
        sleep(2)
        self.add_img()

        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(3) td a:last-child').click()   #点击新增模块的删除按钮
        sleep(2)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取删除确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认删除
        sleep(2)
        self.add_img()

        self.driver.find_element_by_css_selector('#table_module tbody tr:nth-child(2) td a:last-child').click()   #点击新增模块的删除按钮
        sleep(2)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取删除确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认删除
        sleep(2)
        self.add_img()

    
if __name__ == '__main__':
    unittest.main(argv=['ignored','-v'],exit=False)
    print('')


