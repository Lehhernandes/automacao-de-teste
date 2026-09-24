import pytest
from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_acessar_carrinho_sem_itens(driver):
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    titulo_produtos = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert titulo_produtos.text == "Products"

    assert (
        len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0
    ), "O carrinho já possui itens antes da execução do teste."

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    titulo_carrinho = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert titulo_carrinho.text == "Your Cart"

    itens_carrinho = driver.find_elements(By.CLASS_NAME, "cart_item")

    assert (
        len(itens_carrinho) == 0
    ), "Foram encontrados itens no carrinho, mas o cenário espera um carrinho vazio."

    assert (
        len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0
    ), "A badge do carrinho está visível, indicando que existem itens adicionados."
