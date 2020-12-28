from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("http://localhost:8080/upload/admin")
loc = (By.NAME, "username")
pas=(By.NAME,"password")
sub = (By.CSS_SELECTOR, "body > form > table > tbody > tr:nth-child(2)"
                                     " > td > table > tbody > tr:nth-child(5) >"
                                     " td:nth-child(2) > input")
driver.find_element(*loc).send_keys("admin")
driver.find_element(*pas).send_keys("admin123456")
sleep(1)
driver.find_element(*sub).click()
driver.switch_to.frame("menu-frame")
quan=driver.find_element(By.CSS_SELECTOR,"#menu-ul > li.collapse.lis.ico_8")
sleep(1)
quan.click()
lieb=driver.find_element(By.CSS_SELECTOR,"#menu-ul > li.explode.lis.ico2_8 >"                                      " ul > li:nth-child(1) > a")
lieb.click()
driver.switch_to.parent_frame()
driver.switch_to.default_content()
driver.switch_to.frame("main-frame")
tian=driver.find_element(By.CSS_SELECTOR,"body > h1 > span.action-span > a")
sleep(1)
tian.click()
driver.find_element(By.NAME,"user_name").send_keys("long")
driver.find_element(By.NAME,"email").send_keys("125676@qq.com")
driver.find_element(By.NAME,"password").send_keys("admin123456")
driver.find_element(By.NAME,"pwd_confirm").send_keys("admin123456")
btn=driver.find_element(By.CSS_SELECTOR,"body > div.main-div > form > table > tbody > "
                                        "tr:nth-child(5) > td >"
                                        " input:nth-child(1)")
sleep(2)
btn.click()









