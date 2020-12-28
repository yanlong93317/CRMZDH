# -*- coding: utf-8 -*-
# @Time : 2020/12/26 22:32
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : browser.py
# @Project : CrmZDH.test
from selenium import webdriver


class BroswerModel():
    def broswer_chrome(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        return driver
