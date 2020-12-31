from selenium import webdriver


class BroswerModel():
    def broswer_chrome(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        return driver
