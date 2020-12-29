# -*- coding: utf-8 -*-
# @Time : 2020/12/30 0:04
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : editsuccess_page.py
# @Project : CRMZDH
from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类


class EditSuccess(BasePage):
    editsyccessname_loc = (By.CSS_SELECTOR,
                           'body > div.container > div.row > div:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(2)')

    def editsyccessname(self):
        '''
        编辑成功页面的应收款名字
        :return:
        '''
        self.find_element(self.editsyccessname_loc)
        return self.find_element(self.editsyccessname_loc)
