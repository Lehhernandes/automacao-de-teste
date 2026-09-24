import pytest
from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_continuar_comprando_apos_adicionar_item(driver):
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

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "continue-shopping")))

    driver.find_element(By.ID, "continue-shopping").click()

    titulo_produtos = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert titulo_produtos.text == "Products"

    produtos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(produtos) > 0, "Nenhum produto foi exibido após retornar para a página Products."
