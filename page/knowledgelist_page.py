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
    searchknowledge_loc = (By.CSS_SELECTOR, '#search')
    searchsubmit_loc = (By.ID, 'dosearch')
    addknowledgename_loc = (By.LINK_TEXT, '云深不知处 《虞美人》')
    viewknowledge_loc = (By.LINK_TEXT, '查看')
    editknowledge_loc = (By.LINK_TEXT, '编辑')
    editknowledgename_loc = (By.LINK_TEXT, '云深不知处')
    checkbox_loc = (By.CSS_SELECTOR, '#form1 > table > tbody > tr > td:nth-child(1) > input')
    deleteknowledge_loc = (By.CSS_SELECTOR, '#delete')
    deletexiangqing_loc=(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td')

    def addknowledge(self):
        '''
        添加知识
        :return:
        '''
        self.find_element(self.addknowledge_loc).click()

    def searchknowledge(self, knowledge):
        '''
        知识搜索
        :return:
        '''
        self.find_element(self.searchknowledge_loc).send_keys(knowledge)

    def searchsubmit(self):
        '''
        搜索确定按钮
        :return:
        '''
        self.find_element(self.searchsubmit_loc).click()

    def searchknowledgeset(self, knowledge):
        '''
        搜索操作的集合
        :return:
        '''
        self.searchknowledge(knowledge)
        self.searchsubmit()

    def addknowledgename(self):
        '''
        找到我添加知识的文本信息
        :return:
        '''
        self.find_element(self.addknowledgename_loc)
        return self.find_element(self.addknowledgename_loc)

    def viewknowledge(self):
        '''
        查看知识
        :return:
        '''
        self.find_element(self.viewknowledge_loc).click()

    def editknowledge(self):
        '''
        编辑添加的知识
        :return:
        '''
        self.find_element(self.editknowledge_loc).click()

    def editknowledgename(self):
        '''
        编辑修改
        :return:
        '''
        self.find_element(self.editknowledgename_loc)
        return self.find_element(self.editknowledgename_loc)

    def checkbox(self):
        '''
        选择要删除的知识按钮
        :return:
        '''
        self.find_element(self.checkbox_loc).click()

    def deleteknowledge(self):
        '''
        删除选择的知识
        :return:
        '''
        self.find_element(self.deleteknowledge_loc).click()

    def deletesets(self):
        '''
        删除集合
        :return:
        '''
        self.checkbox()
        self.deleteknowledge()
        self.driver.switch_to.alert.accept()

    def deletexiangqing(self):
        self.find_element(self.deletexiangqing_loc)
        return self.find_element(self.deletexiangqing_loc)

