from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# 打开登录网页
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome()
# driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
# # 登录
# driver.find_element(By.NAME, "name").send_keys("huachuan")
# sleep(1)
# driver.find_element(By.NAME, "password").send_keys("admin123456")
# sleep(1)
# driver.find_element(By.NAME, "submit").click()
# sleep(2)
# # 添加部门
# driver.find_element(By.CSS_SELECTOR, "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > "
#                                      "div.nav-collapse.collapse >"
#                                      " ul.nav.pull-right > li:nth-child(6) > a > img").click()
# sleep(1)
# driver.find_element(By.CSS_SELECTOR,
#                     "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > "
#                     "ul.nav.pull-right > li.dropdown.open"
#                     " > ul > li:nth-child(5) > a").click()
#
# # 添加部门
# driver.find_element(By.CSS_SELECTOR, "#add_role").click()
# sleep(2)
# driver.find_element(By.NAME, "name").send_keys("ban")
# sleep(3)
# loc = driver.find_element_by_name("status_id")  # 下拉列表
# select = Select(loc)
# select.select_by_index(2)
# driver.find_element(By.CSS_SELECTOR,
#                     "body > div:nth-child(15) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix >"
#                     " div > button:nth-child(1) > span").click()
# sleep(6)
# driver.refresh()
# sleep(3)
# driver.find_element(By.CSS_SELECTOR, "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > "
#                                      "div.nav-collapse.collapse >"
#                                      " ul.nav.pull-right > li:nth-child(6) > a > img").click()
# sleep(1)
# driver.find_element(By.CSS_SELECTOR,
#                     "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > "
#                     "ul.nav.pull-right > li.dropdown.open"
#                     " > ul > li:nth-child(5) > a").click()
# sleep(3)
# driver.quit()
# driver = webdriver.Chrome()
# driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
# # 登录
# driver.find_element(By.NAME, "name").send_keys("huachuan")
# sleep(1)
# driver.find_element(By.NAME, "password").send_keys("admin123456")
# sleep(1)
# driver.find_element(By.NAME, "submit").click()
# sleep(2)
# # #添加用户
# driver.find_element(By.CSS_SELECTOR, "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > "
#                                      "div.nav-collapse.collapse >"
#                                      " ul.nav.pull-right > li:nth-child(6) > a > img").click()
# sleep(1)
# driver.find_element(By.CSS_SELECTOR,
#                     "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > "
#                     "ul.nav.pull-right > li.dropdown.open"
#                     " > ul > li:nth-child(5) > a").click()
# driver.find_element(By.CSS_SELECTOR,
#                     "body > div.container > div.row > form > div:nth-child(1) > div > div > a:nth-child(3)").click()
# sleep(2)
# # #
# # aa=driver.find_element(By.CSS_SELECTOR,"#add > table > tbody")
# # aa.find_element(By.TAG_NAME,"td:nth-child(2)")
#
#
# driver.find_element(By.XPATH,
#                     "/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[1]/td[2]/input").send_keys(
#     "yyye")  # 用户名
# sleep(1)
# driver.find_element(By.XPATH,
#                     "/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys(
#     "123456")  # 密码
# sleep(1)
# # driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/select").click() #用户类别
# sleep(2)
# driver.find_element(By.XPATH,
#                     "/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/select/option[2]").click()
# sleep(2)
# driver.find_element(By.XPATH,
#                     "/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/select").click()  # 部门
# sleep(2)
# driver.find_element(By.XPATH,
#                     "/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/select/option[2]").click()
# sleep(2)
# driver.find_element(By.XPATH,
#                     "/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/select").click()  # 岗位
# sleep(2)
# driver.find_element(By.XPATH,
#                     "/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/select/option[1]").click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, "body > div.container > div.page-header > h4").click()
# sleep(2)
# driver.find_element(By.XPATH,
#                     "/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[6]/td[2]/input[1]").click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR,
#                     "#user_form > div:nth-child(2) > table > tfoot > tr > td > div.pagination > div > div.span4 > div > ul > li:nth-child(5) > a").click()  # 点击末页
# sleep(5)
# driver.quit()
driver = webdriver.Chrome()
driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
# 登录
driver.find_element(By.NAME, "name").send_keys("huachuan")
sleep(1)
driver.find_element(By.NAME, "password").send_keys("admin123456")
sleep(1)
driver.find_element(By.NAME, "submit").click()
# sleep(2)
# # 用户翻页
#
# driver.find_element(By.CSS_SELECTOR, "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > "
#                                      "div.nav-collapse.collapse >"
#                                      " ul.nav.pull-right > li:nth-child(6) > a > img").click()
# sleep(1)
# driver.find_element(By.CSS_SELECTOR,
#                     "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > "
#                     "ul.nav.pull-right > li.dropdown.open"
#                     " > ul > li:nth-child(5) > a").click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, "body > div.container > div.page-header >"
#                                      " h4 > small > a:nth-child(2)").click()  # 用户管理
# sleep(2)
# aa=driver.find_element(By.CSS_SELECTOR,"#user_form > div:nth-child(2) > table > tfoot >"
#                                     " tr > td > div.pagination > div > div:nth-child(1)").text
# print(aa)
#
# driver.find_element(By.CSS_SELECTOR, "#user_form > div:nth-child(2) > table > tfoot > tr > "
#                                      "td > div.pagination > div > div.span4 >"
#                                     " div > ul > li:nth-child(4) > a").click()  # 翻页
#
# bb=driver.find_element(By.CSS_SELECTOR,"#user_form > div:nth-child(2) > table > "
#                                        "tfoot > tr > td > div.pagination > div > div:nth-child(1)").text
# print(bb)
# # sleep(8)
# driver.quit()
#
# driver = webdriver.Chrome()
# driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
# # 登录
# driver.find_element(By.NAME, "name").send_keys("huachuan")
# sleep(1)
# driver.find_element(By.NAME, "password").send_keys("admin123456")
# sleep(1)
# driver.find_element(By.NAME, "submit").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > "
                                     "div.nav-collapse.collapse >"
                                     " ul.nav.pull-right > li:nth-child(6) > a > img").click()
sleep(1)
driver.find_element(By.CSS_SELECTOR,
                    "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > "
                    "ul.nav.pull-right > li.dropdown.open"
                    " > ul > li:nth-child(5) > a").click()
#
#
#
# aa=driver.find_element(By.CSS_SELECTOR,"#browser > li > ul")
# cs=aa.find_elements(By.TAG_NAME,"li")
# for i in cs:
#     ss=i.text
#     bb='失败'
#     if "vvvv" in ss:
#         bb="成功"
#         # print("成功")
#     else:
#         pass
#     if bb=="成功":
#         print(bb)
#     elif bb=="失败" and i==cs[-1]:
#         print(bb)




# for j in range(ss):
#     print(j)
    # cs=aa.find_element(By.CSS_SELECTOR,"#browser > li > ul > li.last > span").text
# print(cs)


# sleep(2)
#
# 修改用户信息
driver.find_element(By.CSS_SELECTOR, "body > div.container > div.page-header >"
                                     " h4 > small > a:nth-child(2)").click()


tab_loc=driver.find_element(By.CSS_SELECTOR,"#user_form > div:nth-child(2) > table > tbody")
tr_loc=tab_loc.find_elements(By.TAG_NAME,"tr")
pst=[]
#获取号码
for td in tr_loc:
    dd=td.find_element(By.CSS_SELECTOR,"td:nth-child(2)").text
    pst.append(dd)
print(pst[0])



#
# for line in range(len(tr_loc)):
#     tr_loc[line].find_elements(By.TAG_NAME,"td")[0].find_element(By.TAG_NAME,"a").click()






#
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#user_form > div:nth-child(2) > "
#                                      "table > tbody > tr:nth-child(1) >"
#                                      " td:nth-child(8) > a:nth-child(2)").click()
# sleep(2)
# driver.find_element(By.NAME, "telephone").clear()
# sleep(2)
# driver.find_element(By.NAME, "telephone").send_keys("13265479897")
# sleep(2)
# driver.find_element(By.NAME, "submit").click()
# sleep(2)
# driver.quit()
# #
#
# driver = webdriver.Chrome()
# driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
# # 登录
# driver.find_element(By.NAME, "name").send_keys("huachuan")
# sleep(1)
# driver.find_element(By.NAME, "password").send_keys("admin123456")
# sleep(1)
# driver.find_element(By.NAME, "submit").click()
# sleep(2)
# # 按类别查看员工
# driver.find_element(By.CSS_SELECTOR, "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > "
#                                      "div.nav-collapse.collapse >"
#                                      " ul.nav.pull-right > li:nth-child(6) > a > img").click()
# sleep(1)
# driver.find_element(By.CSS_SELECTOR,
#                     "body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > "
#                     "ul.nav.pull-right > li.dropdown.open"
#                     " > ul > li:nth-child(5) > a").click()
#
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, "body > div.container > div.page-header > h4 > small > a:nth-child(2)").click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#user_form > div:nth-child(1) > ul > li > ul > li > a").click()  # 全部员工
# # sleep(2)
# driver.find_element(By.CSS_SELECTOR,
#                     "#user_form > div:nth-child(1) > ul > li > ul > li > ul > li:nth-child(3) > a").click()  # 选择
# sleep(4)
# driver.quit()
