# -*- coding: utf-8 -*-
# @Time : 2020/12/28 20:35
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : puduct_edit_page.py
# @Project : CRMZDH
from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类
from time import sleep


class PuductEdit(BasePage):
    editshopname_loc = (By.CSS_SELECTOR, '#name')
    baocunsubmit_loc = (By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td > input.btn.btn-primary')

    def editshopname(self, shopname):
        '''
        这个是编辑页面的商品名称的元素定位
        :param shopname:
        :return:
        '''
        ele=self.find_element(self.editshopname_loc)
        ele.clear()
        self.driver.switch_to.alert.accept()
        sleep(4)
        ele.send_keys(shopname)



    def baocunsubmit(self):
        '''
        这个是编辑页面的保存按钮的元素定位
        :return:
        '''
        self.find_element(self.baocunsubmit_loc).click()

    def editset(self,shopname):
        self.editshopname(shopname)
        self.baocunsubmit()
