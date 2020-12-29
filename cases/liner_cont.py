from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
#打开登录网页
driver=webdriver.Chrome()
driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
#登录
driver.find_element(By.NAME,"name" ).send_keys("huachuan")
sleep(2)
driver.find_element(By.NAME,"password").send_keys("admin123456")
sleep(2)
driver.find_element(By.NAME,"submit").click()
sleep(2)

# 添加合同
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top >"
                                    " div > div > div.nav-collapse.collapse >"
                                    " ul:nth-child(1) > li:nth-child(7) > a").click() #点击合同
sleep(2)
#点击添加合同
driver.find_element(By.CSS_SELECTOR,"body > div.container > div.row > div:nth-child(1) > div > a").click()
sleep(1)
#点击商机选择框
driver.find_element(By.NAME,"business_name").click()
sleep(2)
driver.find_element(By.NAME,"business").click()  #选择商机
sleep(2)
driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(12) >"
                     " div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix"
                                    " > div > button:nth-child(1)").click()  #点击确定
sleep(2)
driver.find_element(By.NAME,"submit").click() #点确定
sleep(3)
#点击查看
driver.find_element(By.CSS_SELECTOR,"#form1 > table > tbody > tr:nth-child(1) > td:nth-child(10) > a:nth-child(1)").click()
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
# 合同编辑
#合同编辑
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top >"
                                    " div > div > div.nav-collapse.collapse >"
                                    " ul:nth-child(1) > li:nth-child(7) > a").click() #点击合同
sleep(2)
#点击编辑按钮
driver.find_element(By.CSS_SELECTOR,"#form1 > table > tbody > tr:nth-child(1) > td:nth-child(10) > a:nth-child(2)").click()
sleep(2)
#修改负责人
driver.find_element(By.NAME,"owner_role_name").click()
sleep(1)
driver.find_element(By.NAME,"owner").click()
#点击OK按钮
driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(13) >"
                                    " div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix >"
                                    " div > button:nth-child(1)").click()
sleep(3)
#点击保存
driver.find_element(By.NAME,"submit").click()
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
#搜索
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top >"
                                    " div > div > div.nav-collapse.collapse >"
                                    " ul:nth-child(1) > li:nth-child(7) > a").click() #点击合同
#搜索
driver.find_element(By.ID,"search").send_keys("6")
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#searchForm > ul > li:nth-child(4) > button").click()
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
# 翻页
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top >"
                                    " div > div > div.nav-collapse.collapse >"
                                    " ul:nth-child(1) > li:nth-child(7) > a").click() #点击合同
driver.find_element(By.CSS_SELECTOR,"#form1 > table > tfoot > tr > td > div.pagination "
                                    "> div.span4 > div > ul > li:nth-child(4) > span").click() #点击下一页
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

# 删除合同
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top >"
                                    " div > div > div.nav-collapse.collapse >"
                                    " ul:nth-child(1) > li:nth-child(7) > a").click() #点击合同
#选择合同
driver.find_element(By.NAME,"contract_id[]").click()
sleep(2)
driver.find_element(By.ID,"delete").click()
sleep(2)
driver.switch_to.alert.text
driver.switch_to.alert.accept()
sleep(5)
driver.quit()








