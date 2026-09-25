from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver
import pytest

@pytest.mark.regression
def test_checkout(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory.html" in driver.current_url

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    assert "cart.html" in driver.current_url

    driver.find_element(By.ID, "checkout").click()

    assert "checkout-step-one.html" in driver.current_url

    driver.find_element(By.ID, "first-name").send_keys("Douglas")
    driver.find_element(By.ID, "last-name").send_keys("Teste")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()

    assert "checkout-step-two.html" in driver.current_url

    driver.find_element(By.ID, "finish").click()
    mensagem = driver.find_element(By.CLASS_NAME, "complete-header")

    assert mensagem.is_displayed()
    assert "Thank you" in mensagem.text
