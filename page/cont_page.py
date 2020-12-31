from time import sleep
from selenium.webdriver.common.by import By
from page.home_page import HomePage


class MyCont(HomePage):
    addcont_loc = (By.CSS_SELECTOR, "body > div.container > "
                                    "div.row > div:nth-child(1) > div > a")  # 添加合同
    # 点击商机选择框
    businesscont_loc = (By.NAME, "business_name")  # 商机选择框
    selectbusin_loc = (By.NAME, "business")  # 选择商机
    sleep(1)
    djsure_loc = (By.CSS_SELECTOR, "body > div:nth-child(12) >"
                                   " div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix"
                                   " > div > button:nth-child(1)")  # 点击确定
    contprice_loc = (By.NAME, "price")  # 合同金额
    djmake_loc = (By.NAME, "submit")  # 确定
    contedit_loc = (By.CSS_SELECTOR, "#form1 > table > tbody > tr:nth-child(1) > "
                                     "td:nth-child(10) > a:nth-child(2)")  # 编辑按钮
    getback_loc = (By.CSS_SELECTOR, "#tab1 > div.container2.top-pad > div > a:nth-child(3)") #返回
    getbacke_loc=(By.CSS_SELECTOR,"#tab1 > form > table > tfoot > tr > td:nth-child(2) > input:nth-child(2)") #返回
    keyword_loc = (By.ID, "search")  # 关键字
    djsearch_loc = (By.CSS_SELECTOR, "#searchForm > ul > li:nth-child(4) > button")  # 搜索按钮
    nextpage_loc = (By.CSS_SELECTOR, "#form1 > table > tfoot > tr > td > div.pagination > div.span4 > div > ul > li:nth-child(4) > a")  # 点击下一页
    selcont_loc = (By.NAME, "contract_id[]")  # 选择合同
    djdel_loc = (By.ID, "delete")  # 删除
    addshopfy_loc=(By.CSS_SELECTOR,"#form1 > table > tfoot > tr > td > "
                                   "div.pagination > div:nth-child(1)")  #页数
    money_loc=(By.CSS_SELECTOR,"#form1 > table > tbody > tr:nth-child(1) > td:nth-child(7)")

    def djaddcont(self):
        self.find_element(self.addcont_loc).click()
        sleep(1)

    def djbucont(self):
        self.find_element(self.businesscont_loc).click()
        sleep(1)

    def selectcont(self):
        self.find_element(self.selectbusin_loc).click()
        sleep(1)

    def djsure(self):
        self.find_element(self.djsure_loc).click()
        sleep(1)

    def contprice(self, conprice):
        self.find_element(self.contprice_loc).clear()
        sleep(1)
        self.find_element(self.contprice_loc).send_keys(conprice)
        sleep(1)

    def djmake(self):
        self.find_element(self.djmake_loc).click()
        sleep(1)
    def contfy(self):
        yeshu=self.find_element(self.addshopfy_loc).text
        return yeshu
    def addcont(self, contprice):
        '''增加合同'''
        self.djaddcont()
        self.djbucont()
        self.selectcont()
        self.djsure()
        self.contprice(contprice)
        self.djmake()

    def djedit(self):
        self.find_element(self.contedit_loc).click()
        sleep(1)

    def getback(self):
        self.find_element(self.getback_loc).click()
        sleep(1)
    def geiback2(self):
        self.find_element(self.getbacke_loc).click()
        sleep(1)
    def money(self):
        money=int(self.find_element(self.money_loc).text[:-4])
        return money


    def editcont(self, editprice):
        '''修改合同'''
        self.djedit()
        self.contprice(editprice)
        self.djmake()
        self.getback()
        self.geiback2()
        sleep(1)
        self.driver.refresh()

    def keywprd_input(self, keyword):
        self.find_element(self.keyword_loc).clear()
        sleep(1)
        self.find_element(self.keyword_loc).send_keys(keyword)
        sleep(1)

    def djserach(self):
        self.find_element(self.djsearch_loc).click()
        sleep(1)

    def search(self, kyword):
        '''搜索'''
        self.keywprd_input(kyword)
        self.djserach()

    def nextpage(self):
        self.find_element(self.nextpage_loc).click()
        sleep(1)



    def checknext(self):
        '''下一页'''
        self.nextpage()

    def seletcont(self):
        self.find_element(self.selcont_loc).click()
        sleep(1)

    def djdel(self):
        self.find_element(self.djdel_loc).click()

    def djassert(self):
        self.driver.switch_to.alert.text
        sleep(1)
        self.driver.switch_to.alert.accept()
        sleep(1)

    def delcont(self):
        '''删除合同'''
        self.seletcont()
        self.djdel()
        self.djassert()
