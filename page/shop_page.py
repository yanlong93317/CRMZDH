from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page.home_page import HomePage


class BisinShop(HomePage):
    djshop_loc = (By.CSS_SELECTOR, "body > div.container > div.row > div:nth-child(1) > div > a")  # 添加商机
    djuser_loc = (By.NAME, "customer_name")  # 客户名
    client_loc = (By.NAME, "customer")  # 选择客户名
    djok_loc = (By.CSS_SELECTOR, "body > div:nth-child(17) > div.ui-dialog-buttonpane.ui-widget-"
                                 "content.ui-helper-clearfix > div > button:nth-child(1) > span")  # 点击确定
    shopname_loc = (By.NAME, "name")  # 输入商家名
    price_loc = (By.NAME, "estimate_price")  # 输入价格
    sure_loc = (By.NAME, "submit")  # 保存按钮
    edid_loc = (By.CSS_SELECTOR, "#form1 > table > tbody > tr > td:nth-child(12) "
                                 "> a:nth-child(3)")  # 编辑按钮
    yjprice_loc = (By.NAME, "estimate_price")  # 清空数据并输入价格
    djcheck_loc = (By.CSS_SELECTOR, "#form1 > table > tbody >"
                                    " tr > td:nth-child(12) > a:nth-child(1)")  # 查看
    scerrn_loc = (By.CSS_SELECTOR, "#field > option:nth-child(4)")  # 选择筛选条件
    keyword_loc = (By.ID, "search")  # 输入关键字
    # djserach_loc = (By.CSS_SELECTOR, "#dosearch")  # 点击搜索按钮
    djserach_loc = (By.ID, "dosearch")
    boost_loc = (By.CSS_SELECTOR, "#form1 > table > tbody > "
                                  "tr:nth-child(1) > td:nth-child(12) > a.advance")  # 推进按钮
    djconf_loc = (By.CSS_SELECTOR, "#dialog-advance > form > table > tbody > tr:nth-child(5) "
                                   "> td:nth-child(2) > input.btn.btn-primary")  # 确定按钮
    table_loc = (By.CSS_SELECTOR, "#form1 > table > tbody")  # 找到表格
    ecct_lor = (By.NAME, "business_id[]")  # 选中商机
    djdel_loc = (By.ID, "delete")  # 删除
    addshop_loc=(By.CSS_SELECTOR,"#form1 > table > tbody > "
                            "tr:nth-child(1) > td:nth-child(4) > a")  #商机名
    yjprice_locator=(By.CSS_SELECTOR,"#tab1 > div.back_box.container3.mar-top > "
           "table.table.table-hover > tbody > tr:nth-child(8) > td:nth-child(2)") #价格
    numye_loc=(By.CSS_SELECTOR,"#td_colspan > div.pagination > div:nth-child(1)")  #数量
    state_loc=(By.CSS_SELECTOR,"#tab1 > div.back_box.container3.mar-top > table.table.table-hover > "
                               "tbody > tr:nth-child(6) > td:nth-child(4) > span")  #状态

    def djshop(self):
        self.find_element(self.djshop_loc).click()
        sleep(1)

    def djuser(self):
        self.find_element(self.djuser_loc).click()
        sleep(1)

    def client(self):
        self.find_element(self.client_loc).click()
        sleep(1)

    def diok(self):
        self.find_element(self.djok_loc).click()

    def input_shopname(self, shop):
        self.find_element(self.shopname_loc).send_keys(shop)
        sleep(1)

    def input_yujiprice(self, yjprice):
        self.find_element(self.price_loc).send_keys(yjprice)
        sleep(1)

    def sure(self):
        self.find_element(self.sure_loc).click()
        sleep(1)

    def shopadd(self):
        shopname=self.find_element(self.addshop_loc).text.strip()
        return  shopname
    def addshop(self, shopname, yujprice):
        '''添加商机'''
        self.djshop()
        self.djuser()
        self.client()
        self.diok()
        self.input_shopname(shopname)
        self.input_yujiprice(yujprice)
        self.sure()

    def edit(self):
        self.find_element(self.edid_loc).click()
        sleep(1)

    def input_yijprice(self, yjprice):
        self.find_element(self.yjprice_loc).clear()
        sleep(1)
        self.find_element(self.yjprice_loc).send_keys(yjprice)
        sleep(1)

    def djcheck(self):
        self.find_element(self.djcheck_loc).click()
        sleep(1)
    def yujiprice(self):
        yjprice=int(self.find_element(self.yjprice_locator).text)
        return  yjprice
    def editshop(self, yijprice):
        '''商机编辑'''
        self.edit()
        self.input_yijprice(yijprice)
        self.sure()
        self.djcheck()

    def scachce(self):
        self.find_element(self.scerrn_loc).click()
        sleep(1)

    def input_keyword(self, keyword):
        self.find_element(self.keyword_loc).send_keys(keyword)
        sleep(1)

    def djserach(self):
        self.find_element(self.djserach_loc).click()
        sleep(1)
    def djnumber(self):
        number=self.find_element(self.numye_loc).text
        return number
    def serach(self,keiwords):
        '''商机搜索'''
        self.scachce()
        self.input_keyword(keiwords)
        self.djserach()

    def djboost(self):
        self.find_element(self.boost_loc).click()
        sleep(1)

    def stage(self, num):
        loc = self.driver.find_element_by_name("status_id")  # 下拉列表
        select = Select(loc)
        select.select_by_index(num)
        sleep(1)
    def stge(self,number):
        loc = self.driver.find_element_by_name("status_id")  # 下拉列表
        select = Select(loc)
        select.select_by_index(number)
        sleep(1)
        aa=select.options[number].text
        return aa
    def djconf(self):
        self.find_element(self.djconf_loc).click()
        sleep(1)
    def status(self):
        status=self.find_element(self.state_loc).text
        return status
    def boost(self):
        '''推进'''
        self.djconf()
        self.djcheck()
        sleep(4)

    # def deltab(self,num,nm):
    #     table_loc=self.find_element(self.table_loc)
    #     tr_loc = table_loc.find_elements(By.CSS_SELECTOR, "td:nth-child({})".format(num))  # 第四列
    #     tst = []
    #     for tds in tr_loc:
    #         td = tds.find_element_by_tag_name("a").text
    #         tst.append(td)
    #    return tst[nm]
    def ecct(self):
        self.find_element(self.ecct_lor).click()
        sleep(1)

    def djdel(self):
        self.find_element(self.djdel_loc).click()
        sleep(1)

    def delshop(self):
        '''删除商机'''
        self.ecct()
        self.djdel()
        self.driver.switch_to.alert.text  # 获取alert上的文本
        sleep(1)
        self.driver.switch_to.alert.accept()  # 点击确定
