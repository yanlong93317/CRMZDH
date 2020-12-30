# -*- coding: utf-8 -*-
# @Time : 2020/12/28 17:05
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : productlist_page.py
# @Project : CRMZDH
from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类
from time import sleep  # 引入时间


class ProductList(BasePage):
    addproduct_loc = (By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(2) > div.pull-right > a')
    product_loc = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(3) > a > span')
    search_loc = (By.CSS_SELECTOR, '#search')
    searchsubmit_loc = (By.ID, 'dosearch')
    productnames_loc = (By.CSS_SELECTOR, '#form1 > table > tbody > tr > td:nth-child(3) > a > span')
    view_loc = (By.LINK_TEXT, '查看')
    edit_loc = (By.LINK_TEXT, '编辑')
    table_loc = (By.CSS_SELECTOR, '#form1 > table > tbody')
    tr_loc = (By.TAG_NAME, 'tr')
    td_loc = (By.TAG_NAME, 'td')
    xuanze_loc = (By.CSS_SELECTOR, '#form1 > table > tbody > tr > td:nth-child(1) > input')
    delete_loc = (
        By.CSS_SELECTOR, '#delete')
    a_loc = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(2) > td:nth-child(1) > input')
    deletresult_loc = (By.CSS_SELECTOR, '#form1 > table > tbody > tr > td')

    def addproduct(self):
        '''
        这个是商品列表添加产品的按钮
        :return:
        '''
        self.find_element(self.addproduct_loc).click()

    def prductname(self):
        '''
        这个是商品列表里面商品的商品名称的元素定位
        :return:
        '''
        elemet = self.find_element(self.product_loc)
        return elemet

    def search(self, name):
        '''
        这个是商品列表里面的搜索框输入框的元素定位
        :param name:
        :return:
        '''
        self.find_element(self.search_loc).send_keys(name)

    def searchsubmit(self):
        '''
        输入搜索内容后的搜索按钮
        :return:
        '''
        self.find_element(self.searchsubmit_loc).click()

    def searchset(self, name):
        self.search(name)
        self.searchsubmit()

    def productnames(self):
        '''
        这个是我通过搜索搜索出来的商品的商品名称
        :return:
        '''
        self.find_element(self.productnames_loc)
        return self.find_element(self.productnames_loc)

    def view(self):
        '''
        这是查看了商品名称的元素定位
        :return:
        '''
        self.find_element(self.view_loc).click()

    def edit(self):
        '''
        这是编辑商品名称的元素定位
        :return:
        '''
        self.find_element(self.edit_loc).click()

    def zhanghaun(self, name):
        table_element = self.find_element(self.table_loc)
        sleep(2)
        tr_lists = table_element.find_elements(*self.tr_loc)
        sleep(2)
        tr_lists = tr_lists[2:]
        for tr in tr_lists:
            td_list = tr.find_elements(*self.td_loc)
            sleep(3)
            if td_list[2].text == name:
                return td_list[2]

    def xuanzesubmit(self):
        self.find_element(self.xuanze_loc).click()

    def deletesubmit(self):
        self.find_element(self.delete_loc).click()
        self.driver.switch_to.alert.accept()

    def deletresult(self):
        self.find_element(self.deletresult_loc)
        return self.find_element(self.deletresult_loc)
