'''
登录测试，分下面几种情况：
(1)用户名、密码正确
(2)用户名正确、密码不正确
(3)用户名正确、密码为空
(4)用户名错误、密码正确
(5)用户名为空、密码正确
(6)用户名为空、密码为空
(7)退出登录、回到主界面
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
from HTMLTestRunnerCN import HTMLTestRunner


class test01_LoginCase(unittest.TestCase):
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
        # self.driver = webdriver.Edge()
        # self.driver.maximize_window()
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs = []
        self.addCleanup(self.cleanup)
      
    # def tearDown(self):
    #     sleep(2)
    #     print('测试完成')
    #     self.driver.quit()

    def cleanup(self):
        pass

#定义错误截图方法
    def save_img(self, img_name):  
        """
         传入一个img_name, 并存储到默认的文件路径下img
         :param img_name:
          :return:
         """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('./登录/img'), img_name))    #os.path.abspath('')截图存放路径


    #定义登录方法
    def login(self, username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #登录页面
        sleep(2)
        self.driver.find_element_by_id('input_username').send_keys(username)  #定义用户名
        self.driver.find_element_by_id('input_password').send_keys(password)   #定义密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        sleep(3)
        # #显示等待时间到进入系统主界面
        # wait=WebDriverWait(self.driver,40,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 

    #定义登录成功退出登录
    def logout(self,username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #登录页面
        sleep(2)
        self.driver.find_element_by_id('input_username').send_keys(username)  #定义用户名
        self.driver.find_element_by_id('input_password').send_keys(password)   #定义密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        sleep(2)
         #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        # self. Explicit_Waits(By.ID,'navbarNav')   #显示等待时间到进入系统主界面
        self.driver.find_element_by_id('navbarDropdownMenuLink2').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('navbarDropdownMenuLink2')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
       
       
    #登录测试
    @BeautifulReport.add_test_img('登录成功')
    def test_01_login_success(self):
        '''用户名、密码正确'''
        self.login('admin', 'admin123456')  
        #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        # self. Explicit_Waits(By.ID,'navbarNav')   #显示等待时间到进入系统主界面
        link1 = self.driver.find_element_by_id('navbarNav')
        self.assertIn('菜单', link1.text)
        self.add_img()
        self.save_img('登录成功')   
        # self.driver.close()

       


    @BeautifulReport.add_test_img('密码不正确')
    def test_02_login_pwd_error(self):
        '''用户名正确、密码不正确'''
        self.login('admin', '123456') 
         #显示等待时间到出现报错提醒
        link2 = self.driver.find_element_by_id('alter_notify')
        self.assertEqual(link2.text,'用户名或密码不正确') 
        self.add_img()
        self.save_img('密码不正确')
        sleep(1)
       

    @BeautifulReport.add_test_img('密码为空')
    def test_03_login_pwd_null(self):
        '''用户名正确、密码为空'''
        self.login('admin', '') 
         #显示等待时间到出现报错提醒
        link3 = self.driver.find_element_by_id('alter_notify')
        self.assertEqual(link3.text,'请输入用户名和密码') 
        self.add_img()
        self.save_img('密码为空')
        sleep(1)
        
    @BeautifulReport.add_test_img('用户名错误')
    def test_04_login_user_error(self):
        '''用户名错误、密码正确'''
        self.login('17371294396', 'admin123456') 
         #显示等待时间到出现报错提醒
        # wait=WebDriverWait(self.driver,40,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        # self. Explicit_Waits(By.ID,'alter_notify')#显示等待时间到出现报错提醒
        link4 = self.driver.find_element_by_id('alter_notify')
        self.assertEqual(link4.text,'用户名或密码不正确') 
        self.add_img()
        self.save_img('用户名错误')
        sleep(1)
    

    @BeautifulReport.add_test_img('用户名为空')
    def test_05_login_user_null(self):
        '''用户名为空、密码正确'''
        self.login('', 'admin123456') 
         #显示等待时间到出现报错提醒
        # wait=WebDriverWait(self.driver,40,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        # # self. Explicit_Waits(By.ID,'alter_notify')#显示等待时间到出现报错提醒
        link5 = self.driver.find_element_by_id('alter_notify')
        self.assertEqual(link5.text,'请输入用户名和密码') 
        self.add_img()
        self.save_img('用户名为空')
        
       

    @BeautifulReport.add_test_img('都为空')
    def test_06_login_all_null(self):
        '''用户名为空、密码为空'''
        self.login('', '')  
         #显示等待时间到出现报错提醒
        # wait=WebDriverWait(self.driver,40,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link6 = self.driver.find_element_by_id('alter_notify')
        self.assertEqual(link6.text,'请输入用户名和密码') 
        #self.assertIn('账号或密码不正确！', link2.text)  #用assertIn(a,b)方法来断言 a in b  '用户名或密码错误'在error_message里
        # self.driver.get_screenshot_as_file("C:/Users/ZAssitant/Desktop/Geoportal/登录/img/all_null.png")
        self.add_img()
        self.save_img('都为空')
        
     


    #'''需要修改的地方'''
    @BeautifulReport.add_test_img('退出登录')
    def test_07_Logout_success(self):
        '''退出登录'''
        self.logout('admin', 'admin123456') #正确用户名和密码
         #显示等待时间直到回到登录界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_login'))) 
        # self. Explicit_Waits(By.ID,'btn_login')#显示等待时间直到回到登录界面
        link7 = self.driver.find_element_by_id('btn_login')  #断言是否退出登录回到登录界面
        self.assertEqual(link7.text,'登录') 
        self.add_img()
        self.save_img('退出登录')
        
  

      


if __name__ == '__main__':
    unittest.main(argv=['ignored','-v'],exit=False)
    print('')




