# -*- coding: utf-8 -*-
# @Time : 2020/12/29 0:23
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : knowledgelist_page.py
# @Project : CRMZDH
from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类
from time import sleep  # 引入时间


class KnowLedgeList(BasePage):
    addknowledge_loc = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(2) > div > div.pull-right > a')

    def addknowledge(self):
        '''
        添加知识
        :return:
        '''
        self.find_element(self.addknowledge_loc).click()
