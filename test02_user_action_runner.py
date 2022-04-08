''''
用户操作功能测试分为以下情况:
上传头像
(1)上传头像,查看是否上传成功
修改密码
(2)点击修改密码,查看是否弹出修改密码弹窗
(3)在修改密码弹窗所有输入框为空,点击确定,查看是否提示修改失败
(4)在修改密码弹窗输入原密码,其他为空,查看是否提示请输入新密码
(5)在修改密码弹窗输入原密码、新密码,其他为空,查看是否提示两次密码输入不一样
(6)在修改密码弹窗输入原密码、新密码、错误的确认密码,查看是否提示两次输入的密码不一样
(7)在修改密码弹窗输入错误原密码、新密码、正确的确认密码,查看是否提示原密码错误
(8)在修改密码弹窗输入正确原密码、新密码、正确的确认密码,查看是否提示修改成功
(9)使用刚刚修改的账户在登录界面使用原密码登录,查看是否提示用户名或密码错误
(10)使用刚刚修改的账户在登录界面使用新密码登录,查看是否登录成功
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


class test02_User_Action_Case(unittest.TestCase):

    """
    def setUp(self):
        self.dr = webdriver.Edge()

    def tearDown(self):
       self.driver.quit()

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
        # 在是python3.x 中，如果在这里初始化iveriver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
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
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('./用户操作/img'), img_name))    #os.path.abspath('')截图存放路径

  #定义登录方法
    def login(self, username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #登录页面
        sleep(2)
        self.driver.find_element_by_id('input_username').send_keys(username)  #定义用户名
        self.driver.find_element_by_id('input_password').send_keys(password)   #定义密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        sleep(3)
        #显示等待时间到进入系统主界面
        # wait=WebDriverWait(self.driver,40,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
       
# 上传头像
# 用例1：上传头像,查看是否上传成功
    @BeautifulReport.add_test_img('上传头像')
    def test_01_upload_picture(self):
        '''上传头像,查看是否上传成功'''
        self.login('lili', '123') 
        #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        self.driver.find_element_by_id('avatar_user').click()   #点击头像处
        # #鼠标悬停至头像列表处
        # el=self.driver.find_element_by_class_name('nav-user-info')
        # ActionChains(self.driver).move_to_element(el).pause(3).perform()#鼠标悬停在
        sleep(1)
        self.driver.find_element_by_link_text('上传头像').click()
        sleep(2)
#非input框上传文件
        kk = PyKeyboard()
        kk.tap_key(kk.shift_key) #切换为英文，看实际情况是否需要
        sleep(1)
        kk.type_string(os.path.abspath('./images'))#打开文件所在目录，方便多个文件上传
        sleep(1)
        kk.tap_key(kk.enter_key)
        sleep(1)
        kk.type_string( '"3.jpg" ')#多文件上传
        sleep(1)
        kk.tap_key(kk.enter_key) 
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否上传成功
        link1 = self.driver.find_element_by_id('alter_notify')
        self.assertIn('上传成功',link1.text) 
        self.add_img()
        self.save_img('头像上传成功')


# 修改密码
# 用例2：点击修改密码,查看是否弹出修改密码弹窗
    @BeautifulReport.add_test_img('修改密码弹窗')
    def test_02_change_password_page(self):
        '''点击修改密码,查看是否弹出修改密码弹窗'''
        self.login('lili', '123') 
        #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        self.driver.find_element_by_id('avatar_user').click()   #点击头像处
        sleep(1)
        self.driver.find_element_by_link_text('修改密码').click()   #点击修改密码按钮
        #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_password_form'))) 
        #断言是否上传成功
        link1 = self.driver.find_element_by_id('input_password_form')
        self.assertIn('确认密码',link1.text) 
        self.add_img()
        self.save_img('修改密码弹窗')
        sleep(1)

# 用例3：在修改密码弹窗所有输入框为空,点击确定,查看是否提示修改失败
    @BeautifulReport.add_test_img('修改密码输入框为空')
    def test_03_change_password_null(self):
        '''在修改密码弹窗所有输入框为空,点击确定,查看是否提示修改失败'''
        self.login('lili', '123') 
        #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        self.driver.find_element_by_id('avatar_user').click()   #点击头像处
        sleep(1)
        self.driver.find_element_by_link_text('修改密码').click()   #点击修改密码按钮
        #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_password_form'))) 
        sleep(1)
        self.driver.find_element_by_id('btn_password_save').click()   #点击修改按钮
         #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示不能为空
        link1 = self.driver.find_element_by_id('alter_notify')
        self.assertIn('The NewPassword field is required',link1.text) 
        self.add_img()
        self.save_img('修改密码输入框为空')
        sleep(1)

# 用例4：在修改密码弹窗输入原密码,其他为空,查看是否提示请输入新密码
    @BeautifulReport.add_test_img('修改密码输入原密码')
    def test_04_input_passwprd_old(self):
        '''在修改密码弹窗输入原密码,其他为空,查看是否提示请输入新密码'''
        self.login('lili', '123') 
        #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        self.driver.find_element_by_id('avatar_user').click()   #点击头像处
        sleep(1)
        self.driver.find_element_by_link_text('修改密码').click()   #点击修改密码按钮
        #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_password_form'))) 
        self.driver.find_element_by_id('input_passwprd_old').send_keys('123')  #输入原密码
        sleep(2)
        self.driver.find_element_by_id('btn_password_save').click()   #点击修改按钮
         #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示新密码不能为空
        link1 = self.driver.find_element_by_id('alter_notify')
        self.assertIn('The NewPassword field is required.',link1.text) 
        self.add_img()
        self.save_img('修改密码输入原密码')
        sleep(1)

# 用例5：在修改密码弹窗输入原密码、新密码,其他为空,查看是否提示两次密码输入不一样
    @BeautifulReport.add_test_img('修改密码输入新密码')
    def test_05_input_passwprd_new(self):
        '''在修改密码弹窗输入原密码、新密码,其他为空,查看是否提示两次密码输入不一样'''
        self.login('lili', '123') 
        #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        self.driver.find_element_by_id('avatar_user').click()   #点击头像处
        sleep(1)
        self.driver.find_element_by_link_text('修改密码').click()   #点击修改密码按钮
        #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_password_form'))) 
        sleep(1)
        self.driver.find_element_by_id('input_passwprd_old').send_keys('123')  #输入原密码
        sleep(2)
        self.driver.find_element_by_id('input_passwprd_new').send_keys('123456')  #输入新密码
        sleep(2)
        self.driver.find_element_by_id('btn_password_save').click()   #点击修改按钮
         #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示新密码不能为空
        link1 = self.driver.find_element_by_id('alter_notify')
        self.assertIn('两次输入的密码不一致',link1.text) 
        self.add_img()
        self.save_img('修改密码输入新密码')
        sleep(1)

# 用例6：在修改密码弹窗输入原密码、新密码、错误的确认密码,查看是否提示两次输入的密码不一样
    @BeautifulReport.add_test_img('修改密码输入错误确认密码')
    def test_06_input_passwprd_re_error(self):
        '''在修改密码弹窗输入原密码、新密码、错误的确认密码,查看是否提示两次输入的密码不一样'''
        self.login('lili', '123') 
        #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        self.driver.find_element_by_id('avatar_user').click()   #点击头像处
        sleep(1)
        self.driver.find_element_by_link_text('修改密码').click()   #点击修改密码按钮
        #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_password_form'))) 
        sleep(1)
        self.driver.find_element_by_id('input_passwprd_old').send_keys('123')  #输入原密码
        sleep(1)
        self.driver.find_element_by_id('input_passwprd_new').send_keys('123456')  #输入新密码
        sleep(1)
        self.driver.find_element_by_id('input_passwprd_re').send_keys('1234')#输入错误确认密码
        sleep(1)
        self.driver.find_element_by_id('btn_password_save').click()   #点击修改按钮
         #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示新密码不能为空
        link1 = self.driver.find_element_by_id('alter_notify')
        self.assertIn('两次输入的密码不一致',link1.text) 
        self.save_img('修改密码输入错误新密码')
        self.add_img()
        sleep(1)

# 用例7：在修改密码弹窗输入错误原密码、新密码、正确的确认密码,查看是否提示原密码错误
    @BeautifulReport.add_test_img('修改密码输入错误原密码')
    def test_07_input_passwprd_old_error(self):
        '''在修改密码弹窗输入错误原密码、新密码、正确的确认密码,查看是否提示原密码错误'''
        self.login('lili', '123') 
        #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        self.driver.find_element_by_id('avatar_user').click()   #点击头像处
        sleep(1)
        self.driver.find_element_by_link_text('修改密码').click()   #点击修改密码按钮
        #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_password_form'))) 
        sleep(1)
        self.driver.find_element_by_id('input_passwprd_old').send_keys('12')  #输入原密码
        sleep(1)
        self.driver.find_element_by_id('input_passwprd_new').send_keys('123456')  #输入新密码
        sleep(1)
        self.driver.find_element_by_id('input_passwprd_re').send_keys('123456')    #输入确认密码
        sleep(1)
        self.driver.find_element_by_id('btn_password_save').click()   #点击修改按钮
         #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示新密码不能为空
        link1 = self.driver.find_element_by_id('alter_notify')
        self.assertIn('原密码不正确',link1.text) 
        sleep(1)
        self.save_img('修改密码输入错误原密码')
        self.add_img()
        sleep(1)
 
# 用例8：在修改密码弹窗输入正确原密码、新密码、正确的确认密码,查看是否提示修改成功
    @BeautifulReport.add_test_img('修改密码成功')
    def test_08_change_passwprd_access(self):
        '''在修改密码弹窗输入正确原密码、新密码、正确的确认密码,查看是否提示修改成功'''
        self.login('lili', '123') 
        #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        self.driver.find_element_by_id('avatar_user').click()   #点击头像处
        sleep(1)
        self.driver.find_element_by_link_text('修改密码').click()   #点击修改密码按钮
        #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_password_form'))) 
        sleep(1)
        self.driver.find_element_by_id('input_passwprd_old').send_keys('123')  #输入原密码
        sleep(1)
        self.driver.find_element_by_id('input_passwprd_new').send_keys('123456')  #输入新密码
        sleep(1)
        self.driver.find_element_by_id('input_passwprd_re').send_keys('123456')    #输入确认密码
        sleep(1)
        self.driver.find_element_by_id('btn_password_save').click()   #点击修改按钮
         #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言是否提示新密码修改成功
        link1 = self.driver.find_element_by_id('alter_notify')
        self.assertIn('修改成功',link1.text) 
        sleep(1)
        self.save_img('修改密码成功')
        self.add_img()
        sleep(1)

# 用例9：使用刚刚修改的账户在登录界面使用原密码登录,查看是否提示用户名或密码错误
    @BeautifulReport.add_test_img('原密码无法登录')
    def test_09_use_old_passwprd(self):
        '''使用刚刚修改的账户在登录界面使用原密码登录,查看是否提示用户名或密码错误'''
        self.login('lili', '123') 
         #断言是否提示用户名或密码不正确
          #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1 = self.driver.find_element_by_id('alter_notify')
        self.assertIn('用户名或密码不正确',link1.text) 
        sleep(1)
        self.save_img('原密码无法登录')
        self.add_img()
        sleep(2)

# 用例10：使用刚刚修改的账户在登录界面使用新密码登录,查看是否登录成功
    @BeautifulReport.add_test_img('修改密码登录成功')
    def test_10_use_new_passwprd(self):
        '''使用刚刚修改的账户在登录界面使用新密码登录,查看是否登录成功'''
        self.login('lili', '123456') 
        #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        link1 = self.driver.find_element_by_id('navbarNav')
        self.assertIn('菜单', link1.text)
        self.add_img()
        self.save_img('修改密码登录成功')
        sleep(2)
#将密码修改回去
        self.driver.find_element_by_id('avatar_user').click()   #点击头像处
        sleep(1)
        self.driver.find_element_by_link_text('修改密码').click()   #点击修改密码按钮
        #显示等待时间直到出现弹窗
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_password_form'))) 
        sleep(1)
        self.driver.find_element_by_id('input_passwprd_old').send_keys('123456')  #输入原密码
        sleep(1)
        self.driver.find_element_by_id('input_passwprd_new').send_keys('123')  #输入新密码
        sleep(1)
        self.driver.find_element_by_id('input_passwprd_re').send_keys('123')    #输入确认密码
        sleep(1)
        self.driver.find_element_by_id('btn_password_save').click()   #点击修改按钮
        sleep(1)
         #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link2= self.driver.find_element_by_id('alter_notify')
        self.assertIn('修改成功',link2.text) 
        self.add_img()


if __name__ == '__main__':
    unittest.main(argv=['ignored','-v'],exit=False)
    print('')


