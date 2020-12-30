from time import sleep
from selenium.webdriver.common.by import By
from page.home_page import HomePage
class MyCont(HomePage):
    # addcont_loc=(By.CSS_SELECTOR, "body > div.container > "
    #                               "div.row > div:nth-child(1) > div > a")   #添加合同
    # # 点击商机选择框
    # businesscont_loc=(By.NAME, "business_name")#商机选择框
    # selectbusin_loc=(By.NAME, "business")  # 选择商机
    # sleep(2)
    # djsure_loc=(By.CSS_SELECTOR, "body > div:nth-child(12) >"
    #                                      " div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix"
    #                                      " > div > button:nth-child(1)")  # 点击确定
    # contprice_loc=(By.NAME,"price")  #合同金额
    # djmake_loc=(By.NAME, "submit") # 确定
    # contedit_loc=(By.CSS_SELECTOR,"#form1 > table > tbody > tr:nth-child(1) > "
    #                             "td:nth-child(10) > a:nth-child(2)")# 编辑按钮
    # getback_loc=(By.CSS_SELECTOR,"#tab1 > div.container2.top-pad > div > a:nth-child(3)")
    # keyword_loc=(By.ID, "search") #关键字
    # djsearch_loc=(By.CSS_SELECTOR, "#searchForm > ul > li:nth-child(4) > button") #搜索按钮
    # nextpage_loc=(By.CSS_SELECTOR, "#form1 > table > tfoot > tr > td > div.pagination "
    #                         "> div.span4 > div > ul > li:nth-child(4) > span") #点击下一页
    selectcont_loc=(By.NAME, "contract_id[]").click()
    djdel_loc=(By.ID, "delete").click()
    # def djaddcont(self):
    #     self.find_element(self.addcont_loc).click()
    #     sleep(2)
    # def djbucont(self):
    #     self.find_element(self.businesscont_loc).click()
    #     sleep(2)
    # def selectcont(self):
    #     self.find_element(self.selectbusin_loc).click()
    #     sleep(2)
    # def djsure(self):
    #     self.find_element(self.djsure_loc).click()
    #     sleep(2)
    # def contprice(self,conprice):
    #     self.find_element(self.contprice_loc).clear()
    #     sleep(2)
    #     self.find_element(self.contprice_loc).send_keys(conprice)
    #     sleep(3)
    # def djmake(self):
    #     self.find_element(self.djmake_loc).click()
    #     sleep(2)
    # def addcont(self,contprice):
    #     '''增加合同'''
    #     self.djaddcont()
    #     self.djbucont()
    #     self.selectcont()
    #     self.djsure()
    #     self.contprice(contprice)
    #     self.djmake()
    # def djedit(self):
    #     self.find_element(self.contedit_loc).click()
    #     sleep(2)
    # def getback(self):
    #     self.find_element(self.getback_loc).click()
    #     sleep(2)
    # def editcont(self,editprice):
    #     '''修改合同'''
    #     self.djedit()
    #     self.contprice(editprice)
    #     self.djmake()
    #     self.getback()
    # def keywprd_input(self,keyword):
    #     self.find_element(self.keyword_loc).clear()
    #     sleep(1)
    #     self.find_element(self.keyword_loc).send_keys(keyword)
    #     sleep(2)
    # def djserach(self):
    #     self.find_element(self.djsearch_loc).click()
    #     sleep(2)
    # def search(self,kyword):
    #     '''搜索'''
    #     self.keywprd_input(kyword)
    #     self.djserach()
    # def nextpage(self):
    #     self.find_element(self.nextpage_loc).click()
    #     sleep(2)
    # def checknext(self):
    #     '''下一页'''
    #     self.nextpage()
    def selectcont(self):
        self.find_element(self.selectcont_loc).click()
        sleep(2)
    def djdel(self):
        self.find_element(self.djdel_loc).click()
    def djassert(self):
        self.driverswitch_to.alert.text
        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(3)
    def delcont(self):
        '''删除合同'''
        self.selectcont()
        self.djdel()
        self.djassert()