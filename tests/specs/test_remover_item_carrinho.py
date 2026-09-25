import pytest
from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.regression
def test_remover_item_do_carrinho(driver):
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    titulo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert titulo.text == "Products"

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert badge.text == "1"

    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    WebDriverWait(driver, 10).until(
        lambda navegador: len(navegador.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0
    )

    assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0
