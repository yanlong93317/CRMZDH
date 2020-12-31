from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类


class FinanceList(BasePage):
    addfinance_loc = (
        By.CSS_SELECTOR, 'body > div.container > div.row > div:nth-child(1) > div.pull-right > a:nth-child(1)')
    searchfinance_loc = (By.CSS_SELECTOR, '#search')
    searchsubmit_loc = (By.CSS_SELECTOR, '#searchForm > ul > li:nth-child(4) > button')
    choosefinancesubmit_loc=(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td:nth-child(1) > input')
    deletesubmits_loc = (By.CSS_SELECTOR, '#delete')
    addfinancename_loc=(By.LINK_TEXT,'天子笑')
    serchfinancename_loc=(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td:nth-child(2) > a')
    viewfinancename_loc=(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td:nth-child(11) > a:nth-child(1)')
    ceditfinancename_loc=(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td:nth-child(11) > a:nth-child(2)')
    deletresults_loc=(By.CSS_SELECTOR,'#form1 > table > tbody > tr > td')
    def addfinance(self):
        '''
        新建应收款按钮
        :return:
        '''
        self.find_element(self.addfinance_loc).click()

    def searchfinance(self, name):
        '''
        搜索输入框
        :return:
        '''
        self.find_element(self.searchfinance_loc).send_keys(name)

    def searchsubmits(self):
        '''
        搜索确定按钮
        :return:
        '''
        self.find_element(self.searchsubmit_loc).click()

    def searchsets(self,name):
        '''
        搜索的集合操作
        :return:
        '''
        self.searchfinance(name)
        self.searchsubmits()

    def choosefinancesubmit(self):
        '''
        搜索到以后选择按钮
        :return:
        '''
        self.find_element(self.choosefinancesubmit_loc).click()

    def deletesubmits(self):
        '''
        删除按钮
        :return:
        '''
        self.find_element(self.deletesubmits_loc).click()
        self.driver.switch_to.alert.accept()

    def deletesubmitset(self):
        '''
        删除集合
        :return:
        '''
        self.choosefinancesubmit()
        self.deletesubmits()



    def addfinanceanme(self):
        '''
        添加应收款的名字
        :return:
        '''
        self.find_element(self.addfinancename_loc)
        return self.find_element(self.addfinancename_loc)

    def serchfinancename(self):
        '''
        定位搜索到的应收款名字
        :return:
        '''
        self.find_element(self.serchfinancename_loc)
        return self.find_element(self.serchfinancename_loc)

    def viewfinancename(self):
        '''
        查看应收款名字
        :return:
        '''
        self.find_element(self.viewfinancename_loc).click()

    def editfinancename(self):
        '''
        编辑应收款
        :return:
        '''
        self.find_element(self.ceditfinancename_loc).click()

    def deletresults(self):
        '''
        删除应收款搜索到的结果要返回一个文本
        :return:
        '''
        self.find_element(self.deletresults_loc)
        return self.find_element(self.deletresults_loc)



