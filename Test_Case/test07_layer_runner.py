'''
图层管理功能测试分为以下几种情况:
(1)点击图层管理,查看能否正常进入图层管理界面
(2)点击图层管理中图层列表中的预览按钮,查看能否正常加载预览图
(3)在图层预览中查看能否正常放大或缩小预览图
(4)在图层管理的搜索框中输入图层标题关键字,查看能否成功完成筛选
(5)点击图层列表中的删除按钮,查看能否完成图层删除
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


class LayerCase(unittest.TestCase):
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
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('./图层管理/img'), img_name))    #os.path.abspath('')截图存放路径
             
#打开浏览器至数据管理界面
    def layer_management(self,username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys(username)  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys(password)  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        # #显示等待时间到进入系统主界面
        # wait=WebDriverWait(self.driver,40,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        sleep(3)
        self.driver.implicitly_wait(2)   #隐式等待2秒
        self.driver.find_element_by_link_text('图层管理').click()   #点击图层管理按钮
        sleep(2)
        self.driver.implicitly_wait(2)   #隐式等待2秒 
        sleep(1)  

#用例1：点击图层管理,查看能否正常进入图层管理界面
    @BeautifulReport.add_test_img('图层管理主界面') 
    def test_01_page_layer(self):
        '''点击图层管理,查看能否正常进入图层管理界面'''
        self.layer_management('admin','admin123456')    #进入数据管理界面
        link1=self.driver.find_element_by_id('page_layer')  #断言是否成功进入数据管理界面
        self.assertIn('标题', link1.text)
        self.add_img()
        self.save_img('图层管理主界面') 
        sleep(2)

#用例2：点击图层管理中图层列表中的预览按钮,查看能否正常加载预览图
    @BeautifulReport.add_test_img('查看图层预览') 
    def test_02_preview(self):
        '''点击图层管理中图层列表中的预览按钮,查看能否正常加载预览图'''
        self.layer_management('admin','admin123456')    #进入图层管理界面
        self.driver.find_element_by_css_selector('#layer_list > div:last-child input:first-child').click()   #点击图层列表中最后一列图层的预览按钮
       #显示等待时间到预览图加载完成
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'layer_preview_map'))) 
        sleep(2) 
        self.save_img('图层预览成功') 
        self.add_img()
        sleep(2)


#用例3：在图层预览中查看能否正常放大或缩小预览图
    @BeautifulReport.add_test_img('操作图层预览') 
    def test_03_preview(self):
        '''在图层预览中查看能否正常放大或缩小预览图'''
        self.layer_management('admin','admin123456')    #进入图层管理界面
        self.driver.find_element_by_css_selector('#layer_list > div:last-child input:first-child').click()   #点击图层列表中最后一列图层的预览按钮
        #显示等待时间到预览图加载完成
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'layer_preview_map'))) 
        sleep(2)
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()  #点击放大按钮
        sleep(1)
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()  #点击放大按钮
        sleep(1)
        self.driver.find_element_by_class_name('leaflet-control-zoom-in').click()  #点击放大按钮
        sleep(1)
        self.add_img()
        self.save_img('图层预览放大成功')
        sleep(2)
        self.driver.find_element_by_class_name('leaflet-control-zoom-out').click()  #点击缩小按钮
        sleep(1)
        self.driver.find_element_by_class_name('leaflet-control-zoom-out').click()  #点击缩小按钮
        sleep(1)
        self.add_img()
        self.save_img('图层预览缩小成功')
        sleep(2) 
        
#用例4：在图层管理的搜索框中输入图层名称、标题、描述关键字,查看能否成功完成筛选
    @BeautifulReport.add_test_img('搜索查询图层') 
    def test_04_search(self):
        '''在搜索框中输入关键字,查看是否能完成查询'''
        self.layer_management('admin','admin123456')    #进入图层管理界面
#测试搜索查询图层名称关键字
        self.driver.find_element_by_id('input_layer_search').send_keys('test')   #点击搜索输入框输入图层名称关键字
        self.driver.find_element_by_id('btn_layer_search').click()       #点击搜索按钮
        sleep(1)
        #断言搜索后显示的图层列表第一行的标题中包含polyline
        link1=self.driver.find_element_by_css_selector('#layer_list > div:first-child h2:first-child')   #定位在筛选后列表第一列的图层名称位置
        self.assertIn('test', link1.text)
        self.add_img()
        self.save_img('搜索查询图层名称关键字') 
        sleep(2)
#测试搜索查询图层标题关键字
        self.driver.refresh()   #刷新当前页面
        self.driver.implicitly_wait(2)   #隐式等待2秒
        self.driver.find_element_by_id('input_layer_search').send_keys('边框')   #点击搜索输入框输入标题关键字
        self.driver.find_element_by_id('btn_layer_search').click()       #点击搜索按钮
        sleep(1)
        #断言搜索后显示的图层列表第一行的标题中包含polyline
        link1=self.driver.find_element_by_css_selector('#layer_list > div:first-child span:first-child')   #定位在筛选后列表的一列的标题位置
        self.assertIn('边框', link1.text)
        self.add_img()
        self.save_img('搜索查询图层标题关键字') 
        sleep(2)
#测试搜索查询图层描述关键字
        self.driver.refresh()   #刷新当前页面
        self.driver.implicitly_wait(2)   #隐式等待2秒
        self.driver.find_element_by_id('input_layer_search').send_keys('测试')   #点击搜索输入框输入标题关键字
        self.driver.find_element_by_id('btn_layer_search').click()       #点击搜索按钮
        sleep(1)
        #断言搜索后显示的图层列表第一行的标题中包含polyline
        link1=self.driver.find_element_by_css_selector('#layer_list > div:first-child p')   #定位在筛选后列表第一列的图层描述位置
        self.assertIn('测试', link1.text)
        self.add_img()
        self.save_img('搜索查询图层描述关键字') 
        sleep(2)


   
# 用例5:点击测试图层对应的共享按钮,查看是否弹出共享部门选择弹窗
    @BeautifulReport.add_test_img('共享图层弹窗') 
    def test_05_btn_share_pop(self):
        '''点击测试图层对应的共享按钮,查看是否弹出共享部门选择弹窗'''
        self.layer_management('admin','admin123456')    #进入图层管理界面
#先新增图层
        self.driver.find_element_by_link_text('数据管理').click() #点击数据管理界面
          #显示时间等待进入数据管理界面
        wait=WebDriverWait(self.driver,400,0.5)
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
          #点击发布数据按钮
        self.driver.implicitly_wait(10)   #隐式等待10秒
         #显示等待时间直到加载完成
        wait=WebDriverWait(self.driver,400,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME,'leaflet-styleeditor-footer'))) 
        self.driver.find_element_by_id('btn_publish').click() 
        #显示等待时间直到弹出框显示
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_layer_form'))) 
        #断言是否弹出发布图层弹窗
        link1=self.driver.find_element_by_id('input_layer_form')   
        self.assertIn('样式名称',link1.text)
        # self.save_img('发布图层弹窗')
        ele1=self.driver.find_element_by_id('input_layer_name')   #定位图层名称
        ele1.clear()
        ele1.send_keys('共享图层名称')  #修改图层名称
        self.driver.find_element_by_id('input_layer_name').clear()  #清除图层标题输入框
        self.driver.find_element_by_id('input_layer_name').send_keys('共享图层标题1')  #输入修改后的图层标题
        self.driver.find_element_by_id('input_layer_style').clear()   #清除样式名称输入框 
        self.driver.find_element_by_id('input_layer_style').send_keys('共享图层样式')   #输入修改后的样式名称
        self.driver.find_element_by_id('input_layer_description').send_keys('共享图层描述')
        sleep(1)
        self.driver.find_element_by_id('btn_layer_save').click()           #点击发布按钮
#显示等待时间到弹出框显示数据发布成功
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('图层发布成功', link1.text)
        self.add_img()
        # self.save_img('图层发布成功')
        sleep(1)
        self.driver.close() #删除当前发布图层界面
#回到首页的图层管理去验证是否已发布成功
        self.driver.switch_to.window(self.driver.window_handles[0])            #回到主界面
        self.driver.implicitly_wait(2)   #隐式等待2秒
        sleep(3)
        self.driver.find_element_by_link_text('图层管理').click()           #点击图层管理按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒
#断言发布图层列表中是否存在刚刚新发布的图层
        link2=self.driver.find_element_by_css_selector('#layer_list div:last-child div div div.col-9 div.pl-xl-3 div.m-b-0 div h2')   #定位图层列表最后一列图层名称位置
        self.assertIn('共享图层标题1', link2.text)
        self.add_img()
        sleep(1)
        self.driver.implicitly_wait(2)   #隐式等待2秒
#断言判定点击刚刚新增的图层共享按钮是否弹出共享图层弹窗
        self.driver.find_element_by_css_selector('#layer_list > div:last-child input:nth-child(2)').click()      #点击新增图层的共享按钮
        sleep(2)
        link3=self.driver.find_element_by_css_selector('#modal_share h5')      #断言判定是否出现弹窗
        self.assertIn('共享',link3.text)
        self.add_img()
        # self.save_img('共享图层弹窗')

# 用例6:在共享弹窗中不选择部门,点击保存,查看是否提示请选择部门
    @BeautifulReport.add_test_img('共享图层部门为空') 
    def test_06_table_share_department_null(self):
        '''在共享弹窗中不选择部门,点击保存,查看是否提示请选择部门'''
        self.layer_management('admin','admin123456')    #进入图层管理界面
        self.driver.find_element_by_css_selector('#layer_list > div:last-child input:nth-child(2)').click() #点击新增图层的共享按钮
        sleep(2)
        self.add_img()
        self.driver.find_element_by_id('btn_share_save').click()   #点击保存按钮
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
         #断言是否提示编辑成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('请选择要分享的部门',link1.text)
        self.add_img()
        # self.save_img('共享图层部门为空')

# 用例7:在共享弹窗中选择一级部门,权限选择读,点击保存,查看是否保存成功(用该部门下的测试用户重新登录查看能否查看共享的图层)
    @BeautifulReport.add_test_img('共享一级部门读图层') 
    def test_07_share_first_department_read(self):
        '''在共享弹窗中选择一级部门,权限选择读,点击保存,查看是否保存成功'''
        self.layer_management('admin','admin123456')    #进入图层管理界面
        self.driver.find_element_by_css_selector('#layer_list > div:last-child input:nth-child(2)').click() #点击新增图层的共享按钮
        sleep(2)
        self.driver.find_element_by_css_selector('#table_share_department tbody tr:nth-child(1) td:first-child').click()   #点击选择第一大部门
        sleep(1)
        self.add_img()
        self.driver.find_element_by_id('btn_share_save').click()   #点击保存按钮
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('共享成功',link1.text)
        self.add_img()
        # self.save_img('共享一级部门读图层成功')
#回到我的共享界面查看我的共享界面是否存在刚刚共享的图层
        self.driver.find_element_by_link_text('我的共享').click()     #进入我的共享界面
        sleep(2)
        #验证共享图层标题是否正确
        lin1=self.driver.find_element_by_css_selector('#table_share  tbody tr:first-child  td:nth-child(1)') #定位我的共享第一列的资源名称位置
        self.assertIn('共享图层标题1',lin1.text)
        sleep(0.2)
        #验证共享图层操作是否正确
        lin2=self.driver.find_element_by_css_selector('#table_share  tbody tr:first-child  td:nth-child(4)')
        self.assertIn('只读',lin2.text)  
        self.add_img()
        sleep(0.5)
#使用刚刚共享的部门下面账户登录查看能否查看图层
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#使用第一大部门下第一小组成员账户登录
        self.layer_management('ywyz','123')    #使用第一大部门下第一小组成员账户登录
        # self.driver.find_element_by_link_text('图层管理').click()  #点击进入图层管理界面
        sleep(1)
        #验证数据名称是否为共享的图层名称
        link2=self.driver.find_element_by_css_selector('#layer_list div:first-child div div div.col-9 div.pl-xl-3 div.m-b-0 div h2')   #定位图层列表第一列图层名称位置
        self.assertIn('共享图层标题1',link2.text)   #验证数据名称是否为共享的图层名称
        self.add_img()
#使用第一大部门下第二小组成员账户登录
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
        #使用第一大部门下第二小组成员账户登录
        self.layer_management('ywez','123')    #使用第一大部门下第一小组成员账户登录
        # self.driver.find_element_by_link_text('数据管理').click()  #点击进入数据管理界面
        sleep(1)
        #验证数据名称是否为共享的图层名称
        link2=self.driver.find_element_by_css_selector('#layer_list div:first-child div div div.col-9 div.pl-xl-3 div.m-b-0 div h2')   #定位图层列表第一列图层名称位置
        self.assertIn('共享图层标题1',link2.text)   #验证数据名称是否为共享的图层名称
        self.add_img()
      
# 用例8:在共享弹窗中选择一级部门,权限选择写,点击保存,查看是否保存成功(用该部门下的测试用户重新登录查看能否编辑共享的图层)
    @BeautifulReport.add_test_img('共享一级部门读图层') 
    def test_08_share_first_department_write(self):
        '''在共享弹窗中选择一级部门,权限选择读,点击保存,查看是否保存成功'''
        self.layer_management('admin','admin123456')    #进入图层管理界面
        sleep(1)
        self.driver.find_element_by_css_selector('#layer_list > div:last-child input:nth-child(2)').click() #点击新增图层的共享按钮
        sleep(2)
        self.driver.find_element_by_css_selector('#table_share_department tbody tr:nth-child(1) td:first-child').click()   #点击选择第一大部门
        sleep(1)
        self.driver.find_element_by_css_selector('#input_share_form div div label:nth-child(2) span').click()   #点击写按钮
        self.add_img()
        self.driver.find_element_by_id('btn_share_save').click()   #点击保存按钮
         #显示等待时间直到提示弹窗出现
        wait=WebDriverWait(self.driver,40,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('共享成功',link1.text)
        self.add_img()
        # self.save_img('共享一级部门读写图层成功')
#回到我的共享界面查看我的共享界面是否存在刚刚共享的图层
        self.driver.find_element_by_link_text('我的共享').click()     #进入我的共享界面
        sleep(2)
        #验证共享图层标题是否正确
        lin1=self.driver.find_element_by_css_selector('#table_share  tbody tr:first-child  td:nth-child(1)') #定位我的共享第一列的资源名称位置
        self.assertIn('共享图层标题1',lin1.text)
        sleep(0.2)
        #验证共享图层操作是否正确
        lin2=self.driver.find_element_by_css_selector('#table_share  tbody tr:first-child  td:nth-child(4)')
        self.assertIn('读写',lin2.text)  
        self.add_img()
        sleep(0.5)
#使用刚刚共享的部门下面账户登录查看能否查看图层
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#使用第一大部门下第一小组成员账户登录
        self.layer_management('ywyz','123')    #使用第一大部门下第一小组成员账户登录
        # self.driver.find_element_by_link_text('图层管理').click()  #点击进入图层管理界面
        sleep(1)
        #验证数据名称是否为共享的图层名称
        link2=self.driver.find_element_by_css_selector('#layer_list div:first-child div div div.col-9 div.pl-xl-3 div.m-b-0 div h2')   #定位图层列表第一列图层名称位置
        self.assertIn('共享图层标题1',link2.text)   #验证数据名称是否为共享的图层名称
        self.add_img()
#使用第一大部门下第二小组成员账户登录
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
        #使用第一大部门下第二小组成员账户登录
        self.layer_management('ywez','123')    #使用第一大部门下第一小组成员账户登录
        # self.driver.find_element_by_link_text('数据管理').click()  #点击进入数据管理界面
        sleep(1)
        #验证数据名称是否为共享的图层名称
        link2=self.driver.find_element_by_css_selector('#layer_list div:first-child div div div.col-9 div.pl-xl-3 div.m-b-0 div h2')   #定位图层列表第一列图层名称位置
        self.assertIn('共享图层标题1',link2.text)   #验证数据名称是否为共享的图层名称
        self.add_img()


# 用例9:在共享弹窗中选择二级部门,权限选择读,点击保存,查看是否保存成功(用该部门下的测试用户重新登录查看能否查看共享的图层)
    @BeautifulReport.add_test_img('共享一级部门读图层') 
    def test_09_share_second_department_read(self):
        '''在共享弹窗中选择二级部门,权限选择读,点击保存,查看是否保存成功'''
        self.layer_management('admin','admin123456')    #进入图层管理界面
        sleep(1)
#进入数据管理界面发布针对第二部门共享的图层
        self.driver.find_element_by_link_text('数据管理').click() #点击数据管理界面
          #显示时间等待进入数据管理界面
        wait=WebDriverWait(self.driver,400,0.5)
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
          #点击发布数据按钮
        self.driver.implicitly_wait(10)   #隐式等待10秒
         #显示等待时间直到加载完成
        wait=WebDriverWait(self.driver,400,0.5)           
        wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME,'leaflet-styleeditor-footer'))) 
        self.driver.find_element_by_id('btn_publish').click() 
        #显示等待时间直到弹出框显示
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'input_layer_form'))) 
        #断言是否弹出发布图层弹窗
        link1=self.driver.find_element_by_id('input_layer_form')   
        self.assertIn('样式名称',link1.text)
        # self.save_img('发布图层弹窗')
        ele1=self.driver.find_element_by_id('input_layer_name')   #定位图层名称
        ele1.clear()
        ele1.send_keys('共享图层名称2')  #修改图层名称
        self.driver.find_element_by_id('input_layer_name').clear()  #清除图层标题输入框
        self.driver.find_element_by_id('input_layer_name').send_keys('共享图层标题2')  #输入修改后的图层标题
        self.driver.find_element_by_id('input_layer_style').clear()   #清除样式名称输入框 
        self.driver.find_element_by_id('input_layer_style').send_keys('共享图层样式2')   #输入修改后的样式名称
        self.driver.find_element_by_id('input_layer_description').send_keys('共享图层描述2')
        sleep(1)
        self.driver.find_element_by_id('btn_layer_save').click()           #点击发布按钮
#显示等待时间到弹出框显示数据发布成功
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('图层发布成功', link1.text)
        self.add_img()
        # self.save_img('图层发布成功')
        sleep(1)
        self.driver.close() #删除当前发布图层界面
#回到首页的图层管理去验证是否已发布成功
        self.driver.switch_to.window(self.driver.window_handles[0])            #回到主界面
        self.driver.implicitly_wait(2)   #隐式等待2秒
        sleep(3)
        self.driver.find_element_by_link_text('图层管理').click()           #点击图层管理按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒
#断言发布图层列表中是否存在刚刚新发布的图层
        link2=self.driver.find_element_by_css_selector('#layer_list div:last-child div div div.col-9 div.pl-xl-3 div.m-b-0 div h2')   #定位图层列表最后一列图层名称位置
        self.assertIn('共享图层标题2', link2.text)
        self.add_img()
        sleep(1)
        self.driver.implicitly_wait(2)   #隐式等待2秒
#对新增的共享图层进行共享操作
        self.driver.find_element_by_css_selector('#layer_list > div:last-child input:nth-child(2)').click() #点击新增图层的共享按钮
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
        # self.save_img('共享二级部门读图层成功')
        sleep(1)
#回到我的共享界面查看我的共享界面是否存在刚刚共享的图层
        self.driver.find_element_by_link_text('我的共享').click()     #进入我的共享界面
        sleep(2)
        #验证共享图层标题是否正确
        lin1=self.driver.find_element_by_css_selector('#table_share  tbody tr:last-child  td:nth-child(1)') #定位我的共享第一列的资源名称位置
        self.assertIn('共享图层标题2',lin1.text)
        sleep(0.2)
        #验证共享图层操作是否正确
        lin2=self.driver.find_element_by_css_selector('#table_share  tbody tr:last-child  td:nth-child(4)')
        self.assertIn('只读',lin2.text)  
        self.add_img()
        sleep(0.5)
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#使用第一大部门下第一小组成员账户登录
        self.layer_management('ywyz','123')    #使用第一大部门下第一小组成员账户登录
        # self.driver.find_element_by_link_text('图层管理').click()  #点击进入图层管理界面
        sleep(1)
        #验证数据名称是否为共享的图层名称
        link2=self.driver.find_element_by_css_selector('#layer_list div:last-child div div div.col-9 div.pl-xl-3 div.m-b-0 div h2')   #定位图层列表最后一列图层名称位置
        self.assertIn('共享图层标题1',link2.text)   #验证数据名称是否为共享的图层名称
        self.add_img()
#使用第一大部门下第二小组成员账户登录
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
        #使用第一大部门下第二小组成员账户登录
        self.layer_management('ywez','123')    #使用第一大部门下第一小组成员账户登录
        # self.driver.find_element_by_link_text('数据管理').click()  #点击进入数据管理界面
        sleep(1)
        #验证数据名称是否为共享的图层名称
        link2=self.driver.find_element_by_css_selector('#layer_list div:last-child div div div.col-9 div.pl-xl-3 div.m-b-0 div h2')   #定位图层列表最后一列图层名称位置
        self.assertIn('共享图层标题2',link2.text)   #验证数据名称是否为共享的图层名称
        self.add_img()     

# 用例10:在共享弹窗中选择二级部门,权限选择写,点击保存,查看是否保存成功(用该部门下的测试用户重新登录查看能否编辑共享的图层)
    @BeautifulReport.add_test_img('共享一级部门读图层') 
    def test_10_share_second_department_write(self):
        '''在共享弹窗中选择二级部门,权限选择写,点击保存,查看是否保存成功'''
        self.layer_management('admin','admin123456')    #进入图层管理界面
        self.driver.find_element_by_css_selector('#layer_list > div:last-child input:nth-child(2)').click() #点击新增图层的共享按钮
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
        # self.save_img('共享二级部门写图层成功')
#回到我的共享界面查看我的共享界面是否存在刚刚共享的图层
        self.driver.find_element_by_link_text('我的共享').click()     #进入我的共享界面
        sleep(2)
        #验证共享图层标题是否正确
        lin1=self.driver.find_element_by_css_selector('#table_share  tbody tr:last-child  td:nth-child(1)') #定位我的共享第一列的资源名称位置
        self.assertIn('共享图层标题2',lin1.text)
        sleep(0.2)
        #验证共享图层操作是否正确
        lin2=self.driver.find_element_by_css_selector('#table_share  tbody tr:last-child  td:nth-child(4)')
        self.assertIn('读写',lin2.text)  
        self.add_img()
        sleep(0.5)
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
#使用第一大部门下第一小组成员账户登录
        self.layer_management('ywyz','123')    #使用第一大部门下第一小组成员账户登录
        # self.driver.find_element_by_link_text('图层管理').click()  #点击进入图层管理界面
        sleep(1)
        #验证数据名称是否为共享的图层名称
        link2=self.driver.find_element_by_css_selector('#layer_list div:last-child div div div.col-9 div.pl-xl-3 div.m-b-0 div h2')   #定位图层列表最后一列图层名称位置
        self.assertIn('共享图层标题1',link2.text)   #验证数据名称是否为共享的图层名称
        self.add_img()
#使用第一大部门下第二小组成员账户登录
#退出登录
        self.driver.find_element_by_id('avatar_user').click()                #点击头像按钮
        sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('avatar_user')).pause(3).perform()    #使鼠标悬浮在头像处
        self.driver.find_element_by_link_text('退出登录').click()             #点击退出登录按钮
        sleep(3)
        #使用第一大部门下第二小组成员账户登录
        self.layer_management('ywez','123')    #使用第一大部门下第一小组成员账户登录
        # self.driver.find_element_by_link_text('数据管理').click()  #点击进入数据管理界面
        sleep(1)
        #验证数据名称是否为共享的图层名称
        link2=self.driver.find_element_by_css_selector('#layer_list div:last-child div div div.col-9 div.pl-xl-3 div.m-b-0 div h2')   #定位图层列表最后一列图层名称位置
        self.assertIn('共享图层标题2',link2.text)   #验证数据名称是否为共享的图层名称
        self.add_img()     

#用例11：在我的共享界面查看点击取消刚刚共享的图层能否成功
    @BeautifulReport.add_test_img('取消共享图层') 
    def test_11_share_delete(self):
        '''在我的共享界面查看点击取消刚刚共享的图层能否成功'''
        self.layer_management('admin','admin123456')    #进入图层管理界面
        sleep(1)
        self.driver.find_element_by_link_text('我的共享').click()
        self.add_img()
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
        # self.save_img('取消共享成功') 
        sleep(2)
#取消测试共享数据
        self.driver.find_element_by_css_selector('#table_share tbody tr:first-child a').click()  #点击第一列的取消共享按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取取消确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认取消
        self.add_img()
        sleep(1)
#
        self.driver.find_element_by_css_selector('#table_share tbody tr:first-child a').click()  #点击第一列的取消共享按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取取消确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认取消
        self.add_img()
        sleep(1)
#
        self.driver.find_element_by_css_selector('#table_share tbody tr:first-child a').click()  #点击第一列的取消共享按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取取消确认弹出窗口
        print(alert.text)  # 打印窗口信息
        alert.accept()  # 确认取消
        self.add_img()
        sleep(1)

#用例12：点击图层列表中的删除按钮,查看能否完成图层删除
    @BeautifulReport.add_test_img('图层删除') 
    def test_12_delete_layer(self):
        '''点击图层列表中的删除按钮,查看能否完成图层删除'''
        self.layer_management('admin','admin123456')    #进入图层管理界面
        self.driver.find_element_by_link_text('数据管理').click() #点击数据管理界面
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
        # self.save_img('发布图层弹窗')
        ele1=self.driver.find_element_by_id('input_layer_name')   #定位图层名称
        ele1.clear()
        ele1.send_keys('测试发布图层')  #修改图层名称
        self.driver.find_element_by_id('input_layer_name').clear()  #清除图层标题输入框
        self.driver.find_element_by_id('input_layer_name').send_keys('测试删除图层标题')  #输入修改后的图层标题
        self.driver.find_element_by_id('input_layer_style').clear()   #清除样式名称输入框 
        self.driver.find_element_by_id('input_layer_style').send_keys('测试删除图层样式')   #输入修改后的样式名称
        self.driver.find_element_by_id('input_layer_description').send_keys('测试删除图层')
        sleep(1)
        self.driver.find_element_by_id('btn_layer_save').click()           #点击发布按钮
#显示等待时间到弹出框显示数据发布成功
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('图层发布成功', link1.text)
        self.add_img()  
        # self.save_img('图层发布成功')
        sleep(1)
        self.driver.close() #关闭当前发布图层页面
#回到首页的图层管理去验证是否已发布成功
        self.driver.switch_to.window(self.driver.window_handles[0])            #回到主界面
        self.driver.implicitly_wait(2)   #隐式等待2秒
        sleep(3)
        self.driver.find_element_by_link_text('图层管理').click()           #点击图层管理按钮
        sleep(1)
        #将滚动条移动到页面的顶部  
        js="var q=document.documentElement.scrollTop=0"  
        self.driver.execute_script(js)  
        sleep(1)  
        #断言发布图层列表中是否存在刚刚新发布的图层
        link2=self.driver.find_element_by_css_selector('#layer_list div:last-child div div div.col-9 div.pl-xl-3 div.m-b-0 div h2')   #定位图层列表最后一列图层名称位置
        self.assertIn('测试删除图层标题', link2.text)
        sleep(1)
        self.add_img()
        self.driver.implicitly_wait(2)   #隐式等待2秒
        self.driver.find_element_by_css_selector('#layer_list > div:last-child input:last-child').click()   #点击图层列表最后一列的删除按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        self.driver.implicitly_wait(2)   #隐式等待2秒
        alert.accept()               # 确认删除图层
         #显示等待时间到弹出框出现
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify')))
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link1.text)
        self.add_img()
        sleep(2)
#删除刚刚新增的测试共享图层2
        self.driver.find_element_by_css_selector('#layer_list > div:last-child input:last-child').click()   #点击图层列表最后一列的删除按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        self.driver.implicitly_wait(2)   #隐式等待2秒
        alert.accept()               # 确认删除图层
         #显示等待时间到弹出框出现
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify')))
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link1.text)
        self.add_img()
        sleep(2)

#用例13：删除已共享的图层，查看是否提示改图层正常共享，不能直接删除
    @BeautifulReport.add_test_img('已共享图层删除') 
    def test_13_delete_share_layer(self):
        '''删除已共享的图层，查看是否提示改图层正常共享，不能直接删除'''
        self.layer_management('admin','admin123456')    #进入图层管理界面
#先将图层共享
        self.driver.find_element_by_css_selector('#layer_list > div:last-child input:nth-child(2)').click() #点击新增图层的共享按钮
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
        sleep(2)
#对共享的图层点击删除按钮
        self.driver.find_element_by_css_selector('#layer_list > div:last-child input:last-child').click()   #点击图层列表最后一列的删除按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        self.driver.implicitly_wait(2)   #隐式等待2秒
        alert.accept()               # 确认删除图层
         #显示等待时间到弹出框出现
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify')))
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('不能直接删除', link1.text)
        self.add_img()
#回到我的共享界面点击取消共享然后再尝试删除
        self.driver.find_element_by_link_text('我的共享').click()
        self.add_img()
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
        # self.save_img('取消共享成功') 
        sleep(2)
#删除刚取消共享的图层
        self.driver.find_element_by_css_selector('#layer_list > div:last-child input:last-child').click()   #点击图层列表最后一列的删除按钮
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        self.driver.implicitly_wait(2)   #隐式等待2秒
        alert.accept()               # 确认删除图层
         #显示等待时间到弹出框出现
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify')))
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link1.text)
        self.add_img()
        sleep(1)









if __name__ == '__main__':
    unittest.main(argv=['ignored','-v'],exit=False)
    print('')
