import pytest
from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_resetar_carrinho(driver):
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

    driver.find_element(By.ID, "react-burger-menu-btn").click()

    resetar_estado = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "reset_sidebar_link"))
    )

    resetar_estado.click()

    WebDriverWait(driver, 10).until(
        lambda navegador: len(navegador.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0
    )

    assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    itens_carrinho = driver.find_elements(By.CLASS_NAME, "cart_item")

    assert len(itens_carrinho) == 0, "O carrinho ainda contém itens após executar Reset App State."
