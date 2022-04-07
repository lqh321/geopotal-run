# -*- coding: utf-8 -*-
"""HTMLTestRunner 截图版示例 selenium 版"""
from fileinput import filename
from selenium import webdriver
import unittest
import time
from HTMLTestRunnerCN import HTMLTestRunner
import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.expected_conditions import alert_is_present
from BeautifulReport import BeautifulReport


class test13_Articlecase(unittest.TestCase):
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

   #定义错误截图方法
    def save_img(self, img_name):  
        """
         传入一个img_name, 并存储到默认的文件路径下
         :param img_name:
          :return:
         """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('./首页设置/文章管理/img'), img_name))    #os.path.abspath('')截图存放路径

#打开浏览器至数据管理界面
    def article_management(self,username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys(username)  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys(password)  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        #显示等待时间到进入系统主页
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        sleep(2)
        self.driver.find_element_by_link_text('首页设置').click()   #点击首页设置按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒 
        sleep(1)  
        self.driver.find_element_by_link_text('文章管理').click()         #点击文章管理按钮
         #显示等待时间到进入文章管理主页
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_article_save'))) 
        sleep(2)


# 发布文章
# 用例1:点击首页设置下的文章管理,查看能否正常进入文章管理界面
    @BeautifulReport.add_test_img('文章管理主界面') 
    def test_01_page_article(self):
        '''点击首页设置下的文章管理,查看能否正常进入文章管理界面'''
        self.article_management('admin','admin123456')    #进入文章管理界面
        link1=self.driver.find_element_by_css_selector('#page_h_article h4')
        self.assertIn('文章列表',link1.text)
        self.save_img('文章管理主界面')
        self.add_img()
    

# 用例2:在文章管理界面选择文章列表,点击发布文章,查看是否提示请输入文章标题
    @BeautifulReport.add_test_img('文章标题为空') 
    def test_02_articl_null(self):
        '''在文章管理界面选择文章列表,点击发布文章,查看是否提示请输入文章标题'''
        self.article_management('admin','admin123456')    #进入文章管理界面
#首先进入栏目管理界面添加一个测试栏目
        self.driver.find_element_by_link_text('栏目管理').click() #进入栏目管理界面
         #显示等待时间到进入栏目管理主页
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_channel_add'))) 
        sleep(1)
        self.driver.find_element_by_id('btn_channel_add').click()   #点击添加栏目按钮
        sleep(1)
        #显示等待时间到进入添加栏目弹窗
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'form_channel'))) 
        self.driver.find_element_by_id('input_channel_name').send_keys('测试添加文章栏目')   #输入栏目名称
        sleep(0.5)
        el=self.driver.find_element_by_id('input_channel_index')   #定位栏目序号位置
        el.clear() #清空栏目序号输入框
        el.send_keys('6')       #输入栏目序号
        self.driver.find_element_by_css_selector('#form_channel div:nth-child(3) label').click()     #点击勾选设为导航
        sleep(0.5)
        self.add_img()
        self.driver.find_element_by_id('btn_channel_save').click()   #点击保存按钮
        sleep(0.2)
        #显示等待时间到出现提示框
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言判定是否提示添加成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功',link1.text)
        self.add_img()
#回到文章管理界面，使用刚刚新增的栏目来添加文章
        self.driver.find_element_by_link_text('文章管理').click()  #回到文章管理界面
        #显示等待时间到进入文章管理主页
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_article_save'))) 
        sleep(1)
        #选择栏目
        self.driver.find_element_by_id('select_article_channel').click() #点击栏目选择框
        sleep(0.5)
        self.driver.find_element_by_css_selector('#select_article_channel option:last-child').click()  #点击刚刚新增的栏目
        sleep(0.5)
        self.driver.find_element_by_css_selector('#btn_create_article span').click()    #点击新建文章
        sleep(0.5)
        self.driver.find_element_by_id('btn_article_save').click()          #点击发布文章
        sleep(0.5)
        #显示等待时间到出现提示框
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言判定是否有提示请输入文章标题
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('请输入文章标题',link1.text)
        self.add_img()
        self.save_img('请输入文章标题')
        
   

# 用例3:在文章管理界面选择文章列表,输入文章标题,点击发布文章,查看是否发布成功
    @BeautifulReport.add_test_img('输入文章标题') 
    def test_03_input_article_title(self):
        '''在文章管理界面选择文章列表,输入文章标题,点击发布文章,查看是否发布成功'''
        self.article_management('admin','admin123456')    #进入文章管理界面
          #选择栏目
        self.driver.find_element_by_id('select_article_channel').click() #点击栏目选择框
        sleep(0.5)
        self.driver.find_element_by_css_selector('#select_article_channel option:last-child').click()  #点击刚刚新增的栏目
        sleep(0.5)
        self.driver.find_element_by_css_selector('#btn_create_article span').click()    #点击新建文章
        sleep(0.5)
        self.driver.find_element_by_id('input_article_title').send_keys('测试发布文章1')      #输入文章标题
        sleep(0.5)
        self.add_img()
        self.driver.find_element_by_id('btn_article_save').click()          #点击发布文章
        sleep(0.2)
        #显示等待时间到出现提示框
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言判定是否有提示请输入文章标题
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('发布成功',link1.text)
        self.add_img()
        self.save_img('添加文章标题')
        #断言文章列表中是否存在刚刚新增的文章
        link2=self.driver.find_element_by_css_selector('#list_article li:first-child')   #断言文章列表中是否存在刚刚新增的文章
        self.assertIn('测试发布文章1',link2.text)

# 用例4:在文章管理界面选择文章列表,输入文章标题、文章内容,点击发布文章,查看是否发布成功
    @BeautifulReport.add_test_img('输入文章内容') 
    def test_04_input_article_content(self):
        '''在文章管理界面选择文章列表,输入文章标题、文章内容,点击发布文章,查看是否发布成功'''
        self.article_management('admin','admin123456')    #进入文章管理界面
          #选择栏目
        self.driver.find_element_by_id('select_article_channel').click() #点击栏目选择框
        sleep(0.5)
        self.driver.find_element_by_css_selector('#select_article_channel option:last-child').click()  #点击刚刚新增的栏目
        sleep(0.5)
        self.driver.find_element_by_css_selector('#btn_create_article span').click()    #点击新建文章
        sleep(0.5)
        self.driver.find_element_by_id('input_article_title').send_keys('测试发布文章2')      #输入文章标题
        self.driver.find_element_by_css_selector('#eidtor_article div.vditor-content div.vditor-ir pre').send_keys('测试发布文章2内容')  #输入文章内容
        sleep(0.5)
        self.driver.find_element_by_id('btn_article_save').click()          #点击发布文章
        sleep(0.5)
        #显示等待时间到出现提示框
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言判定是否有提示请输入文章标题
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('发布成功',link1.text)
        self.add_img()
        self.save_img('添加文章内容')
        #断言文章列表中是否存在刚刚新增的文章
        link2=self.driver.find_element_by_css_selector('#list_article li:nth-child(2)')   #断言文章列表中是否存在刚刚新增的文章
        self.assertIn('测试发布文章2',link2.text)

# 链接文章
# 用例5:回到栏目管理界面,找到刚刚添加文章的栏目,点击链接文章,查看是否弹出链接文章列表
    @BeautifulReport.add_test_img('链接文章弹窗') 
    def test_05_link_articl_pop(self):
        '''回到栏目管理界面,找到刚刚添加文章的栏目,点击链接文章,查看是否弹出链接文章列表'''
        self.article_management('admin','admin123456')    #进入文章管理界面
        #首先进入栏目管理界面
        self.driver.find_element_by_link_text('栏目管理').click() #进入栏目管理界面
         #显示等待时间到进入栏目管理主页
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_channel_add'))) 
        sleep(1)
        self.driver.find_element_by_css_selector('#table_channel tbody tr:last-child  td:last-child  a:nth-child(2)').click()   #点击测试的栏目链接文章按钮
        sleep(1)
        #断言判定是否弹出弹窗
        link1=self.driver.find_element_by_css_selector('#modal_link_select h5')   #断言判定是否进入链接文章弹窗
        self.assertIn('链接文章',link1.text)
        self.add_img()
        self.save_img('链接文章弹窗')
   
# 用例6:回到栏目管理界面,对刚刚添加文章的栏目下的某一文章点击勾选,查看是否链接文章成功
    @BeautifulReport.add_test_img('选择链接文章') 
    def test_06_link_articl(self):
        '''回到栏目管理界面,对刚刚添加文章的栏目下的某一文章点击勾选,查看是否链接文章成功'''
        self.article_management('admin','admin123456')    #进入文章管理界面
        #首先进入栏目管理界面
        self.driver.find_element_by_link_text('栏目管理').click() #进入栏目管理界面
         #显示等待时间到进入栏目管理主页
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_channel_add'))) 
        sleep(1)
        self.driver.find_element_by_css_selector('#table_channel tbody tr:last-child  td:last-child  a:nth-child(2)').click()   #点击测试的栏目链接文章按钮
        sleep(0.5)
         #显示等待时间到进入链接文章弹窗
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'table_channel_article'))) 
        link1=self.driver.find_element_by_css_selector('#modal_link_select h5')   #断言判定是否进入链接文章弹窗
        self.assertIn('链接文章',link1.text)
        #选择第一个文章设置链接
        self.driver.find_element_by_css_selector('#table_channel_article tbody tr:first-child  td:first-child input').click()   #点击选择文章列表第一列的文章
        self.add_img()
        self.driver.find_element_by_id('btn_channel_link_save').click()      #点击保存按钮
        sleep(0.5)
        #断言判定是否保存成功
        link2=self.driver.find_element_by_id('alter_notify')    #断言判定保存后是否出现提示框保存成功
        self.assertIn('修改成功',link2.text)
        self.add_img()
        self.save_img('链接文章')
        sleep(0.5)
        #断言判定栏目列表中链接文章栏是否显示刚刚链接的文章
        link3=self.driver.find_element_by_css_selector('#table_channel tbody tr:last-child td:nth-child(4)')       #定位刚刚新增栏目的链接文章栏
        self.assertIn('测试发布文章1',link3.text)  #判定链接文章栏是否存在刚刚新增的文章名
        #断言判定操作栏是否变为删除链接
        link4=self.driver.find_element_by_css_selector('#table_channel tbody tr:last-child td:last-child a:nth-child(2)')       #定位新增栏目的操作栏链接文章位置
        self.assertIn('删除链接',link4.text)      #判定是否变为删除链接
        self.add_img()
        self.save_img('链接文章成功')

# 用例7:回到栏目管理界面,对刚刚链接文章的栏目点击删除链接,查看是否删除链接成功
    @BeautifulReport.add_test_img('取消链接文章') 
    def test_07_cancel_link_articl(self):
        '''回到栏目管理界面,对刚刚链接文章的栏目点击删除链接,查看是否删除链接成功'''
        self.article_management('admin','admin123456')    #进入文章管理界面
        #首先进入栏目管理界面
        self.driver.find_element_by_link_text('栏目管理').click() #进入栏目管理界面
         #显示等待时间到进入栏目管理主页
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_channel_add'))) 
        sleep(1)
        self.driver.find_element_by_css_selector('#table_channel tbody tr:last-child td:last-child a:nth-child(2)').click()      #点击新增栏目的操作栏的删除链接按钮
        sleep(0.5)
        link1=self.driver.find_element_by_id('alter_notify')    #断言判定点击后是否出现提示框修改成功
        self.assertIn('修改成功',link1.text)
        self.add_img()
        self.save_img('取消链接文章')
        sleep(0.5)
        link2=self.driver.find_element_by_css_selector('#table_channel tbody tr:last-child td:nth-child(4)')   #断言判定新增栏目的链接文章栏是否为空
        self.assertIn('',link2.text)
        link3= self.driver.find_element_by_css_selector('#table_channel tbody tr:last-child td:last-child a:nth-child(2)')      #断言判定新增栏目的操作栏是否变为链接文章
        self.assertIn('链接文章',link3.text)
        self.save_img('取消链接文章成功')
        self.add_img()

# 删除文章：
# 用例8:直接删除已被设置为链接的文章,查看是否提示不能直接删除
    @BeautifulReport.add_test_img('删除链接文章') 
    def test_08_delete_link_articl(self):
        '''直接删除已被设置为链接的文章,查看是否提示不能直接删除'''
        self.article_management('admin','admin123456')    #进入文章管理界面
#首先进入栏目管理界面添加链接文章
        self.driver.find_element_by_link_text('栏目管理').click() #进入栏目管理界面
         #显示等待时间到进入栏目管理主页
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_channel_add'))) 
        sleep(1)
        self.driver.find_element_by_css_selector('#table_channel tbody tr:last-child  td:last-child  a:nth-child(2)').click()   #点击测试的栏目链接文章按钮
        sleep(0.5)
         #显示等待时间到进入链接文章弹窗
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'table_channel_article'))) 
        #选择第一个文章设置链接
        self.driver.find_element_by_css_selector('#table_channel_article tbody tr:first-child  td:first-child input').click()   #点击选择文章列表第一列的文章
        self.add_img()
        self.driver.find_element_by_id('btn_channel_link_save').click()      #点击保存按钮
        sleep(0.2)
        #断言判定是否保存成功
        link2=self.driver.find_element_by_id('alter_notify')    #断言判定保存后是否出现提示框保存成功
        self.assertIn('修改成功',link2.text)
        self.add_img()
        sleep(0.5)
        #断言判定栏目列表中链接文章栏是否显示刚刚链接的文章
        link3=self.driver.find_element_by_css_selector('#table_channel tbody tr:last-child td:nth-child(4)')       #定位刚刚新增栏目的链接文章栏
        self.assertIn('测试发布文章1',link3.text)  #判定链接文章栏是否存在刚刚新增的文章名
        #断言判定操作栏是否变为删除链接
        link4=self.driver.find_element_by_css_selector('#table_channel tbody tr:last-child td:last-child a:nth-child(2)')       #定位新增栏目的操作栏链接文章位置
        self.assertIn('删除链接',link4.text)      #判定是否变为删除链接
        self.add_img()
        sleep(1)
#回到文章管理界面删除链接文章
        self.driver.find_element_by_link_text('文章管理').click()   #进入文章管理界面
        self.driver.find_element_by_id('select_article_channel').click() #点击栏目选择框
        sleep(0.5)
        self.driver.find_element_by_css_selector('#select_article_channel option:last-child').click()  #点击刚刚新增的栏目
        sleep(0.5)
        self.driver.find_element_by_css_selector('#list_article li:first-child i').click()   #定位文章列表第一行文章的删除按钮
        sleep(0.5)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        self.driver.implicitly_wait(2)   #隐式等待2秒
        alert.accept()               # 确认删除文章
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('有栏目链接到了文章', link1.text)
        self.add_img()
        self.save_img('删除链接文章') 
        sleep(1)

# 用例9:删除未被设置为链接的文章,查看能否直接删除
    @BeautifulReport.add_test_img('删除文章') 
    def test_09_delete_articl(self):
        '''删除未被设置为链接的文章,查看能否直接删除'''
        self.article_management('admin','admin123456')    #进入文章管理界面
#首先进入栏目管理界面取消链接文章
        self.driver.find_element_by_link_text('栏目管理').click() #进入栏目管理界面
         #显示等待时间到进入栏目管理主页
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_channel_add'))) 
        sleep(1)
        self.driver.find_element_by_css_selector('#table_channel tbody tr:last-child td:last-child a:nth-child(2)').click()      #点击新增栏目的操作栏的删除链接按钮
        sleep(0.2)
        link1=self.driver.find_element_by_id('alter_notify')    #断言判定点击后是否出现提示框修改成功
        self.assertIn('修改成功',link1.text)
        self.add_img()
        sleep(0.5)
        link2=self.driver.find_element_by_css_selector('#table_channel tbody tr:last-child td:nth-child(4)')   #断言判定新增栏目的链接文章栏是否为空
        self.assertIn('',link2.text)
        link3= self.driver.find_element_by_css_selector('#table_channel tbody tr:last-child td:last-child a:nth-child(2)')      #断言判定新增栏目的操作栏是否变为链接文章
        self.assertIn('链接文章',link3.text)
        sleep(1)
#回到文章管理界面删除文章
        self.driver.find_element_by_link_text('文章管理').click()   #进入文章管理界面
        self.driver.find_element_by_id('select_article_channel').click() #点击栏目选择框
        sleep(0.5)
        self.driver.find_element_by_css_selector('#select_article_channel option:last-child').click()  #点击刚刚新增的栏目
        sleep(0.5)
        self.driver.find_element_by_css_selector('#list_article li:first-child i').click()   #定位文章列表第一行文章的删除按钮
        sleep(0.5)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        self.driver.implicitly_wait(2)   #隐式等待2秒
        alert.accept()               # 确认删除文章
        link4=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link4.text)
        self.add_img()
        self.save_img('删除文章成功') 
        sleep(1)
#删除另一个新增的测试文章
        self.driver.find_element_by_css_selector('#select_article_channel option:last-child').click()  #点击刚刚新增的栏目
        sleep(0.5)
        self.driver.find_element_by_css_selector('#list_article li:first-child i').click()   #定位文章列表第一行文章的删除按钮
        sleep(0.5)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        self.driver.implicitly_wait(2)   #隐式等待2秒
        alert.accept()               # 确认删除文章
        link5=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link5.text)
        self.add_img()
        sleep(1)
#删除测试新增的栏目
        self.driver.find_element_by_link_text('栏目管理').click()    #回到栏目管理界面
          #显示等待时间到进入栏目管理主页
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_channel_add'))) 
        sleep(1)
        self.driver.find_element_by_css_selector('#table_channel tbody tr:last-child td:nth-child(5) a:last-child').click()    #点击新增栏目的删除按钮
        sleep(0.5)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        self.driver.implicitly_wait(2)   #隐式等待2秒
        alert.accept()               # 确认删除栏目
        link6=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link6.text)
        self.add_img()
        sleep(1)



if __name__ == "__main__":
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(Articlecase)
    # dir="C:/Users/ZAssitant/Desktop/Geoportal/首页设置/文章管理/434341.html"    #测试报告存储位置
    # filename=open(dir,'wb')
    # runner = HTMLTestRunner(stream=filename, title="文章管理测试报告343434", description="用例执行情况4343")
    # runner.run(suite1)    #  调用HTMLTestRunner类下面的run()方法运行用例套件
    # filename.close()   #  关闭测试报告文件
    unittest.main(argv=['ignored','-v'],exit=False)
    print('')