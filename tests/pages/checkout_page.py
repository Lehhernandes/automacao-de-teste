from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")

    def fill_form(self, name, last, zip_code):
        self.type(*self.FIRST_NAME, name)
        self.type(*self.LAST_NAME, last)
        self.type(*self.POSTAL_CODE, zip_code)

    def continue_checkout(self):
        self.click(*self.CONTINUE)

    def finish(self):
        self.click(*self.FINISH)

        WebDriverWait(self.driver, 15).until(
            EC.url_contains("checkout-complete")
        )

    def get_success_message(self):
        return self.get_text(*self.SUCCESS_MSG)