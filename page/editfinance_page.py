from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类
from time import sleep


class EditFinance(BasePage):
    editfinancename_loc = (By.XPATH,'/html/body/div[5]/div[2]/div/form/table/tbody/tr[2]/td[2]/input')
    editfinancenamebaocun_loc = (By.CSS_SELECTOR,
                                 'body > div.container > div.row > div > form > table > tfoot > tr > td:nth-child(2) > input.btn.btn-primary')

    def editfinancename(self, namer):
        '''
        编辑应收款的名字
        :param namer:
        :return:
        '''
        ele = self.find_element(self.editfinancename_loc)
        ele.clear()
        sleep(3)
        ele.send_keys(namer)

    def editfinancenamebaocun(self):
        '''
        编辑后保存按钮
        :return:
        '''
        self.find_element(self.editfinancenamebaocun_loc).click()
    def editfinanceset(self,namer):
        '''
        编辑集合
        :return:
        '''
        self.editfinancename(namer)
        self.editfinancenamebaocun()
