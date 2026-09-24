import pytest
from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logout_com_sucesso(driver):
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    titulo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert titulo.text == "Products"

    driver.find_element(By.ID, "react-burger-menu-btn").click()

    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )

    logout_link.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login-button")))

    assert driver.find_element(By.ID, "user-name").is_displayed()

    assert driver.find_element(By.ID, "password").is_displayed()

    assert driver.find_element(By.ID, "login-button").is_displayed()

    assert "saucedemo.com" in driver.current_url
