''''
数据共享功能测试分为以下情况：
用例1:进入数据管理界面,查看上传新增的数据是否有共享按钮
用例2:点击测试数据对应的共享按钮,查看是否弹出共享部门选择弹窗
用例3:在共享弹窗中不选择部门,点击保存,查看是否提示请选择部门
用例4:在共享弹窗中选择一级部门,权限选择读,点击保存,查看是否保存成功(用该部门下的测试用户重新登录查看能否查看共享的数据)
用例5:在共享弹窗中选择一级部门,权限选择写,点击保存,查看是否保存成功(用该部门下的测试用户重新登录查看能否编辑共享的数据)
用例6:在共享弹窗中选择二级部门,权限选择读,点击保存,查看是否保存成功(用该部门下的测试用户重新登录查看能否查看共享的数据)
用例7:在共享弹窗中选择二级部门,权限选择写,点击保存,查看是否保存成功(用该部门下的测试用户重新登录查看能否编辑共享的数据)
我的共享
用例8:通过用例4-7共享的数据,点击我的共享页面,查看能否正常进入我的共享页面
用例9:在我的共享页面对刚刚共享的数据分别进行取消共享,查看登录后还能否查看或编辑数据
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





class test09_data_share_Case(unittest.TestCase):

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
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('./数据共享/img'), img_name))    #os.path.abspath('')截图存放路径

#定义登录方法进入功能配置界面
    def menu_data_share(self,username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys(username)  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys(password)  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        sleep(3)
        # #显示等待时间到进入系统主界面
        # wait=WebDriverWait(self.driver,40,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        # self.driver.find_element_by_link_text('系统设置').click()   #点击系统设置按钮
        # self.driver.implicitly_wait(2)   #隐式等待2秒
        # self.driver.find_element_by_link_text('功能配置').click()   #点击用户管理按钮
        # self.driver.implicitly_wait(2)   #隐式等待2秒  

# 用例1:进入数据管理界面,查看上传新增的数据是否有共享按钮
    @BeautifulReport.add_test_img('共享数据按钮')
    def test_01_data_share_page(self):
        '''进入数据管理界面,查看上传新增的数据是否有共享按钮'''
        self.menu_data_share('admin','admin123456')    #进入系统主界面
        self.driver.find_element_by_link_text('数据管理').click()   #点击数据管理按钮
        sleep(2)
        #显示等待时间到进入数据管理主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_data_upload'))) 
        link1=self.driver.find_element_by_css_selector('#data_table tbody tr:last-child td:last-child  a:nth-last-child(3)')   #定位数据列表最后一列的共享位置
        self.assertIn('共享',link1.text)
        self.add_img()
        self.save_img('数据共享按钮')
       
# 用例2:点击测试数据对应的共享按钮,查看是否弹出共享部门选择弹窗
    @BeautifulReport.add_test_img('共享数据按钮')
    def test_02_data_share_pop(self):
        '''点击测试数据对应的共享按钮,查看是否弹出共享部门选择弹窗'''
        self.menu_data_share('admin','admin123456')    #进入系统主界面
        self.driver.find_element_by_link_text('数据管理').click()   #点击数据管理按钮
        sleep(1)
        self.driver.find_element_by_css_selector('#data_table tbody tr:last-child td:last-child  a:nth-last-child(3)').click()   #点击数据列表最后一列的共享按钮
        sleep(2)
        #断言是否弹出弹窗
        link1=self.driver.find_element_by_css_selector('#modal_share  h5')   
        self.assertIn('共享',link1.text)
        self.add_img()
        self.save_img('共享数据弹窗')

# 用例3:在共享弹窗中不选择部门,点击保存,查看是否提示请选择部门
    @BeautifulReport.add_test_img('共享数据部门为空')
    def test_03_table_share_department_null(self):
        '''在共享弹窗中不选择部门,点击保存,查看是否提示请选择部门'''
        self.menu_data_share('admin','admin123456')    #进入系统主界面
        self.driver.find_element_by_link_text('数据管理').click()   #点击数据管理按钮
        sleep(1)
        self.driver.find_element_by_css_selector('#data_table tbody tr:last-child td:last-child  a:nth-last-child(3)').click()   #点击数据列表最后一列的共享按钮
        sleep(2)
        self.add_img()
        self.driver.find_element_by_id('btn_share_save').click()  #点击保存按钮
          #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
         #断言是否提示编辑成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('请选择要分享的部门',link1.text)
        self.add_img()
        self.save_img('共享数据部门为空')
       
# 用例4:在共享弹窗中选择一级部门,权限选择读,点击保存,查看是否保存成功(用该部门下的测试用户重新登录查看能否查看共享的数据)
    @BeautifulReport.add_test_img('共享一级部门读数据')
    def test_04_share_first_department_read(self):
        '''在共享弹窗中选择一级部门,权限选择读,点击保存,查看是否保存成功'''
        self.menu_data_share('admin','admin123456')    #进入系统主界面
        self.driver.find_element_by_link_text('数据管理').click()   #点击数据管理按钮
        sleep(1)
        self.driver.find_element_by_css_selector('#data_table tbody tr:first-child td:last-child  a:nth-last-child(3)').click()   #点击数据列表第一列的共享按钮
        sleep(2)
        self.driver.find_element_by_css_selector('#table_share_department tbody tr:nth-child(1) td:first-child').click()   #点击选择第一大部门
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_share_save').click()  #点击保存按钮
        #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('共享成功',link1.text)
        self.add_img()
        self.save_img('共享一级部门读数据成功')
#使用刚刚共享的部门下面账户登录查看能否查看数据
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#使用第一大部门下第一小组成员账户登录
        self.menu_data_share('ywyz','123')    #使用第一大部门下第一小组成员账户登录
        self.driver.find_element_by_link_text('数据管理').click()  #点击进入数据管理界面
        sleep(1)
        #验证数据名称是否为共享的数据名称
        link2=self.driver.find_element_by_css_selector('#data_table tbody  tr:first-child  td:nth-child(2)')   #定位数据列表最后一列数据名称位置
        self.assertIn('polyline1',link2.text)   #验证数据名称是否为共享的数据名称
        #验证数据列表操作是否只包含读的操作
        link3=self.driver.find_element_by_css_selector('#data_table tbody tr:first-child td:nth-child(9) span')   #定位操作模块
        self.assertIn('预览 发布',link3.text)
        self.add_img()
        self.save_img('验证共享一级部门读数据')
#使用第一大部门下第二小组成员账户登录
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
        #使用第一大部门下第二小组成员账户登录
        self.menu_data_share('ywez','123')    #使用第一大部门下第一小组成员账户登录
        self.driver.find_element_by_link_text('数据管理').click()  #点击进入数据管理界面
        sleep(1)
        #验证数据名称是否为共享的数据名称
        link2=self.driver.find_element_by_css_selector('#data_table tbody  tr:first-child  td:nth-child(2)')   #定位数据列表最后一列数据名称位置
        self.assertIn('polyline1',link2.text)   #验证数据名称是否为共享的数据名称
        self.add_img()
        #验证数据列表操作是否只包含读的操作
        link3=self.driver.find_element_by_css_selector('#data_table tbody tr:first-child td:nth-child(9) span')   #定位操作模块
        self.assertIn('预览 发布',link3.text)

# 用例5:在共享弹窗中选择一级部门,权限选择写,点击保存,查看是否保存成功(用该部门下的测试用户重新登录查看能否编辑共享的数据)
    @BeautifulReport.add_test_img('共享一级部门写数据')
    def test_05_share_first_department_write(self):
        '''在共享弹窗中选择一级部门,权限选择写,点击保存,查看是否保存成功'''
        self.menu_data_share('admin','admin123456')    #进入系统主界面
        self.driver.find_element_by_link_text('数据管理').click()   #点击数据管理按钮
        sleep(1)
        self.driver.find_element_by_css_selector('#data_table tbody tr:first-child td:last-child  a:nth-last-child(3)').click()   #点击数据列表第一列的共享按钮
        sleep(2)
        self.driver.find_element_by_css_selector('#table_share_department tbody tr:nth-child(1) td:first-child').click()   #点击选择第一大部门
        sleep(1)
        self.add_img()
        self.driver.find_element_by_css_selector('#input_share_form div div label:nth-child(2) span').click()   #点击写按钮
        self.driver.find_element_by_id('btn_share_save').click()  #点击保存按钮
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('共享成功',link1.text)
        self.add_img()
        self.save_img('共享一级部门读写数据成功')
#使用刚刚共享的部门下面账户登录查看能否查看数据
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#使用第一大部门下第一小组成员账户登录
        self.menu_data_share('ywyz','123')    #使用第一大部门下第一小组成员账户登录
        self.driver.find_element_by_link_text('数据管理').click()  #点击进入数据管理界面
        sleep(1)
        #验证数据名称是否为共享的数据名称
        link2=self.driver.find_element_by_css_selector('#data_table tbody  tr:first-child  td:nth-child(2)')   #定位数据列表最后一列数据名称位置
        self.assertIn('polyline1',link2.text)   #验证数据名称是否为共享的数据名称
        #验证数据列表操作是否只包含读的操作
        link3=self.driver.find_element_by_css_selector('#data_table tbody tr:first-child td:nth-child(9) span')   #定位操作模块
        self.assertIn('预览 发布 删除',link3.text)
        self.add_img()
        self.save_img('验证共享一级部门写数据')
#使用第一大部门下第二小组成员账户登录
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
        #使用第一大部门下第二小组成员账户登录
        self.menu_data_share('ywez','123')    #使用第一大部门下第一小组成员账户登录
        self.driver.find_element_by_link_text('数据管理').click()  #点击进入数据管理界面
        sleep(1)
        #验证数据名称是否为共享的数据名称
        link2=self.driver.find_element_by_css_selector('#data_table tbody  tr:first-child  td:nth-child(2)')   #定位数据列表最后一列数据名称位置
        self.assertIn('polyline1',link2.text)   #验证数据名称是否为共享的数据名称
        #验证数据列表操作是否只包含读的操作
        link3=self.driver.find_element_by_css_selector('#data_table tbody tr:first-child td:nth-child(9) span')   #定位操作模块
        self.assertIn('预览 发布 删除',link3.text)
        self.add_img()

# 用例6:在共享弹窗中选择二级部门,权限选择读,点击保存,查看是否保存成功(用该部门下的测试用户重新登录查看能否查看共享的数据)
    @BeautifulReport.add_test_img('共享二级部门写数据')
    def test_06_share_second_department_read(self):
        '''在共享弹窗中选择二级部门,权限选择读,点击保存,查看是否保存成功'''
        self.menu_data_share('admin','admin123456')    #进入系统主界面
        self.driver.find_element_by_link_text('数据管理').click()   #点击数据管理按钮
        sleep(1)
        self.driver.find_element_by_css_selector('#data_table tbody tr:nth-child(2) td:last-child  a:nth-last-child(3)').click()   #点击数据列表第二列的共享按钮
        sleep(2)
        self.driver.find_element_by_css_selector('#table_share_department tbody  tr:first-child td:last-child span ').click()  #点击一级部门展开按钮
        sleep(1)
        self.driver.find_element_by_css_selector('#table_share_department tbody  tr:nth-child(3) td:first-child input').click()   #点击一级部门下的二级小组按钮  
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_share_save').click()  #点击保存按钮
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('共享成功',link1.text)
        self.add_img()
        self.save_img('共享二级部门读数据成功')
#使用刚刚共享的部门下面账户登录查看能否查看数据
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#使用第一大部门下第二小组成员账户登录
        self.menu_data_share('ywez','123')    #使用第一大部门下第二小组成员账户登录
        self.driver.find_element_by_link_text('数据管理').click()  #点击进入数据管理界面
        sleep(1)
        #验证数据名称是否为共享的数据名称
        link2=self.driver.find_element_by_css_selector('#data_table tbody  tr:nth-child(2)  td:nth-child(2)')   #定位数据列表最后一列数据名称位置
        self.assertIn('polyline2',link2.text)   #验证数据名称是否为共享的数据名称
        #验证数据列表操作是否只包含读的操作
        link3=self.driver.find_element_by_css_selector('#data_table tbody tr:nth-child(2) td:nth-child(9) span')   #定位操作模块
        self.assertIn('预览 发布',link3.text)
        self.add_img()
        self.save_img('验证共享二级部门读数据')
#使用刚刚共享的另一部门下面账户登录查看能否查看数据
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#使用第一大部门下第一小组成员账户登录
        self.menu_data_share('ywyz','123')    #使用第一大部门下第二小组成员账户登录
        self.driver.find_element_by_link_text('数据管理').click()  #点击进入数据管理界面
        sleep(1)
        #验证数据名称是否为共享的数据名称
        link2=self.driver.find_element_by_css_selector('#data_table tbody  tr:first-child  td:nth-child(2)')   #定位数据列表最后一列数据名称位置
        self.assertIn('polyline1',link2.text)   #验证数据名称是否为共享的数据名称
        self.add_img()
        
# 用例7:在共享弹窗中选择二级部门,权限选择写,点击保存,查看是否保存成功(用该部门下的测试用户重新登录查看能否编辑共享的数据)
    @BeautifulReport.add_test_img('共享二级部门写数据')
    def test_07_share_second_department_write(self):
        '''在共享弹窗中选择二级部门,权限选择写,点击保存,查看是否保存成功'''
        self.menu_data_share('admin','admin123456')    #进入系统主界面
        self.driver.find_element_by_link_text('数据管理').click()   #点击数据管理按钮
        sleep(1)
        self.driver.find_element_by_css_selector('#data_table tbody tr:nth-child(2) td:last-child  a:nth-last-child(3)').click()   #点击数据列表第二列的共享按钮
        sleep(2)
        self.driver.find_element_by_css_selector('#table_share_department tbody  tr:first-child td:last-child span ').click()  #点击一级部门展开按钮
        sleep(1)
        self.driver.find_element_by_css_selector('#table_share_department tbody  tr:nth-child(3) td:first-child input').click()   #点击一级部门下的二级小组按钮  
        sleep(1)
        self.driver.find_element_by_css_selector('#input_share_form div div label:nth-child(2) span').click()   #点击写按钮
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_share_save').click()  #点击保存按钮
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('共享成功',link1.text)
        self.add_img()
        self.save_img('共享二级部门写数据成功')
#使用刚刚共享的部门下面账户登录查看能否查看数据
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#使用第一大部门下第二小组成员账户登录
        self.menu_data_share('ywez','123')    #使用第一大部门下第二小组成员账户登录
        self.driver.find_element_by_link_text('数据管理').click()  #点击进入数据管理界面
        sleep(1)
        #验证数据名称是否为共享的数据名称
        link2=self.driver.find_element_by_css_selector('#data_table tbody  tr:nth-child(2)  td:nth-child(2)')   #定位数据列表最后一列数据名称位置
        self.assertIn('polyline2',link2.text)   #验证数据名称是否为共享的数据名称
        #验证数据列表操作是否只包含读的操作
        link3=self.driver.find_element_by_css_selector('#data_table tbody tr:nth-child(2) td:nth-child(9) span')   #定位操作模块
        self.assertIn('预览 发布 删除',link3.text)
        self.add_img()
        self.save_img('验证共享二级部门写数据')
#使用刚刚共享的另一部门下面账户登录查看能否查看数据
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#使用第一大部门下第一小组成员账户登录
        self.menu_data_share('ywyz','123')    #使用第一大部门下第二小组成员账户登录
        self.driver.find_element_by_link_text('数据管理').click()  #点击进入数据管理界面
        sleep(1)
        #验证数据名称是否为共享的数据名称
        link2=self.driver.find_element_by_css_selector('#data_table tbody  tr:first-child  td:nth-child(2)')   #定位数据列表最后一列数据名称位置
        self.assertIn('polyline1',link2.text)   #验证数据名称是否为共享的数据名称
        self.add_img()
  
# 我的共享
# 用例8:通过用例4-7共享的数据,点击我的共享页面,查看能否正常进入我的共享页面
    @BeautifulReport.add_test_img('我的共享页面')
    def test_08_share_page(self):
        '''在共享弹窗中选择二级部门,权限选择写,点击保存,查看是否保存成功'''
        self.menu_data_share('admin','admin123456')    #进入系统主界面
        self.driver.find_element_by_link_text('我的共享').click()   #点击我的共享界面
        sleep(3)
        link1=self.driver.find_element_by_id('table_share')
        self.assertIn('资源名称',link1.text)
        self.add_img()
        self.save_img('我的共享界面')

# 用例9:在我的共享页面对刚刚共享的数据分别进行取消共享,查看登录后还能否查看或编辑数据
    @BeautifulReport.add_test_img('取消共享')
    def test_09_delete_share(self):
        '''在我的共享页面对刚刚共享的数据分别进行取消共享,查看登录后还能否查看或编辑数据'''
        self.menu_data_share('admin','admin123456')    #进入系统主界面
        sleep(1)
        self.driver.find_element_by_link_text('我的共享').click()   #点击我的共享界面
        sleep(2)
#取消共享
        self.driver.find_element_by_css_selector('#table_share tbody tr:first-child a').click()  #点击第一列的取消共享按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取取消确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认取消
        sleep(2)
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('取消共享成功', link1.text)
        self.add_img()
        self.save_img('取消共享成功') 
        sleep(2)
#取消测试共享数据
        self.driver.find_element_by_css_selector('#table_share tbody tr:first-child a').click()  #点击第一列的取消共享按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取取消确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认取消
        sleep(1)
#
        self.driver.find_element_by_css_selector('#table_share tbody tr:first-child a').click()  #点击第一列的取消共享按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取取消确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认取消
        sleep(1)
        self.add_img()
#
        self.driver.find_element_by_css_selector('#table_share tbody tr:first-child a').click()  #点击第一列的取消共享按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取取消确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认取消
        sleep(1)
        self.add_img()
#使用测试共享部门的账户登录查看是否还存在刚刚共享的数据
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#使用第一大部门下第二小组成员账户登录
        self.menu_data_share('ywyz','123')    #使用第一大部门下第二小组成员账户登录
        self.driver.find_element_by_link_text('数据管理').click()  #点击进入数据管理界面
        sleep(1)
        #验证数据名称是否为共享的数据名称
        link2=self.driver.find_element_by_css_selector('#data_table tbody  tr:last-child  td:nth-child(2)')   #定位数据列表最后一列数据名称位置
        self.assertIn('point',link2.text)   #验证数据名称是否为共享的数据名称
        self.add_img()
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#使用第一大部门下第二小组成员账户登录
        self.menu_data_share('ywez','123')    #使用第一大部门下第二小组成员账户登录
        self.driver.find_element_by_link_text('数据管理').click()  #点击进入数据管理界面
        sleep(1)
        #验证数据名称是否为共享的数据名称
        link3=self.driver.find_element_by_css_selector('#data_table tbody  tr:last-child  td:nth-child(2)')   #定位数据列表最后一列数据名称位置
        self.assertIn('point',link3.text)   #验证数据名称是否为共享的数据名称
        self.add_img()
        
   

if __name__ == '__main__':
    unittest.main(argv=['ignored','-v'],exit=False)
    print('')


