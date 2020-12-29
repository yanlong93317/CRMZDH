from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#打开登录网页
driver=webdriver.Chrome()
driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
#登录
driver.find_element(By.NAME,"name" ).send_keys("huachuan")
sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123456")
sleep(1)
driver.find_element(By.NAME,"submit").click()
sleep(2)
# 添加部门
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > "
                                    "div.nav-collapse.collapse >"
                                    " ul.nav.pull-right > li:nth-child(6) > a > img").click()
sleep(1)
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > "
                                    "ul.nav.pull-right > li.dropdown.open"
                                    " > ul > li:nth-child(5) > a").click()

#添加部门
driver.find_element(By.CSS_SELECTOR,"#add_role").click()
sleep(2)
driver.find_element(By.NAME,"name").send_keys("baoan")
sleep(3)
driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(15) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix >"
                                    " div > button:nth-child(1) > span").click()
sleep(6)
driver.refresh()
sleep(3)
#
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > "
                                    "div.nav-collapse.collapse >"
                                    " ul.nav.pull-right > li:nth-child(6) > a > img").click()
sleep(1)
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > "
                                    "ul.nav.pull-right > li.dropdown.open"
                                    " > ul > li:nth-child(5) > a").click()
sleep(3)
driver.quit()
driver=webdriver.Chrome()
driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
#登录
driver.find_element(By.NAME,"name" ).send_keys("huachuan")
sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123456")
sleep(1)
driver.find_element(By.NAME,"submit").click()
sleep(2)
# #添加用户
driver.find_element(By.CSS_SELECTOR,"body > div.container > div.row > form > div:nth-child(1) > div > div > a:nth-child(3)").click()
sleep(2)
driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[1]/td[2]/input").send_keys("yyye") #用户名
sleep(1)
driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys("123456") #密码
sleep(1)
driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/select").click() #用户类别
sleep(2)
driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/select/option[2]").click()
sleep(2)
driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/select").click() #部门
sleep(2)
driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/select/option[2]").click()
sleep(2)
driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/select").click() #岗位
sleep(2)
driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/select/option[1]").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"body > div.container > div.page-header > h4").click()
sleep(2)
driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div[2]/div[2]/form/table/tbody/tr[6]/td[2]/input[1]").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#user_form > div:nth-child(2) > table > tfoot > tr > td > div.pagination > div > div.span4 > div > ul > li:nth-child(5) > a").click() #点击末页
sleep(5)
driver.quit()

driver=webdriver.Chrome()
driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
#登录
driver.find_element(By.NAME,"name" ).send_keys("huachuan")
sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123456")
sleep(1)
driver.find_element(By.NAME,"submit").click()
sleep(2)
#用户翻页

driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > "
                                    "div.nav-collapse.collapse >"
                                    " ul.nav.pull-right > li:nth-child(6) > a > img").click()
sleep(1)
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > "
                                    "ul.nav.pull-right > li.dropdown.open"
                                    " > ul > li:nth-child(5) > a").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"body > div.container > div.page-header >"
                                    " h4 > small > a:nth-child(2)").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#user_form > div:nth-child(2) > table > tfoot > tr > "
                                    "td > div.pagination > div > div.span4 >"
                                    " div > ul > li:nth-child(4) > a").click()
sleep(8)
driver.quit()

driver=webdriver.Chrome()
driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
#登录
driver.find_element(By.NAME,"name" ).send_keys("huachuan")
sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123456")
sleep(1)
driver.find_element(By.NAME,"submit").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > "
                                    "div.nav-collapse.collapse >"
                                    " ul.nav.pull-right > li:nth-child(6) > a > img").click()
sleep(1)
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > "
                                    "ul.nav.pull-right > li.dropdown.open"
                                    " > ul > li:nth-child(5) > a").click()
sleep(2)

#修改用户信息
driver.find_element(By.CSS_SELECTOR,"body > div.container > div.page-header >"
                                    " h4 > small > a:nth-child(2)").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#user_form > div:nth-child(2) > "
                                    "table > tbody > tr:nth-child(1) >"
                                    " td:nth-child(8) > a:nth-child(2)").click()
sleep(2)
driver.find_element(By.NAME,"telephone").clear()
sleep(2)
driver.find_element(By.NAME,"telephone").send_keys("13265479897")
sleep(2)
driver.find_element(By.NAME,"submit").click()
sleep(2)
driver.quit()


driver=webdriver.Chrome()
driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
#登录
driver.find_element(By.NAME,"name" ).send_keys("huachuan")
sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123456")
sleep(1)
driver.find_element(By.NAME,"submit").click()
sleep(2)
#按类别查看员工
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > "
                                    "div.nav-collapse.collapse >"
                                    " ul.nav.pull-right > li:nth-child(6) > a > img").click()
sleep(1)
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > "
                                    "ul.nav.pull-right > li.dropdown.open"
                                    " > ul > li:nth-child(5) > a").click()

sleep(2)
driver.find_element(By.CSS_SELECTOR,"body > div.container > div.page-header > h4 > small > a:nth-child(2)").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#user_form > div:nth-child(1) > ul > li > ul > li > a").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#user_form > div:nth-child(1) > ul > li > ul > li > ul > li:nth-child(3) > a").click()
sleep(4)
driver.quit()
