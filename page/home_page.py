# -*- coding: utf-8 -*-
# @Time : 2020/12/26 22:41
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : home_page.py
# @Project : CrmZDH.test
from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类
from time import sleep  # 引入时间


class HomePage(BasePage):
    pudusts_loc = (By.CSS_SELECTOR,
                   'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(4) > a')
    zhaijun_loc = (By.CLASS_NAME,
                   'avatar')
    system_loc = (By.PARTIAL_LINK_TEXT, '系统设置')
    More_loc = (By.XPATH,
                '/html/body/div[1]/div/div/div[2]/ul[1]/li[9]/a')
    knowledge_loc = (By.CSS_SELECTOR,
                     'body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li.dropdown.open > ul > li:nth-child(2) > a')
    shop_loc = (By.CSS_SELECTOR, "body > div.navbar.navbar-inverse.navbar-fixed-top >"
                                 " div > div > div.nav-collapse.collapse > "
                                 "ul:nth-child(1) > li:nth-child(3)")  # 商机
    admin_loc = (By.CSS_SELECTOR, "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div "
                                  "> div.nav-collapse.collapse > ul.nav.pull-right > "
                                  "li:nth-child(6) > a > img")  # 头像
    pan_loc = (By.CSS_SELECTOR,
               "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse >"
               " ul.nav.pull-right > li.dropdown.open > ul > li:nth-child(2) > a")  # 面板
    auth_loc = (By.CSS_SELECTOR,
                "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > "
                "ul.nav.pull-right > li.dropdown.open"
                " > ul > li:nth-child(5) > a")  # 权限分配
    cont_loc = (By.CSS_SELECTOR, "body > div.navbar.navbar-inverse.navbar-fixed-top >"
                                 " div > div > div.nav-collapse.collapse >"
                                 " ul:nth-child(1) > li:nth-child(7) > a")  # 合同

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

    def shopping(self):
        '''商机跳转'''
        self.find_element(self.shop_loc).click()  # 点击商机
        sleep(3)

    def pan(self):
        '''跳转到我的面板'''
        self.find_element(self.admin_loc).click()
        sleep(2)
        self.find_element(self.pan_loc).click()

    def auth(self):
        '''权限分配'''
        self.find_element(self.admin_loc).click()
        sleep(2)
        self.find_element(self.auth_loc).click()

    def cont(self):
        '''跳转到合同界面'''
        self.find_element(self.cont_loc).click()
