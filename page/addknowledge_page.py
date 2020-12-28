# -*- coding: utf-8 -*-
# @Time : 2020/12/29 0:34
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : addknowledge_page.py
# @Project : CRMZDH
from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类
from time import sleep  # 引入时间


class AddknowLedge(BasePage):
    title_loc=(By.CSS_SELECTOR,'#title')

    def title(self,title):
        self.find_element(self.title_loc).send_keys(title)