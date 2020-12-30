from time import sleep
from selenium.webdriver.common.by import By
from page.home_page import HomePage


class MyAuth(HomePage):
    djpart_loc = (By.CSS_SELECTOR, "#add_role")  # 添加部门按钮
    departname_loc = (By.NAME, "name")  # 部门名
    useradmin_loc = (By.CSS_SELECTOR, "body > div.container > div.page-header >"
                                      " h4 > small > a:nth-child(2)")  # 用户管理
    nextpage_loc = (By.CSS_SELECTOR, "#user_form > div:nth-child(2) > table > tfoot > tr > "
                                     "td > div.pagination > div > div.span4 >"
                                     " div > ul > li:nth-child(4) > a")  # 翻页
    # driver.find_element(By.CSS_SELECTOR, "body > div.container > div.page-header >"
    #                                      " h4 > small > a:nth-child(2)").click()
    edituser_loc = (By.CSS_SELECTOR, "#user_form > div:nth-child(2) > "
                                     "table > tbody > tr:nth-child(1) > td:nth-child(8) > a:nth-child(2)")  # 编辑
    phone_loc = (By.NAME, "telephone")  # 号码
    djmake_loc = (By.NAME, "submit")
    djsure_loc = (By.CSS_SELECTOR, "body > div:nth-child(15) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span")  # 确定按钮
    # djsure1_loc=(By.XPATH,"/html/body/div[8]/div[3]/div/button[1]/span")
    alluser_loc = (By.CSS_SELECTOR, "#user_form > div:nth-child(1) > ul > li > ul > li > a")  # 全部员工
    seleadmin_loc = (By.CSS_SELECTOR, "#user_form > div:nth-child(1) > ul > "
                                      "li > ul > li > ul > li:nth-child(3) > a")  # 选择
    addusername_loc = (By.CSS_SELECTOR, "body > div.container > div.row > form > "
                                        "div:nth-child(1) > div > div > a:nth-child(3)")  # 添加用户
    username_loc = (By.XPATH, "/html/body/div[5]/div[2]/div/div"
                              "[2]/div[2]/form/table/tbody/tr[1]/td[2]/input")  # 用户名
    password_loc = (By.XPATH, "/html/body/div[5]/div[2]/div/div[2]/div[2]"
                              "/form/table/tbody/tr[2]/td[2]/input")  # 密码
    usercate_loc = (By.XPATH, "/html/body/div[5]/div[2]/div/div[2]/div[2]"
                              "/form/table/tbody/tr[3]/td[2]/select")
    usercate1_loc = (By.XPATH, "/html/body/div[5]/div[2]/div/div[2]/div[2]"
                               "/form/table/tbody/tr[3]/td[2]/select/option[2]")  # 用户类别
    depart_loc = (By.XPATH, "/html/body/div[5]/div[2]/"
                            "div/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/select")
    depart1_loc = (By.XPATH, "/html/body/div[5]/div[2]/"
                             "div/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/select/option[2]")  # 部门
    post_loc = (By.XPATH, "/html/body/div[5]/div[2]/div/div[2]"
                          "/div[2]/form/table/tbody/tr[5]/td[2]/select")
    post1_loc = (By.XPATH, "/html/body/div[5]/div[2]/div/div[2]"
                           "/div[2]/form/table/tbody/tr[5]/td[2]/select/option[1]")  # 岗位
    djkbai_loc = (By.CSS_SELECTOR, "body > div.container > div.row > div > ul")  # 空白
    sure_loc = (By.XPATH, "/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[6]/td[2]/input[1]")  # 确定按钮
    lastpage_loc = (By.CSS_SELECTOR, "#user_form > div:nth-child(2) > table > tfoot > tr > td "
                                     "> div.pagination > div > div.span4 > div > ul > li:nth-child(5) > a")  # 点击末页

    def djpart(self):
        self.find_element(self.djpart_loc).click()
        sleep(2)

    def depart_input(self, depart):
        self.find_element(self.departname_loc).send_keys(depart)
        sleep(3)

    def djsure(self):
        self.find_element(self.djsure_loc).click()
        sleep(2)

    def adddepart(self, denmae):
        '''增加部门'''
        self.djpart()
        self.depart_input(denmae)
        print("222222")
        self.djsure()
        sleep(7)
        self.driver.refresh()

    def useradmin(self):
        self.find_element(self.useradmin_loc).click()
        sleep(2)

    def nestpage(self):
        self.find_element(self.nextpage_loc).click()
        sleep(2)

    def nextpge(self):
        '''翻页'''
        self.useradmin()
        self.nestpage()

    def edit(self):
        self.find_element(self.edituser_loc).click()
        sleep(2)

    def phone_input(self, phone):
        self.find_element(self.phone_loc).clear()
        sleep(2)
        self.find_element(self.phone_loc).send_keys(phone)
        sleep(2)

    def djmake(self):
        self.find_element(self.djsure_loc).click()
        sleep(3)

    def edituserinfo(self, mobel):
        '''修改用户信息'''
        self.useradmin()
        self.edit()
        self.phone_input(mobel)
        self.djmake()

    def alluser(self):
        self.find_element(self.alluser_loc).click()
        sleep(2)

    def seleadmin(self):
        self.find_element(self.seleadmin_loc).click()
        sleep(2)

    def checkalluser(self):
        '''查看员工'''
        self.useradmin()
        self.alluser()
        self.seleadmin()

    def addusername(self):
        self.find_element(self.addusername_loc).click()
        sleep(2)

    def usernameadmin(self, usernamead):
        self.find_element(self.username_loc).send_keys(usernamead)
        sleep(2)

    def password_input(self, passwordadmin):
        self.find_element(self.password_loc).send_keys(passwordadmin)
        sleep(2)

    def usercate(self):
        self.find_element(self.usercate_loc).click()
        sleep(2)
        self.find_element(self.usercate1_loc).click()
        sleep(2)

    def depart(self):
        self.find_element(self.depart_loc).click()
        sleep(2)
        self.find_element(self.depart1_loc).click()
        sleep(2)

    def selepost(self):
        self.find_element(self.post_loc).click()
        sleep(2)
        self.find_element(self.post1_loc).click()
        sleep(2)

    def blank(self):
        self.find_element(self.djkbai_loc).click()
        sleep(2)

    def sure(self):
        self.find_element(self.sure_loc).click()
        sleep(2)

    def lastpage(self):
        self.find_element(self.lastpage_loc).click()
        sleep(2)

    def adduseradmin(self, username, password):
        '''新增用户'''
        self.addusername()
        self.usernameadmin(username)
        self.password_input(password)
        self.usercate()
        self.depart()
        self.selepost()
        self.blank()
        self.sure()
        self.lastpage()