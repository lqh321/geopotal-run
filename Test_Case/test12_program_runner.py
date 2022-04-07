'''
栏目管理功能测试,有以下几种情况
添加栏目
用例1:点击首页设置下的栏目管理,查看能否进入栏目管理界面
用例2:点击栏目管理中的添加栏目,查看能否弹出添加栏目弹窗
用例3:在添加栏目弹窗中输入框为空,点击保存,查看是否提示不能为空
用例4:在添加栏目弹窗中输入栏目名称，点击保存,查看是否提示保存成功
用例5:在添加栏目弹窗中输入栏目名称,设置栏目序号,查看是否保存成功
用例6:在添加栏目弹窗中输入栏目名称,设置栏目序号,勾选设为导航,查看是否保存成功
编辑栏目
用例7:在已添加未设为导航的栏目中点击编辑按钮,查看是否弹出编辑栏目弹窗
用例8:在已添加未设为导航的编辑栏目弹窗中修改栏目名称,查看是否编辑成功
用例9:在已添加未设为导航的编辑栏目弹窗中修改栏目序号,查看是否编辑成功
用例10:在已添加未设为导航的编辑栏目弹窗中设为导航,查看是否编辑成功
用例11:在刚刚编辑的栏目操作栏中修改为取消导航,查看是否修改成功
删除栏目
用例12:点击存在文章的栏目对应删除按钮,查看是否提示有文章不能删除
用例13:点击不存在文章的栏目操作栏中的删除按钮,查看能否正常删除
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


class test12_ProgramCase(unittest.TestCase):
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
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('./首页设置/栏目管理/img'), img_name))    #os.path.abspath('')截图存放路径

    
#打开浏览器至数据管理界面
    def program_management(self,username, password):
        self.driver.get('http://www.geoportal.com/login.html')  #进入登录页面
        self.driver.find_element_by_id('input_username').send_keys(username)  #输入用户名
        self.driver.find_element_by_id('input_password').send_keys(password)  #输入密码
        self.driver.find_element_by_id('btn_login').click()  #点击登录
        # #显示等待时间到进入系统主页
        # wait=WebDriverWait(self.driver,400,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'navbarNav'))) 
        sleep(3)
        self.driver.find_element_by_link_text('首页设置').click()   #点击首页设置按钮
        self.driver.implicitly_wait(2)   #隐式等待2秒 
        sleep(1)  
        self.driver.find_element_by_link_text('栏目管理').click()         #点击栏目管理按钮
        #  #显示等待时间到进入栏目管理主页
        # wait=WebDriverWait(self.driver,400,0.5)
        # wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_channel_add'))) 
        sleep(2)



# 添加栏目
# 用例1:点击首页设置下的栏目管理,查看能否进入栏目管理界面
    @BeautifulReport.add_test_img('栏目管理主界面') 
    def test_01_page_channel(self):
        '''点击首页设置下的栏目管理,查看能否进入栏目管理界面'''
        self.program_management('admin','admin123456')    #进入栏目管理界面
        link1=self.driver.find_element_by_id('table_channel')
        self.assertIn('栏目名称',link1.text)
        self.save_img('栏目管理主界面')
        self.add_img()

# 用例2:点击栏目管理中的添加栏目,查看能否弹出添加栏目弹窗
    @BeautifulReport.add_test_img('添加栏目弹窗') 
    def test_02_channel_pop(self):
        '''点击栏目管理中的添加栏目,查看能否弹出添加栏目弹窗'''
        self.program_management('admin','admin123456')    #进入栏目管理界面
        self.driver.find_element_by_id('btn_channel_add').click()   #点击添加栏目按钮
        sleep(1)
        #显示等待时间到进入添加栏目弹窗
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'form_channel'))) 
        #断言是否进入添加栏目弹窗
        link1=self.driver.find_element_by_css_selector('#modal_channel_edit h5')
        self.assertIn('添加栏目',link1.text)
        self.add_img()
        self.save_img('添加栏目弹窗')

# 用例3:在添加栏目弹窗中输入框为空,点击保存,查看是否提示不能为空
    @BeautifulReport.add_test_img('添加栏目为空') 
    def test_03_channel_add_null(self):
        '''在添加栏目弹窗中输入框为空,点击保存,查看是否提示不能为空'''
        self.program_management('admin','admin123456')    #进入栏目管理界面
        self.driver.find_element_by_id('btn_channel_add').click()   #点击添加栏目按钮
        sleep(1)
        #显示等待时间到进入添加栏目弹窗
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'form_channel'))) 
        self.add_img()
        self.driver.find_element_by_id('btn_channel_save').click()   #点击保存按钮
        sleep(0.5)
        #显示等待时间到出现提示框
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言判定是否有提示不能为空
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('请输入栏目名称',link1.text)
        self.add_img()
        self.save_img('栏目名称为空')
 

# 用例4:在添加栏目弹窗中输入栏目名称，点击保存,查看是否提示保存成功
    @BeautifulReport.add_test_img('添加栏目1') 
    def test_04_input_channel_name(self):
        '''在添加栏目弹窗中输入栏目名称，点击保存,查看是否提示保存成功'''
        self.program_management('admin','admin123456')    #进入栏目管理界面
        self.driver.find_element_by_id('btn_channel_add').click()   #点击添加栏目按钮
        sleep(1)
        #显示等待时间到进入添加栏目弹窗
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'form_channel'))) 
        self.driver.find_element_by_id('input_channel_name').send_keys('测试栏目1')   #输入栏目名称
        sleep(0.5)
        self.add_img()
        self.driver.find_element_by_id('btn_channel_save').click()   #点击保存按钮
        sleep(0.5)
        #显示等待时间到出现提示框
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言判定是否有提示添加成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功',link1.text)
        self.add_img()
        self.save_img('添加栏目名称')
        sleep(0.5)
        #断言判定栏目列表中是否存在刚刚新增的栏目名称
        link2=self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(2) td:nth-child(1)')  #定位新增栏目的栏目名称位置
        self.assertIn('测试栏目1',link2.text)
#进入文章管理界面查看栏目选择中是否存在刚刚新增的栏目名称
        self.driver.find_element_by_link_text('文章管理').click()     #点击文章管理按钮
         #显示等待时间到进入文章管理主页
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_article_save'))) 
        sleep(1)
        self.driver.find_element_by_id('select_article_channel').click() #点击栏目选择框
        sleep(0.5)
        #断言判定栏目选择框是否存在刚刚新增的栏目
        link3=self.driver.find_element_by_css_selector('#select_article_channel option:nth-child(2)')
        self.assertIn('测试栏目1',link3.text)
        self.add_img()
        self.save_img('添加栏目名称成功')


# 用例5:在添加栏目弹窗中输入栏目名称,设置栏目序号,查看是否保存成功
    @BeautifulReport.add_test_img('添加栏目2') 
    def test_05_input_channel_index(self):
        '''在添加栏目弹窗中输入栏目名称,设置栏目序号,查看是否保存成功'''
        self.program_management('admin','admin123456')    #进入栏目管理界面
        self.driver.find_element_by_id('btn_channel_add').click()   #点击添加栏目按钮
        sleep(1)
        #显示等待时间到进入添加栏目弹窗
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'form_channel'))) 
        self.driver.find_element_by_id('input_channel_name').send_keys('测试栏目2')   #输入栏目名称
        sleep(0.5)
        el=self.driver.find_element_by_id('input_channel_index')   #定位栏目序号位置
        el.clear() #清空栏目序号输入框
        el.send_keys('2')       #输入栏目序号
        self.add_img()
        self.driver.find_element_by_id('btn_channel_save').click()   #点击保存按钮
        sleep(0.5)
        #显示等待时间到出现提示框
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言判定是否有提示不能为空
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功',link1.text)
        self.add_img()
        self.save_img('设置栏目序号')
        #断言判定栏目列表中是否存在刚刚新增的栏目名称
        link2=self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(4) td:nth-child(1)')  #定位新增栏目的栏目名称位置
        self.assertIn('测试栏目2',link2.text)
        sleep(0.5)
        link2=self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(4) td:nth-child(2)')  #定新增栏目的栏目序号位置
        self.assertIn('2',link2.text)
#进入文章管理界面查看栏目选择中是否存在刚刚新增的栏目名称
        self.driver.find_element_by_link_text('文章管理').click()     #点击文章管理按钮
         #显示等待时间到进入文章管理主页
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_article_save'))) 
        sleep(1)
        self.driver.find_element_by_id('select_article_channel').click() #点击栏目选择框
        sleep(0.5)
        #断言判定栏目选择框是否存在刚刚新增的栏目
        link3=self.driver.find_element_by_css_selector('#select_article_channel option:nth-child(4)')
        self.assertIn('测试栏目2',link3.text)
        self.add_img()
        self.save_img('设置栏目序号成功')

# 用例6:在添加栏目弹窗中输入栏目名称,设置栏目序号,勾选设为导航,查看是否保存成功
    @BeautifulReport.add_test_img('添加栏目3') 
    def test_06_input_channel_isnav(self):
        '''在添加栏目弹窗中输入栏目名称,设置栏目序号,勾选设为导航,查看是否保存成功'''
        self.program_management('admin','admin123456')    #进入栏目管理界面
        self.driver.find_element_by_id('btn_channel_add').click()   #点击添加栏目按钮
        sleep(1)
        #显示等待时间到进入添加栏目弹窗
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'form_channel'))) 
        self.driver.find_element_by_id('input_channel_name').send_keys('测试栏目3')   #输入栏目名称
        sleep(0.5)
        el=self.driver.find_element_by_id('input_channel_index')   #定位栏目序号位置
        el.clear() #清空栏目序号输入框
        el.send_keys('3')       #输入栏目序号
        self.driver.find_element_by_css_selector('#form_channel div:nth-child(3) label').click()     #点击勾选设为导航
        sleep(0.5)
        self.add_img()
        self.driver.find_element_by_id('btn_channel_save').click()   #点击保存按钮
        sleep(0.5)
        #显示等待时间到出现提示框
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'alter_notify'))) 
        #断言判定是否有提示不能为空
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('添加成功',link1.text)
        self.add_img()
        self.save_img('设置导航')
        #断言判定栏目列表中是否存在刚刚新增的栏目名称
        link2=self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(6) td:nth-child(1)')  #定位新增栏目的栏目名称位置
        self.assertIn('测试栏目3',link2.text)
        sleep(0.5)
        link2=self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(6) td:last-child a:nth-child(1)')  #定位新增栏目的操作位置
        self.assertIn('取消导航',link2.text)
#进入文章管理界面查看栏目选择中是否存在刚刚新增的栏目名称
        self.driver.find_element_by_link_text('文章管理').click()     #点击文章管理按钮
         #显示等待时间到进入文章管理主页
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'btn_article_save'))) 
        sleep(1)
        self.driver.find_element_by_id('select_article_channel').click() #点击栏目选择框
        sleep(0.5)
        #断言判定栏目选择框是否存在刚刚新增的栏目
        link3=self.driver.find_element_by_css_selector('#select_article_channel option:nth-child(6)')
        self.assertIn('测试栏目3',link3.text)
        self.add_img()
        self.save_img('设置导航成功')

# 编辑栏目
# 用例7:在已添加未设为导航的栏目中点击编辑按钮,查看是否弹出编辑栏目弹窗
    @BeautifulReport.add_test_img('编辑栏目弹窗') 
    def test_07_channel_edit_pop(self):
        '''在已添加未设为导航的栏目中点击编辑按钮,查看是否弹出编辑栏目弹窗'''
        self.program_management('admin','admin123456')    #进入栏目管理界面
        #使用刚刚新增的测试栏目3为测试对象
        self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(6) td:last-child a:nth-child(3)').click()     #点击测试对象的编辑按钮
        sleep(1)
        #显示等待时间到进入编辑栏目弹窗
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'form_channel'))) 
        #断言判定是否弹出编辑栏目弹窗
        link1=self.driver.find_element_by_css_selector('#modal_channel_edit h5')
        self.assertIn('添加栏目',link1.text)
        self.add_img()
        self.save_img('编辑栏目弹窗')

# 用例8:在已添加未设为导航的编辑栏目弹窗中修改栏目名称,查看是否编辑成功
    @BeautifulReport.add_test_img('修改栏目名称') 
    def test_08_channel_edit_name(self):
        '''在已添加未设为导航的编辑栏目弹窗中修改栏目名称,查看是否编辑成功'''
        self.program_management('admin','admin123456')    #进入栏目管理界面
        #使用刚刚新增的测试栏目3为测试对象
        self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(6) td:last-child a:nth-child(3)').click()     #点击测试对象的编辑按钮
        sleep(1)
        #显示等待时间到进入编辑栏目弹窗
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'form_channel'))) 
        e1=self.driver.find_element_by_id('input_channel_name')   #定位栏目名称位置
        e1.clear()  #清空栏目名称输入框
        sleep(0.2)
        self.add_img()
        self.driver.find_element_by_id('btn_channel_save').click()     #点击保存按钮
        sleep(0.2)
        #断言查看是否提示不能为空
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('请输入栏目名称',link1.text)
        self.add_img()
        sleep(0.2)
        e1.send_keys('修改测试栏目名称')    #输入栏目名称
        self.add_img()
        self.driver.find_element_by_id('btn_channel_save').click()     #点击保存按钮
        sleep(0.2)
        #断言判定是否提示修改成功
        link2=self.driver.find_element_by_id('alter_notify')
        self.assertIn('修改成功',link2.text)
        self.add_img()
        self.save_img('修改栏目名称成功')
        sleep(0.5)
        #断言查看栏目列表中栏目名称是否改变
        link3=self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(6) td:nth-child(1)') 
        self.assertIn('修改测试栏目名称',link3.text)


# 用例9:在已添加未设为导航的编辑栏目弹窗中修改栏目序号,查看是否编辑成功
    @BeautifulReport.add_test_img('编辑栏目弹窗') 
    def test_09_channel_edit_index(self):
        '''在已添加未设为导航的编辑栏目弹窗中修改栏目序号,查看是否编辑成功'''
        self.program_management('admin','admin123456')    #进入栏目管理界面
        #使用刚刚新增的测试栏目3为测试对象
        self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(6) td:last-child a:nth-child(3)').click()     #点击测试对象的编辑按钮
        sleep(1)
        #显示等待时间到进入编辑栏目弹窗
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'form_channel'))) 
        e2=self.driver.find_element_by_id('input_channel_index') #定位栏目序号输入框
        e2.clear() #清空栏目序号
        # self.driver.find_element_by_id('btn_channel_save').click()     #点击保存按钮
        # sleep(0.5)
        # #断言查看是否提示不能为空
        # link2=self.driver.find_element_by_id('alter_notify')
        # self.assertIn('请输入栏目序号',link2.text)
        e2.send_keys('1')  #输入栏目序号
        self.add_img()
        self.driver.find_element_by_id('btn_channel_save').click()     #点击保存按钮
        sleep(0.5)
        #断言判定是否提示修改成功
        link3=self.driver.find_element_by_id('alter_notify')
        self.assertIn('修改成功',link3.text)
        self.add_img()
        self.save_img('修改栏目序号成功')
        sleep(0.5)
        #断言查看栏目列表中栏目序号是否改变
        link3=self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(3) td:nth-child(2)')  #定位修改的栏目序号
        self.assertIn('1',link3.text)

# 用例10:在已添加未设为导航的编辑栏目弹窗中设为导航,查看是否编辑成功
    @BeautifulReport.add_test_img('修改栏目设为导航') 
    def test_10_channel_set_isnav(self):
        '''在已添加未设为导航的编辑栏目弹窗中设为导航,查看是否编辑成功'''
        self.program_management('admin','admin123456')    #进入栏目管理界面
        #选定测试栏目1为测试对象
        self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(2) td:last-child a:nth-child(3)').click()   #定位测试栏目1的编辑按钮
        sleep(1)
        #显示等待时间到进入编辑栏目弹窗
        wait=WebDriverWait(self.driver,400,0.5)
        wait.until(EC.visibility_of_any_elements_located((By.ID,'form_channel'))) 
        self.driver.find_element_by_css_selector('#form_channel div:nth-child(3) label').click()     #点击勾选设为导航
        self.add_img()
        self.driver.find_element_by_id('btn_channel_save').click()     #点击保存按钮
        sleep(0.5)
         #断言判定是否提示修改成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('修改成功',link1.text)
        self.add_img()
        self.save_img('修改设为导航成功')
        sleep(0.5)
        #断言判定栏目列表中的操作栏是否变化
        link2=self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(2) td:last-child a:nth-child(1)')
        self.assertIn('取消导航',link2.text)

# 用例11:在刚刚编辑的栏目操作栏中修改为取消导航,查看是否修改成功
    @BeautifulReport.add_test_img('修改栏目取消导航') 
    def test_11_channel_cancel_isnav(self):
        '''在刚刚编辑的栏目操作栏中修改为取消导航,查看是否修改成功'''
        self.program_management('admin','admin123456')    #进入栏目管理界面
        #选定测试栏目1为测试对象
        self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(2) td:last-child a:nth-child(1)').click()   #定位测试栏目1的取消导航按钮
        sleep(0.5)
        #断言判定是否提示修改成功
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('修改成功',link1.text)
        self.add_img()
        self.save_img('修改取消导航成功')
        sleep(0.5)
        #断言判定栏目列表中的操作栏是否变化
        link2=self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(2) td:last-child a:nth-child(1)')
        self.assertIn('设为导航',link2.text)

# 删除栏目
# 用例12:点击存在文章的栏目对应删除按钮,查看是否提示有文章不能删除
    @BeautifulReport.add_test_img('删除文章栏目') 
    def test_12_delete_article_channel(self):
        '''点击存在文章的栏目对应删除按钮,查看是否提示有文章不能删除'''
        self.program_management('admin','admin123456')    #进入栏目管理界面
        self.driver.find_element_by_css_selector('#table_channel tbody tr:first-child td:last-child a:last-child').click()   #定位栏目列表第一列的删除按钮 
        sleep(0.5)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        self.driver.implicitly_wait(2)   #隐式等待2秒
        alert.accept()               # 确认删除图层
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('栏目下存在文章，无法删除', link1.text)
        self.add_img()
        self.save_img('文章栏目不能直接删除') 

# 用例13:点击不存在文章的栏目操作栏中的删除按钮,查看能否正常删除
    @BeautifulReport.add_test_img('删除栏目') 
    def test_13_delete_channel(self):
        '''点击不存在文章的栏目操作栏中的删除按钮,查看能否正常删除'''
        self.program_management('admin','admin123456')    #进入栏目管理界面
#删除测试栏目1
        self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(2) td:last-child a:last-child').click()   #定位测试栏目1的位置
        sleep(0.5)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        self.driver.implicitly_wait(2)   #隐式等待2秒
        alert.accept()               # 确认删除栏目
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link1.text)
        self.add_img()
        self.save_img('栏目删除成功') 
        sleep(1)
#删除修改测试栏目
        self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(2) td:last-child a:last-child').click()   #定位测试修改测试栏目的位置
        sleep(0.5)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        self.driver.implicitly_wait(2)   #隐式等待2秒
        alert.accept()               # 确认删除栏目
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link1.text)
        self.add_img()
        sleep(1)
#删除测试栏目2
        self.driver.find_element_by_css_selector('#table_channel tbody tr:nth-child(3) td:last-child a:last-child').click()   #定位测试栏目2的位置
        sleep(0.5)
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert  # 获取弹出窗口
        self.driver.implicitly_wait(2)   #隐式等待2秒
        alert.accept()               # 确认删除栏目
        link1=self.driver.find_element_by_id('alter_notify')
        self.assertIn('删除成功', link1.text)
        self.add_img()


if __name__ == '__main__':
    unittest.main(argv=['ignored','-v'],exit=False)
    print('')
