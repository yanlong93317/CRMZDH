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
    iframe_loc=(By.TAG_NAME,'iframe')
    iframebody_loc=(By.CSS_SELECTOR,'body')
    savesubmit_loc=(By.CSS_SELECTOR,'body > div.container > div.row > div > form > table > tfoot > tr > td > input:nth-child(1)')

    def title(self,title):
        '''
        添加知识里面是标题
        :param title:
        :return:
        '''
        self.find_element(self.title_loc).send_keys(title)


    def iframe(self,neirong):
        '''
        先切换到iframe这个框架
        在找到这个输入框，输入东西
        在切换回去。
        :param neirong:
        :return:
        '''
        self.driver.switch_to.frame(self.driver.find_elements(*self.iframe_loc)[0])
        self.find_element(self.iframebody_loc).send_keys(neirong)
        self.driver.switch_to.parent_frame()

    def savesubmit(self):
        '''
        确认保存按钮
        :return:
        '''
        self.driver.switch_to.parent_frame()
        self.find_element(self.savesubmit_loc).click()




