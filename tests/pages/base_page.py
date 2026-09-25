from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_for_element(self, by, value):
        return self.wait.until(
            EC.visibility_of_element_located((by, value))
        )

    def wait_for_clickable(self, by, value):
        return self.wait.until(
            EC.element_to_be_clickable((by, value))
        )

    def find(self, by, value):
        return self.wait_for_element(by, value)

    def click(self, by, value):
        self.wait_for_clickable(by, value).click()

    def type(self, by, value, text):
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, value):
        return self.wait_for_element(by, value).text