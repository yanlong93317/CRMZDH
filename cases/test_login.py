from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://192.168.1.211/crm/index.php?m=user&a=login')
driver.maximize_window()
driver.implicitly_wait(30)
sleep(1)
#登录
username_locator = (By.NAME, 'name')
password_locator = (By.NAME, 'password')
submit_locator = (By.CSS_SELECTOR, "input[value='登录']")
driver.find_element(*username_locator).send_keys('tangli')
sleep(1)
driver.find_element(*password_locator).send_keys('admin123456')
sleep(1)
driver.find_element(*submit_locator).click()
sleep(3)

driver.quit()