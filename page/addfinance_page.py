# -*- coding: utf-8 -*-
# @Time : 2020/12/29 21:32
# @Author : zj12345
# @Email : 374680231@qq.com
# @File : addfinance_page.py
# @Project : CRMZDH
from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类
from time import sleep


class AddFinance(BasePage):
    financename_loc = (By.CSS_SELECTOR, '#name')
    client_loc = (By.ID, 'customer')
    clintsubmit_loc = (By.CSS_SELECTOR, '#datas > tr > td:nth-child(1) > input[type=radio]:nth-child(1)')
    clientoksubmit_loc = (By.CSS_SELECTOR,
                          'body > div:nth-child(8) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span')
    principal_loc = (
        By.ID, 'owner_name')
    searchprincipal_loc = (By.CSS_SELECTOR, '#d_name')
    searchsubmits_loc = (By.CSS_SELECTOR, '#dialog-message3 > div > ul > button')
    chooseprincipal_loc = (By.CSS_SELECTOR, '#d_content > tr > td:nth-child(1) > input[type=radio]')
    principalok_loc = (By.XPATH,
                       '/html/body/div[9]/div[3]/div/button[1]/span')
    money_loc = (By.CSS_SELECTOR, '#price')
    querensubmit_loc = (By.CSS_SELECTOR,
                        'body > div.container > div.row > div > form > table > tfoot > tr > td:nth-child(2) > input:nth-child(1)')

    def financename(self, name):
        '''
        应收款名字
        :return:
        '''
        self.find_element(self.financename_loc).send_keys(name)

    def client(self):
        '''
        选择客户
        :return:
        '''
        self.find_element(self.client_loc).click()

    def clintsubmit(self):
        '''
        选择客户的左边的小按钮
        :return:
        '''
        self.find_element(self.clintsubmit_loc).click()

    def clientoksubmit(self):
        '''
        选择客户的确定按钮
        :return:
        '''
        self.find_element(self.clientoksubmit_loc).click()

    def principal(self):
        '''
        点击负责人
        :return:
        '''
        self.find_element(self.principal_loc).click()

    def searchprincipal(self, principal):
        '''
        在搜索框输入负责人的名字
        :return:
        '''
        self.find_element(self.searchprincipal_loc).send_keys(principal)

    def searchsubmits(self):
        '''
        点击搜索按钮
        :return:
        '''
        self.find_element(self.searchsubmits_loc).click()

    def chooseprincipal(self):
        '''
        选择负责人的小按钮
        :return:
        '''
        self.find_element(self.chooseprincipal_loc).click()

    def principalok(self):
        '''
        点击OK按钮
        :return:
        '''
        self.find_element(self.principalok_loc).click()

    def money(self, money):
        '''
        收款金额输入框
        :return:
        '''
        self.find_element(self.money_loc).send_keys(money)

    def querensubmit(self):
        '''
        保存按钮
        :return:
        '''
        self.find_element(self.querensubmit_loc).click()

    def financenameset(self, financename, financenames, money):
        self.financename(financename)
        self.client()
        self.clintsubmit()
        self.clientoksubmit()
        self.principal()
        sleep(5)
        self.searchprincipal(financenames)
        sleep(5)
        self.searchsubmits()
        self.chooseprincipal()
        self.principalok()
        self.money(money)
        self.querensubmit()
