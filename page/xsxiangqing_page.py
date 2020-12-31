from selenium.webdriver.common.by import By
from page.base_page import BasePage


class ClueXiangQing(BasePage):
    alter_locator = (By.LINK_TEXT, '修改')

    getgs_xiangqing_locator = (
    By.CSS_SELECTOR, '#tab1 > div.back_box > table > tbody > tr:nth-child(3) > td:nth-child(2) > span')

    def alterclue(self):
        '''对进入线索详情页面中的修改元素定位'''
        self.find_element(self.alter_locator).click()

    def getgs_xiangqing(self):
        '''断言，查看成功，详情里有点击线索里面的相对应的公司名'''
        self.find_element(self.getgs_xiangqing_locator)
        return self.find_element(self.getgs_xiangqing_locator)
