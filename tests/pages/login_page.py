from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def open (self):
        self.driver.get("https://www.saucedemo.com")

    def login(self, user, password):
        self.type(*self.USERNAME, user)
        self.type(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)
