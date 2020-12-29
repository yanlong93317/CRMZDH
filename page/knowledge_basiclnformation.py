# -*- coding: utf-8 -*-
# @Time : 2020/12/29 11:37
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : knowledge_basiclnformation.py
# @Project : CRMZDH
from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类


class BasicInformationKL(BasePage):
    jbknowledgename_loc = (By.CSS_SELECTOR, 'body > div.container > div.page-header > h4')

    def jbknowledgename(self):
        self.find_element(self.jbknowledgename_loc)
        return self.find_element(self.jbknowledgename_loc)
