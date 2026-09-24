from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from guara.application import Application
from guara import it
from tests.transactions.login_transaction import LoginWith
from tests.fixtures.driver import driver

#comentar todo texto ctrl + /

def test_login(driver):

    # =========================
    # 1. LOGIN
    # =========================

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Validacao login
    assert "inventory.html" in driver.current_url




def test_login_2(driver):

    app = Application(driver)

    app.given(
        LoginWith,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce",
    ).then(
        it.Contains,
        "inventory"
    )