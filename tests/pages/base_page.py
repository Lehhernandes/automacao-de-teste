from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value)))

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        self.find(by, value).click()

    def type(self, by, value, text):
        self.find(by, value).send_keys(text)

    def get_text(self, by, value):
        return self.find(by, value).text
