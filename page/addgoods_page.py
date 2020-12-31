from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类


class AddGoods(BasePage):
    goosname_loc = (By.CSS_SELECTOR, '#name')
    oksubmit_loc = (By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td > input:nth-child(1)')
    developmentteam_loc = (By.CSS_SELECTOR, '#development_team')

    def goodsname(self, goodsname):
        self.find_element(self.goosname_loc).send_keys(goodsname)

    def developmentteam(self, developmentteam):
        self.find_element(self.developmentteam_loc).send_keys(developmentteam)

    def oksubmit(self):
        self.find_element(self.oksubmit_loc).click()

    def addgoodset(self, goodsname, developmentteam):
        self.goodsname(goodsname)
        self.developmentteam(developmentteam)
        self.oksubmit()
