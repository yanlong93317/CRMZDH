# -*- coding: utf-8 -*-
# @Time : 2020/12/28 17:05
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : productlist_page.py
# @Project : CRMZDH
from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类


class ProductList(BasePage):
    addproduct_loc = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(2) > div.pull-right > a')
    product_loc = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(3) > a > span')

    def addproduct(self):
        self.find_element(self.addproduct_loc).click()

    def prductname(self):
        elemet = self.find_element(self.product_loc)
        return elemet
