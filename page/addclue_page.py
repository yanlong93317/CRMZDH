from selenium.webdriver.common.by import By
from page.base_page import BasePage
from time import sleep

class AddClue(BasePage):
    addclue_locator=(By.LINK_TEXT,'新建线索')
    see_clue_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td:nth-child(12) > a:nth-child(1)')
    transfer_clue_locator = (By.CSS_SELECTOR, '#form1 > table > tbody > tr:nth-child(1) > td:nth-child(12) > a:nth-child(2)')
    transfer_save_locator = (By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td > input:nth-child(1)')
    deleteall_locator = (By.ID, 'check_all')
    piliang_caozuo_locator = (By.LINK_TEXT, '批量操作')
    piliang_delete_locator = (By.LINK_TEXT, '批量删除')

    gitcluename_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > a > span')
    noclue_locator=(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td')
    gittransfer_locator=(By.CSS_SELECTOR,'body > div.container > div.alert.alert-success')



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
        sleep(2)


    def deletall(self):
        '''勾选权限按钮框的元素定位'''
        self.find_element(self.deleteall_locator).click()

    def plczclue(self):
        '''对批量操作进行的元素定位'''
        self.find_element(self.piliang_caozuo_locator).click()

    def pldeleteclue(self):
        '''对批量操作下的批量删除元素定位'''
        self.find_element(self.piliang_delete_locator).click()
        self.driver.switch_to.alert.accept()


    def gitcluename(self):
        '''断言，获取新添加的线索名'''
        self.find_element(self.gitcluename_locator)
        return self.find_element(self.gitcluename_locator)

    def noclue(self):
        '''断言批量删除全部线索后，为暂无数据元素定位'''
        self.find_element(self.noclue_locator)
        return self.find_element(self.noclue_locator)

    def gittransfer(self):
        '''转换成功以后，文本添加客户成功断言'''
        self.find_element(self.gittransfer_locator)
        return self.find_element(self.gittransfer_locator)









