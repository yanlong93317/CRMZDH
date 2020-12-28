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

 #添加商机
#点击商机
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(3)").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"body > div.container > div.row > div:nth-child(1) > div > a").click()  #点击添加商机
sleep(1)
driver.find_element(By.NAME,"customer_name").click()  #点击客户名
sleep(2)
driver.find_element(By.NAME,"customer").click() #选择客户名
sleep(1)
driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(17) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span").click()  #点击确定
sleep(1)
driver.find_element(By.NAME,"name").send_keys("yyrr")  #输入商家名
sleep(1)
driver.find_element(By.NAME,"estimate_price").send_keys("2000")   #输入价格
sleep(1)
driver.find_element(By.NAME,"submit").click()  #点击保存按钮
sleep(2)

#'''商机编辑'''
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(3)").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#form1 > table > tbody > tr > td:nth-child(12) > a:nth-child(3)").click()  #点击编辑按钮
sleep(1)
driver.find_element(By.NAME,"estimate_price").clear()  #情空数据
driver.find_element(By.NAME,"estimate_price").send_keys("30000")  #输入数据
sleep(2)
driver.find_element(By.NAME,"submit").click()  #点击确定按钮
sleep(1)
driver.find_element(By.CSS_SELECTOR,"#form1 > table > tbody > tr > td:nth-child(12) > a:nth-child(1)").click()  #查看
sleep(5)
driver.find_element(By.CSS_SELECTOR,"#tab1 > div.container2.top-pad > div > a:nth-child(3)").click() #返回
sleep(2)
#搜索
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(3)").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#field > option:nth-child(4)").click() #选择筛选条件
sleep(1)
driver.find_element(By.ID,"search").send_keys("二")  #输入关键字
sleep(2)
driver.find_element(By.ID,"dosearch").click()   #点击搜索按钮
sleep(2)
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(3)").click()  #点击商机
sleep(2)
#推进
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(3)").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#form1 > table > tbody > tr:nth-child(1) > td:nth-child(12) > a.advance").click()  #点击推进按钮
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#dialog-advance > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > select > option:nth-child(3)").click()  #选择阶段
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#dialog-advance > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > input.btn.btn-primary").click()  #点击确定按钮
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#form1 > table > tbody > tr:nth-child(1) > td:nth-child(12) > a:nth-child(1)").click()  #点击查看
sleep(5)
driver.find_element(By.CSS_SELECTOR,"#tab1 > div.container2.top-pad > div > a:nth-child(3)").click() #返回
sleep(2)
# 删除商机
driver.find_element(By.CSS_SELECTOR,"body > div.navbar.navbar-inverse.navbar-fixed-top > div > div > div.nav-collapse.collapse > ul:nth-child(1) > li:nth-child(3)").click()
sleep(2)
driver.find_element(By.NAME,"business_id[]").click()  #选中商机
sleep(2)
driver.find_element(By.ID,"delete").click()  #点击删除
sleep(2)
driver.switch_to.alert.text #获取alert上的文本
sleep(1)
driver.switch_to.alert.accept()  #点击确定
sleep(4)
driver.quit()