''''
角色权限功能测试分为以下情况：
用例1:点击角色权限按钮,查看是否正常进入角色权限界面
添加角色
用例2:点击添加角色按钮,查看是否弹窗添加角色弹窗
用例3:添加角色弹窗中角色名称输入为空,查看是否提示请输入角色名称
用例4:添加角色弹窗输入角色名称,查看是否提示添加成功(在角色列表和用户管理中验证)
用例5:添加角色弹窗输入已添加过的角色名称,查看是否提示已存在相同角色
编辑角色
用例6:点击角色列表中的编辑按钮,查看是否弹出编辑角色名称弹窗
用例7:在编辑角色弹窗中修改角色名称,查看角色名称是否修改
删除角色
用例8:点击角色列表中没有用户的角色对应删除按钮,点击确认删除,查看是否删除该角色
用例9:点击角色列表中有用户的角色对应删除按钮,点击确认删除,查看是否提示该角色下有用户,无法删除
分配权限
用例10:对测试角色进行模块分配,使用角色账户登录查看是否分配成功
用例11:对测试角色进行功能分配,使用角色账户登录查看是否分配成功
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



class test11_role_Case(unittest.TestCase):

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
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('./角色权限/img'), img_name))    #os.path.abspath('')截图存放路径

#定义登录方法进入角色权限界面
    def menu_role(self,username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys(username)  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys(password)  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        sleep(2)
        #  #显示等待时间到进入系统主界面
        # wait=WebDriverWait(self.driver,40,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        self.driver.find_element_by_link_text('系统设置').click()   #点击系统设置按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒
        sleep(1)
        self.driver.find_element_by_link_text('角色权限').click()   #点击角色权限按钮
         #显示等待时间到进入角色权限主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_role_add'))) 
        sleep(2)
        
#定义登录
    def login(self,username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys(username)  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys(password)  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        sleep(3)
          #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 


# 用例1:点击角色权限按钮,查看是否正常进入角色权限界面
    @BeautifulReport.add_test_img('角色权限界面')
    def test_01_page_role(self):
        '''点击角色权限按钮,查看是否正常进入角色权限界面'''
        self.menu_role('admin','admin123456')    #进入角色权限界面
        #断言是否进入功能配置界面
        link1=self.driver.find_element_by_css_selector('#table_role thead tr th:nth-child(2) div')  #定位角色列表表头
        self.assertIn('角色名称',link1.text)
        self.add_img()
        self.save_img('角色权限主界面')
        sleep(1)
    
# 添加角色
# 用例2:点击添加角色按钮,查看是否弹窗添加角色弹窗
    @BeautifulReport.add_test_img('添加角色弹窗')
    def test_02_add_role_pop(self):
        '''点击添加角色按钮,查看是否弹窗添加角色弹窗'''
        self.menu_role('admin','admin123456')    #进入角色权限界面
        self.driver.find_element_by_id('btn_role_add').click()   #点击添加角色按钮
        self.driver.implicitly_wait(2)
        sleep(2)
        #断言判定是否进入添加角色弹窗
        link1=self.driver.find_element_by_css_selector('#modal_role_edit h5')  
        self.assertIn('添加角色',link1.text)
        self.add_img()
        self.save_img('添加角色弹窗')

# 用例3:添加角色弹窗中角色名称输入为空,查看是否提示请输入角色名称
    @BeautifulReport.add_test_img('角色名称为空')
    def test_03_add_role_name_null(self):
        '''添加角色弹窗中角色名称输入为空,查看是否提示请输入角色名称'''
        self.menu_role('admin','admin123456')    #进入角色权限界面
        self.driver.find_element_by_id('btn_role_add').click()   #点击添加角色按钮
        self.driver.implicitly_wait(2)
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_role_save').click()   #点击保存按钮
        sleep(0.5)
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('The Name field is required.',link1.text)
        self.add_img()
        self.save_img('请输入角色名称')

# 用例4:添加角色弹窗输入角色名称,查看是否提示添加成功(在角色列表和用户管理中验证)
    @BeautifulReport.add_test_img('添加角色')
    def test_04_add_role_name(self):
        '''添加角色弹窗输入角色名称,查看是否提示添加成功'''
        self.menu_role('admin','admin123456')    #进入角色权限界面
        self.driver.find_element_by_id('btn_role_add').click()   #点击添加角色按钮
        self.driver.implicitly_wait(2)
        sleep(1)
        self.driver.find_element_by_id('input_role_name').send_keys('测试角色名称')
        sleep(2)
        self.add_img()
        self.driver.find_element_by_id('btn_role_save').click()   #点击保存按钮
        sleep(0.5)
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示添加成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功',link1.text)
        self.add_img()
        #断言查看角色列表中是否存在刚刚新增的角色
        link2=self.driver.find_element_by_css_selector('#table_role tbody tr:last-child td:nth-child(2)')
        self.assertIn('测试角色名称',link2.text)
        self.save_img('添加角色名称')
        #到用户管理中的添加用户查看选择角色是否有刚刚新增的角色
        self.driver.refresh() #刷新页面
        self.driver.find_element_by_link_text('系统设置').click()   #点击系统设置按钮
        self.driver.find_element_by_link_text('用户管理').click()   #点击用户管理按钮
        self.driver.find_element_by_id('btn_user_add').click()   #点击添加用户按钮
        sleep(2)
        self.driver.find_element_by_id('select_user_role').click()   #点击用户角色按钮
        sleep(1)
        #断言可选择的用户角色是否有刚刚新增的角色
        link3=self.driver.find_element_by_css_selector('#select_user_role option:last-child')
        self.assertIn('测试角色名称',link3.text)
        self.add_img()
        self.save_img('成功添加用户角色')

# 用例5:添加角色弹窗输入已添加过的角色名称,查看是否提示已存在相同角色
    @BeautifulReport.add_test_img('添加角色')
    def test_05_add_role_same_name(self):
        '''添加角色弹窗输入已添加过的角色名称,查看是否提示已存在相同角色'''
        self.menu_role('admin','admin123456')    #进入角色权限界面
        self.driver.find_element_by_id('btn_role_add').click()   #点击添加角色按钮
        self.driver.implicitly_wait(2)
        sleep(1)
        self.driver.find_element_by_id('input_role_name').send_keys('测试角色名称')
        sleep(2)
        self.add_img()
        self.driver.find_element_by_id('btn_role_save').click()   #点击保存按钮
        sleep(0.5)
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示添加成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('已存在相同名称的角色',link1.text)
        self.add_img()
        self.save_img('添加相同角色名称')

# 编辑角色
# 用例6:点击角色列表中的编辑按钮,查看是否弹出编辑角色名称弹窗
    @BeautifulReport.add_test_img('添加角色')
    def test_06_edit_role_pop(self):
        '''点击角色列表中的编辑按钮,查看是否弹出编辑角色名称弹窗'''
        self.menu_role('admin','admin123456')    #进入角色权限界面
        self.driver.find_element_by_css_selector('#table_role tbody tr:last-child a:first-child').click()  #点击角色名称最后一列的编辑按钮
        sleep(2)
        #断言是否弹出编辑角色弹窗
        link1=self.driver.find_element_by_css_selector('#modal_role_edit h5')
        self.assertIn('编辑角色',link1.text)
        self.add_img()
        self.save_img('编辑角色弹窗')

# 用例7:在编辑角色弹窗中修改角色名称为空和更改,查看是否提示以及角色名称是否修改
    @BeautifulReport.add_test_img('编辑角色')
    def test_07_edit_role(self):
        '''在编辑角色弹窗中修改角色名称为空和更改,查看是否提示以及角色名称是否修改'''
        self.menu_role('admin','admin123456')    #进入角色权限界面
        self.driver.find_element_by_css_selector('#table_role tbody tr:last-child a:first-child').click()  #点击角色名称最后一列的编辑按钮
        sleep(2)
        el=self.driver.find_element_by_id('input_role_name')  #定位角色名称输入框
        el.clear()   #情况角色名称输入框
        self.add_img()
        self.driver.find_element_by_id('btn_role_save').click()   #点击保存按钮
        sleep(0.5)
          #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示不能为空
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('The Name field is required.',link1.text)
        self.add_img()
        self.save_img('编辑角色名称为空')
        el.send_keys('修改后角色名称')
        sleep(2)
        self.add_img()
        self.driver.find_element_by_id('btn_role_save').click()   #点击保存按钮
        sleep(1)
        #  #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,10,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示编辑成功
        link2=self.driver.find_element_by_id('alter_notify')
        self.assertIn('编辑成功',link2.text)
        self.add_img()
        self.save_img('编辑角色名称成功')
        sleep(2)
        #断言角色名称列表中是否修改完成
        link3=self.driver.find_element_by_css_selector('#table_role tbody tr:last-child td:nth-child(2)')
        self.assertIn('修改后角色名称',link3.text)
        sleep(1)
         #到用户管理中的添加用户查看选择角色是否有刚刚新增的角色
        self.driver.refresh() #刷新页面
        self.driver.find_element_by_link_text('系统设置').click()   #点击系统设置按钮
        self.driver.find_element_by_link_text('用户管理').click()   #点击用户管理按钮
        self.driver.find_element_by_id('btn_user_add').click()   #点击添加用户按钮
        sleep(2)
        self.driver.find_element_by_id('select_user_role').click()   #点击用户角色按钮
        sleep(1)
        #断言可选择的用户角色是否有刚刚新增的角色
        link4=self.driver.find_element_by_css_selector('#select_user_role option:last-child')
        self.assertIn('修改后角色名称',link4.text)
        self.add_img()
        self.save_img('成功验证编辑角色名称')

# 分配权限
# 用例8:对测试角色进行模块分配,使用角色账户登录查看是否分配成功
    @BeautifulReport.add_test_img('角色权限模块分配')
    def test_08_role_module_distribution(self):
        '''对测试角色进行模块分配,使用角色账户登录查看是否分配成功'''
        self.menu_role('admin','admin123456')    #进入角色权限界面
        self.driver.find_element_by_css_selector('#table_role tbody tr:last-child td:nth-child(2)').click()   #点击角色列表最后一列角色
#对功能模块进行分配
        #分配地图管理模块、portal总览、图层管理、数据管理模块
        # self.driver.find_element_by_css_selector('#table_action_power tbody tr:nth-child(2) td:nth-child(2) span').click()   #点击地图管理展开按钮
        # self.driver.find_element_by_css_selector('#table_action_power tbody tr:nth-child(3) input').click() 
        self.driver.find_element_by_css_selector('#table_action_power tbody tr:nth-child(1) input').click()    #点击勾选poratl总览模块
        sleep(1)
        self.driver.find_element_by_css_selector('#table_action_power tbody tr:nth-child(2) input').click()    #点击勾选地图管理模块
        sleep(1)
        # self.driver.find_element_by_css_selector('#table_action_power tbody tr:nth-child(8) input').click()    #点击勾选图层管理模块
        # sleep(1)
        # self.driver.find_element_by_css_selector('#table_action_power tbody tr:nth-child(12) input').click()    #点击勾选数据管理模块
        self.save_img('用户权限模块分配')
        self.add_img()
        sleep(1)
#跳转至用户管理中新增用户，选择用户角色为测试角色
        self.driver.find_element_by_link_text('用户管理').click()   #点击用户管理按钮
        sleep(2)
        self.driver.find_element_by_id('btn_user_add').click()  #点击添加用户按钮
        el=self.driver.find_element_by_id('input_user_userName')
        el.click()
        sleep(2)
        el.send_keys('测试用户角色权限')   #输入用户名
        sleep(1)
        self.driver.find_element_by_id('input_user_password').send_keys('123')   #输入登录密码
        sleep(1)
        self.driver.find_element_by_id('input_user_repassword').send_keys('123')    #在确认密码框内输入与登录密码一致的密码
        sleep(1)
        self.driver.find_element_by_id('input_user_realName').send_keys('测试权限真实姓名')   #输入真实姓名
        sleep(3)
        self.driver.find_element_by_css_selector('#input_user_form  div:nth-child(5) div:first-child ').click()   #点击所在部门选择框
        sleep(1)
        a=self.driver.find_element_by_css_selector('.modal-open div.cascader-dropdown-container ul:first-child')
        ActionChains(self.driver).move_to_element(a).pause(3).perform()#鼠标悬停在第一大部门处
        sleep(1)
        self.driver.find_element_by_css_selector('.modal-open div.cascader-dropdown-container  ul:first-child li:first-child').click()#点击第一大部门的第一小组
        sleep(2)
        self.driver.find_element_by_id('select_user_role').click()  #点击角色输入框
        self.driver.find_element_by_css_selector('#select_user_role option:last-child').click() #选择角色列表中的最后一个角色
        sleep(1)
        self.driver.find_element_by_id('input_user_phone').send_keys('10086')   #输入手机号
        sleep(1)
        self.driver.find_element_by_id('btn_user_save').click()    #点击保存按钮 
        sleep(1)
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#使用第一大部门下第二小组成员账户登录
        self.login('测试用户角色权限','123')   #使用刚刚新增的角色账户登录
        link1=self.driver.find_element_by_id('ul_menu')
        self.assertIn('菜单\nPortal总览\n地图管理',link1.text)
        self.save_img('验证用户权限模块分配')
        self.add_img()
   
# 用例9:对测试角色进行功能分配,使用角色账户登录查看是否分配成功
    @BeautifulReport.add_test_img('角色权限模块分配')
    def test_09_role_function_distribution(self):
        '''对测试角色进行功能分配,使用角色账户登录查看是否分配成功'''
        self.menu_role('admin','admin123456')    #进入角色权限界面
        self.driver.find_element_by_css_selector('#table_role tbody tr:last-child td:nth-child(2)').click()   #点击角色列表最后一列角色
#对功能模块进行分配
        #分配地图管理模块、portal总览、图层管理、数据管理模块
        self.driver.find_element_by_css_selector('#table_action_power tbody tr:nth-child(2) td:nth-child(2) span').click()   #点击展开地图管理模块
        sleep(1)
        self.driver.find_element_by_css_selector('#table_action_power tbody tr:nth-child(3) input').click()    #点击勾选共享地图功能
        self.driver.find_element_by_css_selector('#table_action_power tbody tr:nth-child(4) input').click()    #点击勾选删除地图功能
        self.driver.find_element_by_css_selector('#table_action_power tbody tr:nth-child(5) input').click()    #点击勾选添加地图功能
        self.driver.find_element_by_css_selector('#table_action_power tbody tr:nth-child(6) input').click()    #点击勾选打开地图功能
        self.save_img('用户权限功能分配')
        self.add_img()
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(1)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#使用第一大部门下第二小组成员账户登录
        self.login('测试用户角色权限','123')   #使用刚刚新增的角色账户登录
        self.driver.find_element_by_link_text('地图管理').click()   #点击进入地图管理页面
        sleep(1)
        self.driver.find_element_by_id('btn_map_add').click()  #点击上传地图按钮
        self.driver.implicitly_wait(20)
        print('点击创建地图后的操作句柄:',self.driver.window_handles)
        print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])  #切换至创建地图界面
        print('当前操作句柄:',self.driver.current_window_handle)
        #断言是否进入创建地图界面
        link1=self.driver.find_element_by_class_name('layer-title')
        self.assertIn('图层',link1.text)
        self.add_img()


# 用例10:点击角色列表中有用户的角色对应删除按钮,点击确认删除,查看是否提示该角色下有用户,无法删除
    @BeautifulReport.add_test_img('当前角色下存在用户')
    def test_10_delet_role_error(self):
        '''点击角色列表中有用户的角色对应删除按钮,点击确认删除,查看是否提示该角色下有用户,无法删除'''
        self.menu_role('admin','admin123456')    #进入角色权限界面
        self.driver.find_element_by_css_selector('#table_role tbody tr:first-child a:last-child').click()  #点击角色名称最后一列的删除按钮
        sleep(2)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取删除确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认删除
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示编辑成功
        link2=self.driver.find_element_by_id('alter_notify')
        self.assertIn('当前角色下存在用户',link2.text)
        self.add_img()
        self.save_img('有用户,无法删除角色')
        

# 删除角色
# 用例11:点击删除新增角色下的用户,最后点击删除角色,查看是否删除成功
    @BeautifulReport.add_test_img('删除角色')
    def test_11_delete_role(self):
        '''点击删除新增角色下的用户,最后点击删除角色,查看是否删除成功'''
        self.menu_role('admin','admin123456')    #进入角色权限界面
        self.driver.find_element_by_link_text('用户管理').click()  #进入用户管理界面
        sleep(1)
        self.driver.find_element_by_css_selector('#user_table tbody tr:last-child td:last-child span a:last-child').click()   #点击刚刚新增用户的删除按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取删除确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认删除
        sleep(2)
        self.add_img()
        self.driver.find_element_by_link_text('角色权限').click()   #进入角色权限界面
        self.driver.find_element_by_css_selector('#table_role tbody tr:last-child a:last-child').click()  #点击角色名称最后一列的删除按钮
        sleep(2)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取删除确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认删除
        sleep(2)
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link1.text)
        self.add_img()
        self.save_img('删除角色成功') 
        sleep(2)


if __name__ == '__main__':
    unittest.main(argv=['ignored','-v'],exit=False)
    print('')


