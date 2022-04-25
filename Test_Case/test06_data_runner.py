'''
参数配置功能测试,分为以下几种情况:
(1)进入系统点击数据管理,界面自动跳转至数据管理界面
(2)点击数据管理界面中的上传数据按钮,查看是否弹出上传数据页面
(3)在上传数据弹窗中选择文件,点击上传,查看是否可以成功上传json数据
(4)在上传数据弹窗中点击选择文件,查看是否可以成功上传shp压缩数据
(5)在数据列表中点击刚刚新增的数据【预览】按钮,查看是否可以成功打开预览界面
(6)在数据管理界面中的搜索框输入关键字,查看是否能够完成查询工作

发布功能测试:
(7)在数据列表中点击刚刚新增的数据【发布】按钮,查看是否可以正常跳转至发布界面
(8)在发布界面点击下方的小地图中的【天地图影像】查看是否可以成功进行切换
(9)点击发布数据图层按钮是否能够成功弹出发布图层弹窗
(10)对样式能否完成修改
(11)修改相应样式后能否完成对应的数据发布
(12)在数据管理界面中对已发布的数据进行删除,查看是否删除成功
(13)对已发布的数据图层进行删除之后,再对该数据进行删除查看能否删除成功
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


class test06_DataCase(unittest.TestCase):
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
        # self.driver = webdriver.Edge()
        # self.driver.maximize_window()
      
#     def tearDown(self):
#         sleep(2)
#         print('测试完成')
#         self.driver.quit()

    def cleanup(self):
        pass

        #定义错误截图方法
    def save_img(self, img_name):  
        """
         传入一个img_name, 并存储到默认的文件路径下
         :param img_name:
          :return:
         """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('./数据管理/img'), img_name))    #os.path.abspath('')截图存放路径
    
#打开浏览器至数据管理界面
    def Data_Department(self,username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys(username)  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys(password)  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        # #显示等待时间到进入系统主界面
        # wait=WebDriverWait(self.driver,40,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        sleep(3)
        self.driver.implicitly_wait(2)   #隐式等待2秒
        self.driver.find_element_by_link_text('数据管理').click()   #点击数据管理按钮
        sleep(2)
        self.driver.implicitly_wait(2)   #隐式等待2秒 
        sleep(1)  

 #打开浏览器至数据管理界面获取发布句柄
    def Data_preview(self,username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys(username)  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys(password)  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        sleep(2)
         #显示时间等待菜单列表加载完
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        self.driver.find_element_by_link_text('数据管理').click()   #点击数据管理按钮
            #显示时间等待进入数据管理界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_data_upload'))) 
        sleep(1)
        sleep(2)
        print('未点击发布前的操作句柄:',self.driver.window_handles)
        self.driver.find_element_by_css_selector('#data_table tbody tr:last-child td:last-child  a:nth-child(3)').click()   #点击发布按钮
        self.driver.implicitly_wait(20)   #隐式等待15秒   
        print('点击发布后的操作句柄:',self.driver.window_handles)
        print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])  #切换至发布界面
        print('当前操作句柄:',self.driver.current_window_handle)
        sleep(2)

#数据管理界面
#用例1：进入系统点击数据管理,界面自动跳转至数据管理界面
#已验证成功
    @BeautifulReport.add_test_img('数据管理主界面') 
    def test_01_data_table(self):
        '''进入系统点击数据管理，查看界面是否进入数据管理界面'''
        self.Data_Department('admin','admin123456')    #进入数据管理界面
        link1=self.driver.find_element_by_id('data_table')  #断言是否成功进入数据管理界面
        self.assertIn('数据名称', link1.text)
        self.add_img()
        self.save_img('数据管理主界面') 
        sleep(2)

#用例2:点击数据管理界面中的上传数据按钮,查看是否弹出上传数据页面
#已验证成功
    @BeautifulReport.add_test_img('上传数据弹窗') 
    def test_02_input_data(self):
        '''点击数据管理界面中的上传数据按钮,查看是否弹出上传数据页面'''
        self.Data_Department('admin','admin123456')    #进入数据管理界面
        self.driver.find_element_by_id('btn_data_upload').click()   #点击上传数据按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒   
        sleep(2)
        #断言判定是否出现正确的弹窗
        link1=self.driver.find_element_by_id('input_data_form')
        self.assertIn('选择数据', link1.text)
        self.add_img()
        self.save_img('上传数据弹窗') 
        sleep(2)
#用例3:在上传数据弹窗中点击选择文件,查看是否可以成功上传json数据
#已验证成功
    @BeautifulReport.add_test_img('json数据上传') 
    def test_03_data_save_json(self):
        '''点击上传数据,选择json数据,查看文件是否可以正常上传'''
        self.Data_Department('admin','admin123456')    #进入数据管理界面
        self.driver.find_element_by_id('btn_data_upload').click()   #点击上传数据按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒
        sleep(2)  
        #上传json数据
        self.driver.find_element_by_id('input_data_file').send_keys(os.path.abspath('./数据管理/testdata/test_point.json'))   #选择本地json文件上传
        self.add_img()
        self.driver.implicitly_wait(15)   #隐式等待10秒
        sleep(3)
        el1=self.driver.find_element_by_id('input_data_name')  #定位数据名称
        el1.clear()
        el1.send_keys('Save_Json')  #输入数据名称
        self.driver.find_element_by_id('input_data_table').clear()    #清空存储表名
        self.driver.find_element_by_id('input_data_table').send_keys('Save_Json表')     #输入存储表名
        sleep(1)
        self.driver.find_element_by_id('input_data_description').send_keys('测试上传json数据')   #在数据描述中输入测试上传json数据
        self.driver.find_element_by_id('btn_data_save').click()     #点击上传按钮
        sleep(2)
        #显示等待时间到弹出框出现
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify')))
        #断言判定弹出框是否显示数据上传成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('数据上传成功', link1.text)
        self.add_img()
        self.save_img('json数据上传')   #截图上传成功
#回到首页的地图管理中的添加地图界面查看数据是否添加成功
        self.driver.refresh()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_link_text('地图管理').click()   #进入地图管理界面
        sleep(2)
        self.driver.find_element_by_id('btn_map_add').click()  #点击创建地图按钮
        self.driver.implicitly_wait(20)
        print('点击创建地图后的操作句柄:',self.driver.window_handles)
        print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])  #切换至创建地图界面
        print('切换至创建地图操作句柄:',self.driver.current_window_handle)
        sleep(3)
        self.driver.find_element_by_id('btn_map_addLayer').click()  #点击选择图层按钮
        sleep(3)
        self.driver.find_element_by_id('contact-tab').click()  #点击数据按钮
        #显示等待时间直到数据列表出现
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.ID,'data_container_list'))) 
#断言图层列表中是否存在刚刚新增的图层
        link3=self.driver.find_element_by_id('data_container_list')
        self.assertIn('Save_Json',link3.text)
        self.add_img()
        self.save_img('创建地图数据列表json')
        sleep(2)
        self.driver.close() #关闭当前页面
        self.driver.switch_to.window(self.driver.window_handles[0])
        

#用例4:在上传数据弹窗中点击选择文件,查看是否可以成功上传shp压缩数据
#已验证成功
    @BeautifulReport.add_test_img('shp压缩数据上传') 
    def test_04_data_save_shp(self):
        '''点击上传数据,选择shp压缩文件,查看文件是否可以正常上传'''
        self.Data_Department('admin','admin123456')    #进入数据管理界面
        self.driver.find_element_by_id('btn_data_upload').click()   #点击上传数据按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒
        sleep(2)
        #上传shp压缩文件
        self.driver.find_element_by_id('input_data_file').send_keys(os.path.abspath('./数据管理/testdata/point/point.zip'))    #选择本地shp压缩文件上传
        self.add_img()
        self.driver.implicitly_wait(16)   #隐式等待10秒
        sleep(3)
        el1=self.driver.find_element_by_id('input_data_name')  #定位数据名称
        el1.clear()
        el1.send_keys('Save_Shp')  #输入数据名称
        sleep(1)
        self.driver.find_element_by_id('input_data_table').clear()    #清空存储表名
        self.driver.find_element_by_id('input_data_table').send_keys('Save_shp表')     #输入存储表名
        sleep(1)
        self.driver.find_element_by_id('input_data_description').send_keys('测试上传shp压缩文件')   #在数据描述中输入测试上传shp压缩文件
        sleep(2)
        self.driver.find_element_by_id('btn_data_save').click()     #点击上传按钮
        #显示等待时间到弹出框
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify')))
        #断言弹出框显示数据上传成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('数据上传成功', link1.text)
        self.add_img()
        self.save_img('shp压缩数据上传成功') 
        sleep(2)
#回到首页的地图管理中的添加地图界面查看数据是否添加成功
        self.driver.refresh()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_link_text('地图管理').click()   #进入地图管理界面
        sleep(2)
        self.driver.find_element_by_id('btn_map_add').click()  #点击创建地图按钮
        self.driver.implicitly_wait(20)
        print('点击创建地图后的操作句柄:',self.driver.window_handles)
        print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])  #切换至创建地图界面
        print('切换创建地图后操作句柄:',self.driver.current_window_handle)
        sleep(3)
        self.driver.find_element_by_id('btn_map_addLayer').click()  #点击选择图层按钮
        sleep(3)
        self.driver.find_element_by_id('contact-tab').click()  #点击数据按钮
        #显示等待时间直到数据列表出现
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.ID,'data_container_list'))) 
#断言图层列表中是否存在刚刚新增的图层
        link3=self.driver.find_element_by_id('data_container_list')
        self.assertIn('Save_Shp',link3.text)
        self.add_img()
        self.save_img('创建地图数据列表shp')
        sleep(2)
        self.driver.close() #关闭创建地图界面
        self.driver.switch_to.window(self.driver.window_handles[0]) #回到首页界面
       

#用例5:在数据列表中点击刚刚新增的数据【预览】按钮,查看是否可以成功打开预览界面
#已验证成功
    @BeautifulReport.add_test_img('查看预览') 
    def test_05_preview(self):
        '''点击预览按钮,查看是否可以成功打开预览界面'''
        self.Data_Department('admin','admin123456')    #进入数据管理界面
        self.driver.find_element_by_css_selector('#data_table tbody tr:last-child td:last-child  a:first-child').click()   #点击预览按钮
        self.driver.implicitly_wait(20)   #隐式等待20秒
         #显示等待时间直到预览地图出现
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME,'leaflet-control-zoom-in')))    
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()  #点击放大按钮
        self.add_img()
        self.save_img('预览放大成功')
        sleep(2)
        self.driver.find_element_by_class_name('leaflet-control-zoom-out').click()  #点击缩小按钮
        sleep(2)
        self.add_img()
        self.save_img('预览缩小成功')
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()  #点击放大按钮
        sleep(2) 
        self.add_img()   
        self.save_img('预览查看成功') 
        sleep(2)
      
#用例6:在数据管理界面中的搜索框输入关键字,查看是否能够完成查询工作
#已验证成功
    @BeautifulReport.add_test_img('搜索查询数据名称') 
    def test_06_search(self):
        '''在搜索框中输入数据名称关键字,查看是否能完成查询'''
        self.Data_Department('admin','admin123456')    #进入数据管理界面
        self.driver.find_element_by_id('input_data_search').send_keys('Save')   #点击搜索输入框输入查询内容
        self.driver.find_element_by_id('btn_data_search').click()       #点击搜索按钮
        sleep(2)
        #断言搜索后显示的数据列表第一行的数据名称中包含ponit
        link1=self.driver.find_element_by_css_selector('#data_table tbody tr:first-child td:nth-last-child(7)')
        self.assertIn('Save', link1.text)
        self.add_img()  
        self.save_img('搜索查询数据名称') 
        sleep(2)
       
       
#用例7：在数据列表中点击刚刚新增的数据【发布】按钮,查看是否可以正常跳转至发布界面
#已验证成功
    @BeautifulReport.add_test_img('数据发布界面') 
    def test_07_publish(self):
        '''点击发布按钮,查看界面能否进入发布界面'''
        self.Data_preview('admin','admin123456')    #进入数据管理界面
        self.driver.implicitly_wait(10)   #隐式等待10秒
         #显示等待时间直到加载完成
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME,'leaflet-styleeditor-footer'))) 
        link1=self.driver.find_element_by_id('btn_publish')
        self.assertIn('发布数据',link1.text)
        self.add_img()  
        self.save_img('数据发布界面')
        self.driver.close() #关闭创建地图界面
        self.driver.switch_to.window(self.driver.window_handles[0]) #回到首页界面
     
      
 
#用例8:在发布界面点击下方的小地图中的【天地图影像】查看是否可以成功进行切换
#已验证成功
    @BeautifulReport.add_test_img('天地图影像') 
    def test_08_image_change(self):
        '''点击下方小地图,查看能否切换成天地图影像'''
        self.Data_preview('admin','admin123456')                     #进入数据管理界面
        wait=WebDriverWait(self.driver,400,0.5)            #显示等待时间直到设置样式出现
        wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME,'leaflet-styleeditor-interior-geometry'))) 
        el=self.driver.find_element_by_id('basemap_wrapper')             #鼠标移动至下方的天地图处
        ActionChains(self.driver).move_to_element(el)
        el.click()
        self.driver.find_element_by_id('basemap_tdt_img').click()           #点击天地图影像
        self.driver.implicitly_wait(10)   #隐式等待10秒
        self.save_img('天地图影像')
        self.add_img()  
        sleep(2)
        self.driver.close() #关闭创建地图界面
        self.driver.switch_to.window(self.driver.window_handles[0]) #回到首页界面
        
      


#用例9：点击发布数据图层按钮是否能够成功弹出发布图层弹窗
    @BeautifulReport.add_test_img('发布图层弹窗') 
    def test_09_layer_window(self):
        '''点击发布数据按钮,能否正常弹出发布图层弹窗'''
        self.Data_preview('admin','admin123456')    #进入数据管理界面
        #点击发布数据按钮
        self.driver.implicitly_wait(10)   #隐式等待10秒
         #显示等待时间直到加载完成
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME,'leaflet-styleeditor-footer'))) 
        self.driver.find_element_by_id('btn_publish').click() 
        #显示等待时间直到弹出框显示
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_layer_form'))) 
        #断言是否弹出发布图层弹窗
        link1=self.driver.find_element_by_id('input_layer_form')   
        self.assertIn('样式名称',link1.text)
        self.add_img()  
        self.save_img('发布图层弹窗')
        sleep(2)
        self.driver.close() #关闭创建地图界面
        self.driver.switch_to.window(self.driver.window_handles[0])  #回到首页界面

#用例10：对样式能否完成修改
    @BeautifulReport.add_test_img('样式修改') 
    def test_10_style_change(self):
        '''在发布界面测试样式修改'''
        self.Data_preview('admin','admin123456')    #进入数据管理界面
        wait=WebDriverWait(self.driver,400,0.5)            #显示等待时间直到设置样式出现
        wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME,'leaflet-styleeditor-interior-geometry'))) 
#点击放大“+”号按钮
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()     
        sleep(1)
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()
        sleep(1)
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()
        sleep(1)
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()
        sleep(2)
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()
        sleep(2)
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()
        sleep(2)
#修改半径
        ele1=self.driver.find_element_by_css_selector('#styleeditor_ue_radius input ')
        self.driver.execute_script("arguments[0].value = '14';",ele1)
        #事件触发
        self.driver.execute_script("var evt = document.createEvent('MouseEvents');evt.initEvent('mouseup', true, false);$('#styleeditor_ue_radius input')[0].dispatchEvent(evt)")
        sleep(1)
        self.add_img()
#修改边框或线条颜色,选择第一个颜色
        self.driver.find_element_by_css_selector('.leaflet-styleeditor-interior-geometry  div:nth-child(2) div div:nth-child(1) ').click() 
        sleep(1)
        self.add_img()
#修改透明度
        ele2=self.driver.find_element_by_css_selector('#styleeditor_ue_opacity input')
        self.driver.execute_script("arguments[0].value = '0.2';",ele2)
        #事件触发
        self.driver.execute_script("var evt = document.createEvent('MouseEvents');evt.initEvent('mouseup', true, false);$('#styleeditor_ue_opacity input')[0].dispatchEvent(evt)")
        sleep(1)   
        self.add_img()
#修改线宽
        ele3=self.driver.find_element_by_css_selector('#styleeditor_ue_weight input ')
        self.driver.execute_script("arguments[0].value = '15';",ele3)
        #事件触发
        self.driver.execute_script("var evt = document.createEvent('MouseEvents');evt.initEvent('mouseup', true, false);$('#styleeditor_ue_weight input')[0].dispatchEvent(evt)")
        sleep(1)
        self.add_img()
#修改线型
        self.driver.find_element_by_css_selector('#styleeditor_ue_dashArray div:last-child ').click()
        sleep(1)
        self.add_img()
#修改填充颜色
        self.driver.find_element_by_css_selector('#styleeditor_ue_fillColor  div div:nth-child(13)').click() 
        sleep(1)
        self.add_img()
#填充透明度
        ele4=self.driver.find_element_by_css_selector('#styleeditor_ue_fillOpacity input ')
        self.driver.execute_script("arguments[0].value = '1';",ele4)
        #事件触发
        self.driver.execute_script("var evt = document.createEvent('MouseEvents');evt.initEvent('mouseup', true, false);$('#styleeditor_ue_fillOpacity input')[0].dispatchEvent(evt)")
        sleep(1)
        self.add_img()
#保存修改后的图片
        self.save_img('修改样式成功的图片') 
        self.add_img()  
        sleep(2)
        self.driver.close() #关闭创建地图界面
        self.driver.switch_to.window(self.driver.window_handles[0])  #回到首页界面
       



#用例11:修改相应样式后能否完成对应的数据发布
    @BeautifulReport.add_test_img('发布数据') 
    def test_11_Data_released(self):
        '''测试修改样式后能否发布数据图层'''
        self.Data_preview('admin','admin123456')    #进入数据管理界面
        wait=WebDriverWait(self.driver,400,0.5)            #显示等待时间直到设置样式出现
        wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME,'leaflet-styleeditor-interior-geometry'))) 
#点击放大“+”号按钮
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()     
        sleep(1)
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()
        sleep(1)
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()
        sleep(1)
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()
        sleep(2)
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()
        sleep(2)
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()
        sleep(2)
#修改半径
        ele1=self.driver.find_element_by_css_selector('#styleeditor_ue_radius input ')
        self.driver.execute_script("arguments[0].value = '14';",ele1)
        #事件的触发
        self.driver.execute_script("var evt = document.createEvent('MouseEvents');evt.initEvent('mouseup', true, false);$('#styleeditor_ue_radius input')[0].dispatchEvent(evt)")
        sleep(1)
#修改边框或线条颜色,选择第一个颜色
        self.driver.find_element_by_css_selector('.leaflet-styleeditor-interior-geometry  div:nth-child(2) div div:nth-child(1) ').click() 
        sleep(1)
#修改透明度
        ele2=self.driver.find_element_by_css_selector('#styleeditor_ue_opacity input')
        self.driver.execute_script("arguments[0].value = '0.2';",ele2)
        #事件触发
        self.driver.execute_script("var evt = document.createEvent('MouseEvents');evt.initEvent('mouseup', true, false);$('#styleeditor_ue_opacity input')[0].dispatchEvent(evt)")
        sleep(1)
#修改线宽
        ele3=self.driver.find_element_by_css_selector('#styleeditor_ue_weight input ')
        self.driver.execute_script("arguments[0].value = '15';",ele3)
        #事件触发
        self.driver.execute_script("var evt = document.createEvent('MouseEvents');evt.initEvent('mouseup', true, false);$('#styleeditor_ue_weight input')[0].dispatchEvent(evt)")
        sleep(1)
#修改线型
        self.driver.find_element_by_css_selector('#styleeditor_ue_dashArray div:last-child ').click()
        sleep(1)
#修改填充颜色
        self.driver.find_element_by_css_selector('#styleeditor_ue_fillColor  div div:nth-child(13)').click() 
        sleep(1)
#填充透明度
        ele4=self.driver.find_element_by_css_selector('#styleeditor_ue_fillOpacity input ')
        self.driver.execute_script("arguments[0].value = '1';",ele4)
        #事件触发
        self.driver.execute_script("var evt = document.createEvent('MouseEvents');evt.initEvent('mouseup', true, false);$('#styleeditor_ue_fillOpacity input')[0].dispatchEvent(evt)")
        sleep(1)
#点击发布数据按钮
        self.driver.find_element_by_id('btn_publish').click()    #点击发布数据按钮
        self.driver.implicitly_wait(2)
        ele5=self.driver.find_element_by_id('input_layer_name')   #定位图层名称
        ele5.clear()
        ele5.send_keys('测试发布图层')  #修改图层名称
        self.driver.find_element_by_id('input_layer_name').clear()  #清除图层标题输入框
        self.driver.find_element_by_id('input_layer_name').send_keys('修改图层标题')  #输入修改后的图层标题
        self.driver.find_element_by_id('input_layer_style').clear()   #清除样式名称输入框 
        self.driver.find_element_by_id('input_layer_style').send_keys('修改图层后样式')   #输入修改后的样式名称
        self.driver.find_element_by_id('input_layer_description').send_keys('修改')
        sleep(1)
        self.driver.find_element_by_id('btn_layer_save').click()           #点击发布按钮
#显示等待时间到弹出框显示数据发布成功
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('图层发布成功', link1.text)
        self.add_img()  
        self.save_img('图层发布成功')
        sleep(1)
#回到首页的图层管理去验证是否已发布成功
        self.driver.switch_to.window(self.driver.window_handles[0])            #回到主界面
        self.driver.implicitly_wait(2)   #隐式等待2秒
        sleep(3)
        self.driver.find_element_by_link_text('图层管理').click()           #点击图层管理按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒
        #断言发布图层列表中是否存在刚刚新发布的图层
        link2=self.driver.find_element_by_css_selector('#layer_list div:last-child div div div.col-9 div.pl-xl-3 div.m-b-0 div h2')   #定位图层列表最后一列图层名称位置
        self.assertIn('修改图层标题', link2.text)
        sleep(1)
#回到首页的地图管理中的添加地图界面查看是否图层添加成功
        self.driver.refresh()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_link_text('地图管理').click()   #进入地图管理界面
        sleep(3)
        self.driver.find_element_by_id('btn_map_add').click()  #点击创建地图按钮
        self.driver.implicitly_wait(20)
        print('点击创建地图后的操作句柄:',self.driver.window_handles)
        print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])  #切换至创建地图界面
        print('当前操作句柄:',self.driver.current_window_handle)
        sleep(3)
        self.driver.find_element_by_id('btn_map_addLayer').click()  #点击选择图层按钮
        sleep(3)
        self.driver.find_element_by_id('profile-tab').click()  #点击图层按钮
        #显示等待时间直到图层列表出现
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.ID,'layer_container_list'))) 
#断言图层列表中是否存在刚刚新增的图层
        link3=self.driver.find_element_by_id('layer_container_list')
        self.assertIn('修改图层标题',link3.text)
        self.add_img()  
        self.save_img('创建地图图层列表')
        sleep(2)
        self.driver.close() #关闭创建地图界面
        self.driver.switch_to.window(self.driver.window_handles[0])  #回到首页界面
      
#用例12：在数据管理界面中对已发布的数据进行删除，查看是否删除成功
    @BeautifulReport.add_test_img('删除数据') 
    def test_12_delete_data(self):
        '''不删除图层,直接删除数据,是否提示存在相关联的图层'''
        self.Data_Department('admin','admin123456')    #进入数据管理界面
        self.driver.find_element_by_css_selector('#data_table tbody tr:last-child  td:last-child a:last-child').click()   #点击最后一列数据的删除按钮
        sleep(1)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        print(alert.text)  # 打印窗口信息
        sleep(1)
        alert.dismiss()  # 取消删除
        sleep(2)
        self.driver.find_element_by_css_selector('#data_table tbody tr:last-child  td:last-child a:last-child').click()   #点击最后一列数据的删除按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        sleep(2)
        alert.accept()  # 确认删除数据
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('存在相关联的图层', link1.text)
        self.add_img()  
        self.save_img('存在相关联的图层') 
        sleep(2)
    

#用例13：对已发布的数据图层进行删除之后，再对该数据进行删除查看能否删除成功
    @BeautifulReport.add_test_img('删除数据') 
    def test_13_delete_layer(self):
        '''对图层删除后查看能否删除数据列表中的最后一列数据'''
        self.Data_Department('admin','admin123456')    #进入数据管理界面
        self.driver.implicitly_wait(10)   #隐式等待10秒
#回到图层管理界面，删除刚刚发布的图层
        self.driver.find_element_by_link_text('图层管理').click()           #点击图层管理按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒
        self.driver.find_element_by_css_selector('#layer_list > div:last-child input:last-child').click()   #点击图层列表最后一列的删除按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        self.driver.implicitly_wait(2)   #隐式等待2秒
        alert.accept()               # 确认删除图层
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link1.text)
        self.add_img()  
        self.save_img('图层删除成功') 
#图层删除成功后回到数据管理界面再对数据完成删除
        sleep(2)
        self.driver.find_element_by_link_text('数据管理').click()           #点击数据管理按钮
        sleep(1)
        self.driver.find_element_by_css_selector('#data_table tbody tr:last-child  td:last-child a:last-child').click()   #点击最后一列数据的删除按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        sleep(2)
        alert.accept()  # 确认删除数据
        link2=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link2.text)
        self.add_img()  
        self.save_img('数据删除成功')
        sleep(2)
        self.driver.find_element_by_css_selector('#data_table tbody tr:last-child  td:last-child a:last-child').click()   #点击最后一列数据的删除按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        sleep(2)
        alert.accept()  # 确认删除数据
        link3=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link3.text)
        self.add_img()  
      





if __name__ == '__main__':
    unittest.main(argv=['ignored','-v'],exit=False)
    print('')

