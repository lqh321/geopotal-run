'''
地图管理功能测试分为以下几种情况:
(1)点击地图管理,查看能否正常进入地图管理界面
(2)点击地图管理中创建地图查看能否打开创建地图界面
创建地图:
(3)切换至创建地图界面点击选择图层,查看是否弹出图层选择弹窗
(4)切换至创建地图界面点击保存地图,查看是否弹出保存地图弹窗
(5)在图层选择弹窗中【底图】选择天地图影像,点击确定,查看底图是否变化
(6)在图层选择弹窗中【图层】选择两个图层,点击确定,查看图层是否有增加
(7)在图层选择弹窗中【数据】选择某一数据,点击确定,查看数据是否有增加
(8)在图层选择弹窗中选择对应底图、图层、数据,点击确定,点击保存地图,在弹出的保存地图弹窗中输入地图名称、地图描述,点击确定,查看是否发布地图成功
(9)在地图管理界面点击搜索,输入地图名称、地图描述对应的关键字,查看能否筛选
修改地图:
(10)点击地图列表中的最后一列,点击打开,查看能否打开地图页面
(11)打开某一地图页面,点击选择图层,修改【底图】、【图层】、【数据】,点击确定,最后点击保存底图,查看是否完成修改
(12)在图层列表中点击最后一行图层对应删除按钮,查看是否删除成功
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


class test08_MapCase(unittest.TestCase):

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
         传入一个img_name, 并存储到默认的文件路径下
         :param img_name:
          :return:
         """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('./地图管理/img'), img_name))    #os.path.abspath('')截图存放路径

#打开浏览器至数据管理界面
    def map_management(self,username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys(username)  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys(password)  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        sleep(3)
        #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        self.driver.find_element_by_link_text('地图管理').click()   #点击地图管理按钮
        sleep(2) 
        wait=WebDriverWait(self.driver,400,0.5)            #显示等待时间直到创建地图ID出现
        wait.until(EC.visibility_of_any_elements_located((By.ID,'page_map'))) 
         



#用例1：点击地图管理,查看能否正常进入地图管理界面
    @BeautifulReport.add_test_img('地图管理主界面') 
    def test_01_page_map(self):
        '''点击地图管理,查看能否正常进入地图管理界面'''
        self.map_management('admin','admin123456')    #进入地图管理界面
        self.add_img()
        self.save_img('地图管理主界面') 
        sleep(2)
   


 #用例2：点击地图管理中创建地图查看能否打开创建地图界面
    @BeautifulReport.add_test_img('创建地图界面') 
    def test_02_add_map(self):
        '''点击地图管理中创建地图查看能否打开创建地图界面'''
        self.map_management('admin','admin123456')    #进入地图管理界面
        print('未点击创建地图前的操作句柄:',self.driver.window_handles)
        self.driver.find_element_by_id('btn_map_add').click()  #点击创建地图按钮
        self.driver.implicitly_wait(20)
        print('点击创建地图后的操作句柄:',self.driver.window_handles)
        print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])  #切换至创建地图界面
        print('当前操作句柄:',self.driver.current_window_handle)
        #断言是否进入创建地图界面
        link1=self.driver.find_element_by_class_name('layer-title')
        self.assertIn('图层',link1.text)
        self.add_img()
        self.save_img('创建地图界面')
        sleep(1)
        self.driver.close() #关闭创建地图界面
        self.driver.switch_to.window(self.driver.window_handles[0])  #切换至首页


#用例3：切换至创建地图界面点击选择图层,查看是否弹出图层选择弹窗
    @BeautifulReport.add_test_img('选择图层界面') 
    def test_03_layer_selection(self):
        '''切换至创建地图界面点击选择图层,查看是否弹出图层选择弹窗'''
        self.map_management('admin','admin123456')    #进入地图管理界面
        self.driver.find_element_by_id('btn_map_add').click()  #点击创建地图按钮
        self.driver.implicitly_wait(20)
        # print('点击创建地图后的操作句柄:',self.driver.window_handles)
        # print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])  #切换至创建地图界面
        # print('当前操作句柄:',self.driver.current_window_handle)
        sleep(2)
        self.driver.find_element_by_id('btn_map_addLayer').click()  #点击选择图层
        sleep(2)
        #断言是否弹出图层选择弹窗
        link1=self.driver.find_element_by_css_selector('#modal_layer_select h5')  
        self.assertIn('图层选择',link1.text)
        self.add_img()
        self.save_img('图层选择弹窗')
        sleep(2)
        self.driver.close() #关闭创建地图界面
        self.driver.switch_to.window(self.driver.window_handles[0])  #切换至首页

#用例4：切换至创建地图界面点击保存地图,查看是否弹出保存地图弹窗
    @BeautifulReport.add_test_img('保存地图界面') 
    def test_04_map_save(self):
        '''切换至创建地图界面点击保存地图,查看是否弹出保存地图弹窗'''
        self.map_management('admin','admin123456')    #进入地图管理界面
        self.driver.find_element_by_id('btn_map_add').click()  #点击创建地图按钮
        self.driver.implicitly_wait(20)
        # print('点击创建地图后的操作句柄:',self.driver.window_handles)
        # print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])  #切换至创建地图界面
        # print('当前操作句柄:',self.driver.current_window_handle)
        sleep(2)
        self.driver.find_element_by_id('btn_map_p_save').click()  #点击保存地图
        sleep(2)
        #断言是否弹出图层选择弹窗
        link1=self.driver.find_element_by_css_selector('#modal_map_add h5')  
        self.assertIn('保存地图',link1.text)
        self.add_img()
        self.save_img('保存地图弹窗')
        sleep(2)   
        self.driver.close() #关闭创建地图界面
        self.driver.switch_to.window(self.driver.window_handles[0])  #切换至首页
    
#用例5：在图层选择弹窗中【底图】选择天地图影像,点击确定,查看底图是否变化
    @BeautifulReport.add_test_img('选择底图界面') 
    def test_05_base_map_selection(self):
        '''在图层选择弹窗中【底图】选择天地图影像,点击确定,查看底图是否变化'''
        self.map_management('admin','admin123456')    #进入地图管理界面
        self.driver.find_element_by_id('btn_map_add').click()  #点击创建地图按钮
        sleep(2)
        # self.driver.implicitly_wait(10)
        # print('点击创建地图后的操作句柄:',self.driver.window_handles)
        # print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])  #切换至创建地图界面
        # print('当前操作句柄:',self.driver.current_window_handle)
        sleep(1)
        self.driver.find_element_by_id('btn_map_addLayer').click()  #点击选择图层
         #显示等待时间直到底图列表出现
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.ID,'baselayer_container'))) 
        #选择底图
        self.driver.find_element_by_link_text('天地图影像').click()  #点击天地图影像
        sleep(1)
        self.add_img()
        self.driver.find_element_by_css_selector('#btn_layer_select').click()   #点击确定按钮
        sleep(2)
        self.add_img()
        self.save_img('变换底图成功')
        sleep(2)
        self.driver.close() #关闭创建地图界面
        self.driver.switch_to.window(self.driver.window_handles[0])  #切换至首页
     
#用例6：在图层选择弹窗中【图层】选择两个图层,点击确定,查看图层是否有增加
    @BeautifulReport.add_test_img('选择图层界面') 
    def test_06_layer_selection(self):
        '''在图层选择弹窗中【图层】选择两个图层,点击确定,查看图层是否有增加'''
        self.map_management('admin','admin123456')    #进入地图管理界面
        self.driver.find_element_by_id('btn_map_add').click()  #点击创建地图按钮
        sleep(2)
        # self.driver.implicitly_wait(10)
        # print('点击创建地图后的操作句柄:',self.driver.window_handles)
        # print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])  #切换至创建地图界面
        # print('当前操作句柄:',self.driver.current_window_handle)
        sleep(1)
        self.driver.find_element_by_id('btn_map_addLayer').click()  #点击选择图层按钮
        sleep(1)
        self.driver.find_element_by_id('profile-tab').click()  #点击图层按钮
         #显示等待时间直到图层列表出现
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.ID,'layer_container_list'))) 
        #选择图层
        self.driver.find_element_by_css_selector('#layer_container_list div:nth-child(2)').click()
        self.driver.find_element_by_css_selector('#layer_container_list div:nth-child(3)').click()
        sleep(1)
        self.add_img()
        self.driver.find_element_by_css_selector('#btn_layer_select').click()   #点击确定按钮
        sleep(2)
        self.add_img()
        self.save_img('选择图层成功')
        sleep(2)
        self.driver.close() #关闭创建地图界面
        self.driver.switch_to.window(self.driver.window_handles[0])  #切换至首页

#用例7：在图层选择弹窗中【数据】选择某一数据,点击确定,查看数据是否有增加
    @BeautifulReport.add_test_img('选择数据界面') 
    def test_07_data_selection(self):
        '''在图层选择弹窗中【数据】选择某一数据,点击确定,查看数据是否有增加'''
        self.map_management('admin','admin123456')    #进入地图管理界面
        self.driver.find_element_by_id('btn_map_add').click()  #点击创建地图按钮
        sleep(2)
        # self.driver.implicitly_wait(10)
        # print('点击创建地图后的操作句柄:',self.driver.window_handles)
        # print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])  #切换至创建地图界面
        # print('当前操作句柄:',self.driver.current_window_handle)
        sleep(3)
        self.driver.find_element_by_id('btn_map_addLayer').click()  #点击选择图层按钮
        sleep(1)
        self.driver.find_element_by_id('contact-tab').click()  #点击数据按钮
        #显示等待时间直到数据列表出现
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.ID,'data_container_list'))) 
        #选择数据
        self.driver.find_element_by_css_selector('#data_container_list  div:nth-child(1)').click()
        self.driver.find_element_by_css_selector('#data_container_list  div:nth-child(2)').click()
        sleep(1)
        self.add_img()
        self.driver.find_element_by_css_selector('#btn_layer_select').click()   #点击确定按钮
        sleep(2)
        self.add_img()
        self.save_img('选择数据成功')
        sleep(2)
        self.driver.close() #关闭创建地图界面
        self.driver.switch_to.window(self.driver.window_handles[0])  #切换至首页

#用例8：在图层选择弹窗中选择对应底图、图层、数据,点击确定,点击保存地图,在弹出的保存地图弹窗中输入地图名称、地图描述,点击确定,查看是否发布地图成功
    @BeautifulReport.add_test_img('发布地图') 
    def test_08_release_map(self):
        '''在图层选择弹窗中选择对应底图、图层、数据,点击确定,点击保存地图,在弹出的保存地图弹窗中输入地图名称、地图描述,点击确定,查看是否发布地图成功'''
        self.map_management('admin','admin123456')    #进入地图管理界面
        self.driver.find_element_by_id('btn_map_add').click()  #点击创建地图按钮
        sleep(2)
        # self.driver.implicitly_wait(10)
        # print('点击创建地图后的操作句柄:',self.driver.window_handles)
        # print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])  #切换至创建地图界面
        # print('当前操作句柄:',self.driver.current_window_handle)
        sleep(1)
#切换底图
        self.driver.find_element_by_id('btn_map_addLayer').click()  #点击选择图层
        #显示等待时间直到底图列表出现
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.ID,'baselayer_container'))) 
        self.driver.find_element_by_id('laye_sel_tdt_img').click()  #点击天地图影像
        sleep(1)
#选择图层
        sleep(1)
        self.driver.find_element_by_id('profile-tab').click()  #点击图层按钮
        #显示等待时间直到图层列表出现
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.ID,'layer_container_list'))) 
        #选择图层
        self.driver.find_element_by_css_selector('#layer_container_list div:nth-child(2)').click()
        sleep(2)
        self.driver.find_element_by_css_selector('#layer_container_list div:nth-child(3)').click()
        sleep(2)
#选择数据
        sleep(1)
        self.driver.find_element_by_id('contact-tab').click()  #点击数据按钮
        #显示等待时间直到数据列表出现
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.ID,'data_container_list'))) 
        #选择数据
        self.driver.find_element_by_css_selector('#data_container_list  div:nth-child(1)').click()
        sleep(2)
        self.driver.find_element_by_css_selector('#data_container_list  div:nth-child(2)').click()
        sleep(2)
        self.driver.find_element_by_css_selector('#btn_layer_select').click()   #点击确定按钮
        sleep(4)
#点击保存地图
        self.driver.find_element_by_id('btn_map_p_save').click()   #点击保存地图按钮
        sleep(2)
        #显示等待时间直到保存地图弹窗出现
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_layer_form'))) 
        sleep(2)
        el=self.driver.find_element_by_id('input_map_name')
        el.click()
        sleep(2)
        el.send_keys('测试发布地图名称')   #在地图名称输入框输入
        sleep(4)
        self.driver.find_element_by_id('input_map_description').send_keys('测试发布地图描述')   #在地图描述输入框输入
        sleep(4)
        self.add_img()
        self.driver.find_element_by_id('btn_map_save').click()   #点击保存按钮
        sleep(1)
#断言是否发布成功
        wait=WebDriverWait(self.driver,400,0.5)            #显示等待时间直到创建地图ID出现
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('地图保存成功',link1.text)
        self.add_img()
        self.save_img('地图保存成功')
        #回到首页查看是否在图层列表中已添加成功
        self.driver.close() #关闭创建地图界面
        self.driver.switch_to.window(self.driver.window_handles[0])  #切换至首页界面
        self.driver.refresh()   #刷新当前页面
        self.driver.implicitly_wait(2)   #隐式等待2秒
        self.driver.find_element_by_link_text('地图管理').click()   #点击地图管理按钮
        link2=self.driver.find_element_by_css_selector('#map_list div:last-child div div div.col-9 div.pl-xl-3 div.user-avatar-address p')  #定位图层列表最后一行的图层描述
        self.assertIn('测试发布地图描述',link2.text)
        self.add_img()
        self.save_img('发布地图成功')
        sleep(3)
    

#用例9：在地图管理界面点击搜索,输入地图名称、地图描述对应的关键字,查看能否筛选
    @BeautifulReport.add_test_img('地图筛选') 
    def test_09_search_map(self):
        '''在地图管理界面点击搜索,输入地图名称、地图描述对应的关键字,查看能否筛选'''
        self.map_management('admin','admin123456')    #进入地图管理界面
#根据图层名称筛选
        el=self.driver.find_element_by_id('input_map_search')             #定义搜索框
        el.send_keys('地图')         #在搜索框内输入关键字
        self.driver.find_element_by_id('btn_map_search').click()       #点击搜索按钮
        sleep(2)
        #断言筛选是否成功
        link1=self.driver.find_element_by_css_selector('#map_list> div:first-child h2') #定位筛选后地图第一列的地图名称位置
        self.assertIn('地图',link1.text)
        self.add_img()
        self.save_img('图层名称关键字筛选')
        sleep(2)
#根据图层描述筛选
        el.clear()  #清除筛选框
        self.driver.find_element_by_id('btn_map_search').click()       #点击搜索按钮
        wait=WebDriverWait(self.driver,400,0.5)            #显示等待时间直到地图列表ID出现
        wait.until(EC.visibility_of_any_elements_located((By.ID,'map_list'))) 
        el.send_keys('描述')   #筛选框输入图层描述关键字
        self.driver.find_element_by_id('btn_map_search').click()       #点击搜索按钮
        #断言筛选是否成功
        sleep(2)
        link2=self.driver.find_element_by_css_selector('#map_list> div:first-child p')#定位筛选后地图第一列的地图描述位置
        self.assertIn('描述',link2.text)
        self.add_img()
        self.save_img('图层描述关键字筛选成功')
        sleep(2)

#修改地图:
#用例10：点击地图列表中的最后一列,点击打开,查看能否打开地图页面
    @BeautifulReport.add_test_img('打开地图') 
    def test_10_open_map(self):
        '''点击地图列表中的最后一列,点击打开,查看能否打开地图页面'''
        self.map_management('admin','admin123456')    #进入地图管理界面
        self.driver.find_element_by_css_selector('#map_list div:last-child div div div.col-3 div input.btn.btn-primary.btn-open').click()   #点击地图列表最后一行的打开按钮
        sleep(2)
        # self.driver.implicitly_wait(10)
        # print('点击创建地图后的操作句柄:',self.driver.window_handles)
        # print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])  #切换至编辑地图界面
        # print('当前操作句柄:',self.driver.current_window_handle)
        sleep(1)
        #断言是否打开地图
        link1=self.driver.find_element_by_css_selector('.layer-title span')
        self.assertIn('图层',link1.text)
        self.add_img()
        self.save_img('打开编辑地图成功')
        sleep(2)
        self.driver.close() #关闭创建地图界面
        self.driver.switch_to.window(self.driver.window_handles[0])  #切换至首页


#用例11：打开某一地图页面,点击选择图层,修改【底图】、【图层】、【数据】,点击确定,最后点击保存底图,查看是否完成修改
    @BeautifulReport.add_test_img('修改地图') 
    def test_11_editor_map(self):
        '''打开某一地图页面,点击选择图层,修改【底图】、【图层】、【数据】,点击确定,最后点击保存底图,查看是否完成修改'''
        self.map_management('admin','admin123456')    #进入地图管理界面
        self.driver.find_element_by_css_selector('#map_list div:last-child div div div.col-3 div input.btn.btn-primary.btn-open').click()   #点击地图列表最后一行的打开按钮
        sleep(2)
        # self.driver.implicitly_wait(10)
        # print('点击创建地图后的操作句柄:',self.driver.window_handles)
        # print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[1])  #切换至编辑地图界面
        # print('当前操作句柄:',self.driver.current_window_handle)
        sleep(1)
#断言是否打开地图
        link1=self.driver.find_element_by_css_selector('.layer-title span')
        self.assertIn('图层',link1.text)
        self.add_img()
#测试从图层列表中直接删除图层/数据
        self.driver.find_element_by_css_selector('.layer-list div:last-child a').click()  #点击删除最后一行图层
        sleep(1)
        self.driver.find_element_by_css_selector('.layer-list div:last-child a').click()  #点击删除最后一行图层
        sleep(1)
        self.add_img()
#测试从首页切换底图
        wait=WebDriverWait(self.driver,400,0.5)            #显示等待时间直到底图出现
        wait.until(EC.visibility_of_any_elements_located((By.ID,'basemap_wrapper'))) 
        el=self.driver.find_element_by_id('basemap_wrapper')             #鼠标移动至下方的天地图处
        ActionChains(self.driver).move_to_element(el)
        el.click()
        self.driver.find_element_by_id('basemap_tdt_vec').click()    #点击天地图矢量
        self.driver.implicitly_wait(3)
        self.add_img()
#从选择图层中重新添加图层和数据
        self.driver.find_element_by_id('btn_map_addLayer').click()   #点击选择图层
        wait=WebDriverWait(self.driver,400,0.5)            #显示等待时间直到图层选择弹窗出现
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_layer_select'))) 
#重新选择图层
        self.driver.find_element_by_id('profile-tab').click()  #点击图层按钮
        #显示等待时间直到图层列表出现
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.ID,'layer_container_list'))) 
        #选择图层
        self.driver.find_element_by_css_selector('#layer_container_list div:nth-child(1)').click()
        sleep(1)
#重新选择数据
        self.driver.find_element_by_id('contact-tab').click()  #点击数据按钮
        #显示等待时间直到数据列表出现
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.ID,'data_container_list'))) 
        #选择数据
        self.driver.find_element_by_css_selector('#data_container_list  div:nth-child(3)').click()
        sleep(1)
        self.driver.find_element_by_css_selector('#btn_layer_select').click()   #点击确定按钮
        sleep(3)
#点击保存地图
        self.driver.find_element_by_id('btn_map_p_save').click()   #点击保存地图按钮
        sleep(3)
        #显示等待时间直到保存地图弹窗出现
        wait=WebDriverWait(self.driver,10,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_layer_form'))) 
        self.driver.implicitly_wait(2)
        sleep(3)
        el=self.driver.find_element_by_id('input_map_name')
        el.clear()
        sleep(2)
        el.send_keys('修改地图发布名称')   #在地图名称输入框输入
        sleep(6)
        self.driver.find_element_by_id('input_map_description').clear()   #清除地图描述输入框
        sleep(2)
        self.driver.find_element_by_id('input_map_description').send_keys('修改地图发布描述')   #在地图描述输入框输入
        sleep(6)
        self.driver.implicitly_wait(5)
        self.add_img()
        self.driver.find_element_by_id('btn_map_save').click()   #点击保存按钮
#断言是否发布成功
        sleep(4)
        wait=WebDriverWait(self.driver,400,0.5)            #显示等待时间直到弹窗出现
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('地图保存成功',link1.text)
        #回到首页查看是否在图层列表中已添加成功
        print('当前操作句柄:',self.driver.current_window_handle)
        self.driver.close()  #关闭当前页面
        self.driver.switch_to.window(self.driver.window_handles[0])  #切换至首页界面
        self.driver.refresh()   #刷新当前页面
        self.driver.implicitly_wait(2)   #隐式等待2秒
        self.driver.find_element_by_link_text('地图管理').click()   #点击地图管理按钮
        link2=self.driver.find_element_by_css_selector('#map_list div:last-child div div div.col-9 div.pl-xl-3 div.user-avatar-address p')  #定位图层列表最后一行的图层描述
        self.assertIn('修改地图发布描述',link2.text)
        self.add_img()
        self.save_img('修改地图发布成功')
        sleep(3)


#用例12：在图层列表中点击最后一行图层对应删除按钮,查看是否删除成功
    @BeautifulReport.add_test_img('删除地图') 
    def test_12_delete_map(self):
        '''在图层列表中点击最后一行图层对应删除按钮,查看是否删除成功'''
        self.map_management('admin','admin123456')    #进入地图管理界面
        self.driver.find_element_by_css_selector('#map_list div:last-child div div div.col-3 div input.btn.btn-danger.btn-delete').click()   #点击地图列表最后一行的删除按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        self.driver.implicitly_wait(2)   #隐式等待2秒
        alert.accept()               # 确认删除地图
        #显示等待时间到进入系统主界面
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link1.text)
        self.add_img()
        self.save_img('地图删除成功') 
        sleep(1)

     

if __name__ == '__main__':
    unittest.main(argv=['ignored','-v'],exit=False)
    print('')



