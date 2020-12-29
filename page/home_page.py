from selenium.webdriver.common.by import By
from page.base_page import BasePage

class HomePage(BasePage):
    source_locator = (By.LINK_TEXT, '线索')
    cusumer_locator = (By.LINK_TEXT, '客户')
    task_locator = (By.LINK_TEXT, '任务')
    more_locator = (By.LINK_TEXT, '更多')
    mail_locator = (By.LINK_TEXT, '站内信')
    name_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a')
    notice_locator = (By.LINK_TEXT, '公告管理')

    def source(self):
        '''
        从home里面点击线索元素定位
        :return:
        '''
        self.find_element(self.source_locator).click()

    def cusumer(self):
        '''对导航列表中的客户元素定位'''
        self.find_element(self.cusumer_locator).click()

    def task(self):
        '''对导航列表中的任务元素定位'''
        self.find_element(self.task_locator).click()

    def more(self):
        '''对导航列表中的更多元素定位'''
        self.find_element(self.more_locator).click()

    def mail(self):
        '''对更多下拉菜单中的站内信元素定位'''
        self.find_element(self.mail_locator).click()

    def tangliname(self):
        '''对右上角的用户tangli元素定位'''
        self.find_element(self.name_locator).click()

    def notice(self):
        '''对用户tangli下拉菜单中的公告管理元素定位'''
        self.find_element(self.notice_locator).click()





