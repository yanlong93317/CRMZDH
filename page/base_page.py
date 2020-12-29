from selenium import webdriver

<<<<<<< HEAD

class BasePage():
    _url = 'http://192.168.1.211/crm/index.php?m=user&a=login'

    def __init__(self, driver, url=None):
        self.driver = driver
        if not url:
            url = self._url
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator, element=None):
        if element and isinstance(element, WebElement):
            return element.find_element(*locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator, element=None):
        if element and isinstance(element, WebElement):
            return element.find_elements(*locator)
        return self.driver.find_elements(*locator)


=======
driver=webdriver.Chrome()
driver=driver.get("http://192.168.1.211/crm/index.php?m=user&a=login")
driver.find_element_
>>>>>>> e0e7a321a8c9884ee5f86e7d28e67c93e9e1c5c2
