import pytest
from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkout_parcial(driver):
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    titulo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert titulo.text == "Products"

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "checkout")))

    driver.find_element(By.ID, "checkout").click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "first-name")))

    driver.find_element(By.ID, "first-name").send_keys("João")

    driver.find_element(By.ID, "last-name").send_keys("Silva")

    driver.find_element(By.ID, "continue").click()

    mensagem_erro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )

    assert mensagem_erro.text == "Error: Postal Code is required"
