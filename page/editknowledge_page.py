from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类
from time import sleep  # 引入时间


class EditKnowledge(BasePage):
    edittitle_loc = (By.CSS_SELECTOR,
                     'body > div.container > div.row > div > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=text]')
    editsubmit_loc = (
    By.CSS_SELECTOR, 'body > div.container > div.row > div > form > table > tfoot > tr > td > input.btn.btn-primary')

    def edittitle(self, title):
        '''
        修改标题的内容
        :return:
        '''
        ele = self.find_element(self.edittitle_loc)
        ele.clear()
        sleep(4)
        ele.send_keys(title)

    def editsubmit(self):
        '''
        修改后的保存按钮
        :return:
        '''
        self.find_element(self.editsubmit_loc).click()

    def edittitleset(self, title):
        self.edittitle(title)
        self.editsubmit()
