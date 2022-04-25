'''
参数配置功能测试,分为以下几种情况:
(1)进入系统点击参数配置,界面自动跳转至参数配置界面
(2)对参数配置界面中的GeoServerd的【URL】输入栏进行修改,刷新页面,查看修改部分是否保存
(3)对参数配置界面中的GeoServerd的【工作区】输入栏进行修改,刷新页面,查看修改部分是否保存
(4)对参数配置界面中的GeoServerd的【用户名】输入栏进行修改,刷新页面,查看修改部分是否保存
(5)对参数配置界面中的GeoServerd的【密码】输入栏进行修改,刷新页面,查看修改部分是否保存
(6)对参数配置界面中的GeoServerd的【数据存储】输入栏进行修改,刷新页面,查看修改部分是否保存
(7)对参数配置界面中的PostGIS的【主机】输入栏进行修改,刷新页面,查看修改部分是否保存
(8)对参数配置界面中的PostGIS的【端口号】输入栏进行修改,刷新页面,查看修改部分是否保存
(9)对参数配置界面中的PostGIS的【数据库】输入栏进行修改,刷新页面,查看修改部分是否保存
(10)对参数配置界面中的PostGIS的【用户名】输入栏进行修改,刷新页面,查看修改部分是否保存
(11)对参数配置界面中的PostGIS的【密码】输入栏进行修改,刷新页面,查看修改部分是否保存
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
from selenium.webdriver.common.keys import Keys


class test04_ParameterCase(unittest.TestCase):

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
    
    #封装的显示等待时间
    def Explicit_Waits(driver,way,path):
 
        try:
              ele = WebDriverWait(driver,40).until(EC.presence_of_element_located((way,path)))
              return ele
        
        except Exception as e:
              print('元素寻找失败： '+str(e)) 

#定义错误截图方法
    def save_img(self, img_name):  
        """
         传入一个img_name, 并存储到默认的文件路径下
         :param img_name:
          :return:
         """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('./参数配置/img'), img_name))    #os.path.abspath('')截图存放路径

        # root_dir=os.path.dirname(os.path.dirname(os.path.abspath('./参数配置/csimg'))).replace('\\','/')
        # img_path=root_dir+'/img'
        #  self.driver.get_screenshot_as_file\
        #     ('{}/{}.png'.format(img_path, test_method))
         
#打开浏览器至参数配置界面
    def Interface(self,username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys(username)  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys(password)  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        # #iver显示等待时间到进入系统主界面
        # wait=WebDriverWait(self.driver,40,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        sleep(3)
        self.driver.find_element_by_link_text('系统设置').click()   #点击系统设置按钮
        sleep(1)
        self.driver.find_element_by_link_text('参数配置').click()   #点击参数配置按钮
        sleep(1)

#用例1：进入系统点击参数配置,界面自动跳转至参数配置界面
#已验证成功
    @BeautifulReport.add_test_img('参数配置i') 
    def test_01_interface(self):
        '''界面进入参数配置界面'''
        self.Interface('admin','admin123456')    #进入参数配置界面
        #显示等待时间到进入参数配置主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'page_s_config'))) 
        link1=self.driver.find_element_by_id('page_s_config')
        self.assertIn('配置GeoServer服务相关参数', link1.text)
        self.add_img()
        self.save_img('参数配置') 
        sleep(2)

#用例2：对参数配置界面中的GeoServerd的【URL】输入栏进行修改,刷新页面,查看修改部分是否保存
#已验证成功 
    @BeautifulReport.add_test_img('修改URL')
    def test_02_url(self):
        '''修改GeoServer的【URL】'''
        self.Interface('admin','admin123456')                         #进入参数配置界面
        el=self.driver.find_element_by_id('input_geoserver_url')          #定位输入框
        el.send_keys(Keys.CONTROL,'a')                                #全选输入框内容
        el.send_keys(Keys.BACK_SPACE)                                 #删除全选的输入框内容
        sleep(1)
        el.send_keys(Keys.ENTER)                                      #键入enter键
        #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('不可为空', link1.text)                          #验证提示框是否提示输入框不可为空
        self.add_img()
        self.save_img('参数为空2') 
        sleep(2)
        el.send_keys('http://192.168.0.107:8080/geoserver')          #在输入框中输入内容
        sleep(1)
        el.send_keys(Keys.ENTER)                                      #在输入框中修改之后按enter键保存
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link2=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('修改成功', link2.text)                          #验证提示框是否提示修改成功
        self.add_img()
        self.save_img('修改URL') 
        sleep(2)


#用例3：对参数配置界面中的GeoServerd的【工作区】输入栏进行修改,刷新页面,查看修改部分是否保存
#工作区自动生成，不用修改
    @BeautifulReport.add_test_img('修改工作区')
    def test_03_workspaceL(self):
        '''修改GeoServer的【工作区】'''
        self.Interface('admin','admin123456')                         #进入参数配置界面
        el=self.driver.find_element_by_id('input_geoserver_workspace')          #定位输入框
        el.send_keys(Keys.CONTROL,'a')                                #全选输入框内容
        el.send_keys(Keys.BACK_SPACE)                                 #删除全选的输入框内容
        sleep(1) 
        el.send_keys(Keys.ENTER)                                      #键入enter键
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('不可为空', link1.text)                          #验证提示框是否提示输入框不可为空
        self.add_img()
        self.save_img('参数为空3') 
        sleep(2)
        el.send_keys('map')                                           #在输入框中输入内容
        sleep(1)
        el.send_keys(Keys.ENTER)                                      #在输入框中修改之后按enter键保存
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link3=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('修改成功', link3.text)                          #验证提示框是否提示修改成功
        self.add_img()
        self.save_img('修改工作区') 
        sleep(2)

#用例4：对参数配置界面中的GeoServerd的【用户名】输入栏进行修改,刷新页面,查看修改部分是否保存
    @BeautifulReport.add_test_img('修改用户名')
    def test_04_user(self):
        '''修改GeoServer的【用户名】'''
        self.Interface('admin','admin123456')                         #进入参数配置界面
        el=self.driver.find_element_by_id('input_geoserver_user')          #定位输入框
        el.send_keys(Keys.CONTROL,'a')                                #全选输入框内容
        el.send_keys(Keys.BACK_SPACE)                                 #删除全选的输入框内容
        sleep(1) 
        el.send_keys(Keys.ENTER)                                      #键入enter键
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('不可为空', link1.text)                          #验证提示框是否提示输入框不可为空
        self.add_img()
        self.save_img('参数为空4') 
        sleep(2)
        el.send_keys('admin')                                         #在输入框中输入内容
        sleep(1)
        el.send_keys(Keys.ENTER)                                      #在输入框中修改之后按enter键保存
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link4=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('修改成功', link4.text)                          #验证提示框是否提示修改成功
        self.add_img()
        self.save_img('修改用户名') 
        sleep(2)

#用例5：对参数配置界面中的GeoServerd的【密码】输入栏进行修改,刷新页面,查看修改部分是否保存
    @BeautifulReport.add_test_img('修改密码')
    def test_05_password(self):
        '''修改GeoServer的【密码】'''
        self.Interface('admin','admin123456')                         #进入参数配置界面
        el=self.driver.find_element_by_id('input_geoserver_password')          #定位输入框
        el.send_keys(Keys.CONTROL,'a')                                #全选输入框内容
        el.send_keys(Keys.BACK_SPACE)                                 #删除全选的输入框内容
        sleep(1) 
        el.send_keys(Keys.ENTER)                                      #键入enter键
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('不可为空', link1.text)                          #验证提示框是否提示输入框不可为空
        self.add_img()
        self.save_img('参数为空5') 
        sleep(2)
        el.send_keys('geoserver')                                   #在输入框中输入内容
        sleep(1)
        el.send_keys(Keys.ENTER)                                      #在输入框中修改之后按enter键保存
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link5=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('修改成功', link5.text)                          #验证提示框是否提示修改成功
        self.add_img()
        self.save_img('修改密码') 
        sleep(2)

# 用例6：对参数配置界面中的GeoServerd的【数据存储】输入栏进行修改,刷新页面,查看修改部分是否保存
# 数据存储自动生成
    @BeautifulReport.add_test_img('修改数据存储')
    def test_06_datastore(self):
        '''修改GeoServer的【数据存储】'''
        self.Interface('admin','admin123456')                         #进入参数配置界面
        el=self.driver.find_element_by_id('input_geoserver_datastore')    #定位输入框
        # el.send_keys(Keys.CONTROL,'a')                                #全选输入框内容
        # el.send_keys(Keys.BACK_SPACE)                                 #删除全选的输入框内容
        el.clear() 
        sleep(1)                                                     #清除输入框
        el.send_keys(Keys.ENTER)                                      #键入enter键
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('不可为空', link1.text)                          #验证提示框是否提示输入框不可为空
        self.add_img()
        self.save_img('参数为空6') 
        sleep(2)
        el.send_keys('local_pg')                                      #在输入框中输入内容
        sleep(1)
        el.send_keys(Keys.ENTER)                                      #在输入框中修改之后按enter键保存
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link6=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('修改成功', link6.text)                          #验证提示框是否提示修改成功
        self.add_img()
        self.save_img('修改数据存储') 
        sleep(2)

#用例7：对参数配置界面中的PostGIS的【主机】输入栏进行修改,刷新页面,查看修改部分是否保存
    @BeautifulReport.add_test_img('修改PostGIS的主机')
    def test_07_host(self):
        '''修改PostGIS的【主机】'''
        self.Interface('admin','admin123456')                         #进入参数配置界面
        el=self.driver.find_element_by_id('input_postgis_host')           #定位输入框
        el.send_keys(Keys.CONTROL,'a')                                #全选输入框内容
        el.send_keys(Keys.BACK_SPACE)                                 #删除全选的输入框内容
        sleep(1)
        el.send_keys(Keys.ENTER)                                      #键入enter键
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('不可为空', link1.text)                          #验证提示框是否提示输入框不可为空
        self.add_img()
        self.save_img('参数为空7') 
        sleep(2)
        el.send_keys('192.168.0.107')                               #在输入框中输入内容
        sleep(1)
        el.send_keys(Keys.ENTER)                                      #在输入框中修改之后按enter键保存
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link7=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('修改成功', link7.text)                          #验证提示框是否提示修改成功
        self.add_img()
        self.save_img('修改PostGIS的主机') 
        sleep(2)

#用例8：对参数配置界面中的PostGIS的【端口号】输入栏进行修改,刷新页面,查看修改部分是否保存
    @BeautifulReport.add_test_img('修改PostGIS的端口号')
    def test_08_port(self):
        '''修改PostGIS的【端口号】'''
        self.Interface('admin','admin123456')                         #进入参数配置界面
        el=self.driver.find_element_by_id('input_postgis_port')           #定位输入框
        el.send_keys(Keys.CONTROL,'a')                                #全选输入框内容
        el.send_keys(Keys.BACK_SPACE)                                 #删除全选的输入框内容
        sleep(1)
        el.send_keys(Keys.ENTER)                                      #键入enter键
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('不可为空', link1.text)                          #验证提示框是否提示输入框不可为空
        self.add_img()
        self.save_img('参数为空8') 
        sleep(2)
        el.send_keys('5432')                                          #在输入框中输入内容
        sleep(1)
        el.send_keys(Keys.ENTER)                                      #在输入框中修改之后按enter键保存
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link8=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('修改成功', link8.text)                          #验证提示框是否提示修改成功
        self.add_img()
        self.save_img('修改PostGIS的端口号') 
        sleep(2)

#用例9：对参数配置界面中的PostGIS的【数据库】输入栏进行修改,刷新页面,查看修改部分是否保存
    @BeautifulReport.add_test_img('修改PostGIS的数据库')
    def test_09_db(self):
        '''修改PostGIS的【数据库】'''
        self.Interface('admin','admin123456')                         #进入参数配置界面
        el=self.driver.find_element_by_id('input_postgis_db')             #定位输入框
        el.send_keys(Keys.CONTROL,'a')                                #全选输入框内容
        el.send_keys(Keys.BACK_SPACE)                                 #删除全选的输入框内容
        sleep(1)
        el.send_keys(Keys.ENTER)                                      #键入enter键
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('不可为空', link1.text)                          #验证提示框是否提示输入框不可为空
        self.add_img()
        self.save_img('参数为空9') 
        sleep(2)
        el.send_keys('postgis_test')                                       #在输入框中输入内容
        sleep(1)
        el.send_keys(Keys.ENTER)                                      #在输入框中修改之后按enter键保存
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link9=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('修改成功', link9.text)                          #验证提示框是否提示修改成功
        self.add_img()
        self.save_img('修改PostGIS的数据库') 
        sleep(2)

#用例10：对参数配置界面中的PostGIS的【用户名】输入栏进行修改,刷新页面,查看修改部分是否保存
    @BeautifulReport.add_test_img('修改PostGIS的用户名')
    def test_10_postgis_user(self):
        '''修改PostGIS的【数据库】'''
        self.Interface('admin','admin123456')                         #进入参数配置界面
        el=self.driver.find_element_by_id('input_postgis_user')             #定位输入框
        el.send_keys(Keys.CONTROL,'a')                                #全选输入框内容
        el.send_keys(Keys.BACK_SPACE)                                 #删除全选的输入框内容
        sleep(1)
        el.send_keys(Keys.ENTER)                                      #键入enter键
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('不可为空', link1.text)                          #验证提示框是否提示输入框不可为空
        self.add_img()
        self.save_img('参数为空10') 
        sleep(2)
        el.send_keys('postgres')                                       #在输入框中输入内容
        sleep(2)
        el.send_keys(Keys.ENTER)                                      #在输入框中修改之后按enter键保存
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link10=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('修改成功', link10.text)                          #验证提示框是否提示修改成功
        self.add_img()
        self.save_img('修改PostGIS的用户名') 
        sleep(2)

#用例11：对参数配置界面中的PostGIS的【密码】输入栏进行修改,刷新页面,查看修改部分是否保存
    @BeautifulReport.add_test_img('修改PostGIS的密码')
    def test_11_postgis_password(self):
        '''修改PostGIS的【数据库】'''
        self.Interface('admin','admin123456')                         #进入参数配置界面
        el=self.driver.find_element_by_id('input_postgis_password')             #定位输入框
        el.send_keys(Keys.CONTROL,'a')                                #全选输入框内容
        el.send_keys(Keys.BACK_SPACE)                                 #删除全选的输入框内容
        sleep(1)
        el.send_keys(Keys.ENTER)                                      #键入enter键
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('不可为空', link1.text)                          #验证提示框是否提示输入框不可为空
        self.add_img()
        self.save_img('参数为空11') 
        sleep(2)
        el.send_keys('zxhm001')                                       #在输入框中输入内容
        sleep(2)
        el.send_keys(Keys.ENTER)                                      #在输入框中修改之后按enter键保存
         #显示等待时间到弹出提示框
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link11=self.driver.find_element_by_id('alter_notify')              #定位提示框
        self.assertIn('修改成功', link11.text)                          #验证提示框是否提示修改成功
        self.add_img()
        self.save_img('修改PostGIS的密码') 
        sleep(2)





if __name__ == '__main__':
    unittest.main(argv=['ignored','-v'],exit=False)
    print('')
