from selenium.webdriver.common.by import By
from page.base_page import BasePage

class AddClue(BasePage):
    addclue_locator=(By.LINK_TEXT,'新建线索')
    see_clue_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td:nth-child(12) > a:nth-child(1)')
    transfer_clue_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(12) > a:nth-child(2)')

    def addclue(self):
        '''
        从home里面点击线索元素后进入线索页面，对新建线索元素定位
        :return:
        '''
        self.find_element(self.addclue_locator).click()

    def seeclue(self):
        '''查看线索'''
        self.find_element(self.see_clue_locator).click()

    def transferclue(self):
        '''转换线索'''
        self.find_element(self.transfer_clue_locator).click()
