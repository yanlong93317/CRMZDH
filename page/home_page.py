# -*- coding: utf-8 -*-
# @Time : 2020/12/26 22:41
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : home_page.py
# @Project : CrmZDH.test
from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类
from time import sleep  # 引入时间


class Home(BasePage):
    knowledge_loc = (By.CSS_SELECTOR,
                     'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(4) > a')
    zhaijun_loc = (By.CLASS_NAME,
                   'avatar')
    system_loc=(By.PARTIAL_LINK_TEXT,'系统设置')
    def knowlege(self):
        '''
        这个是知识的
        :return:
        '''
        self.find_element(self.knowledge_loc).click()
    def zhaijun(self):
        '''
        这个是个人中心
        :return:
        '''
        self.find_element(self.zhaijun_loc).click()

    def system(self):
        self.find_element(self.system_loc).click()