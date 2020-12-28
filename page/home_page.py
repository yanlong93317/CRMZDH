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
    pudusts_loc = (By.CSS_SELECTOR,
                   'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(4) > a')
    zhaijun_loc = (By.CLASS_NAME,
                   'avatar')
    system_loc = (By.PARTIAL_LINK_TEXT, '系统设置')
    More_loc = (By.XPATH,
                '/html/body/div[1]/div/div/div[2]/ul[1]/li[9]/a')
    knowledge_loc = (By.CSS_SELECTOR, 'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li.dropdown.open > ul > li:nth-child(2) > a')

    def puducts(self):
        '''
        这个是产品的元素定位
        :return:
        '''
        self.find_element(self.pudusts_loc).click()

    def zhaijun(self):
        '''
        这个是个人中心
        :return:
        '''
        self.find_element(self.zhaijun_loc).click()

    def system(self):
        '''
        选择系统设置
        :return:
        '''
        self.find_element(self.system_loc).click()

    def systemset(self):
        '''
        直接进入系统设置
        :return:
        '''
        self.zhaijun()
        self.system()

    def more(self):
        '''
        更多的元素定位
        :return:
        '''
        self.find_element(self.More_loc).click()

    def knowledge(self):
        '''
        更多下面的知识
        :return:
        '''
        self.find_element(self.knowledge_loc).click()

    def knowledgeset(self):
        self.more()
        self.knowledge()
