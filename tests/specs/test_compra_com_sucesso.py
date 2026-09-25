import pytest
from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_compra_produto_com_sucesso(driver):

    usuario = "standard_user"
    senha = "secret_sauce"
    nome = "Joao"
    sobrenome = "Silva"
    cep = "01001000"

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys(usuario)

    driver.find_element(By.ID, "password").send_keys(senha)

    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "inventory_container"))
    )

    assert "inventory.html" in driver.current_url

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert badge.text == "1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    assert "cart.html" in driver.current_url

    driver.find_element(By.ID, "checkout").click()

    assert "checkout-step-one.html" in driver.current_url

    driver.find_element(By.ID, "first-name").send_keys(nome)

    driver.find_element(By.ID, "last-name").send_keys(sobrenome)

    driver.find_element(By.ID, "postal-code").send_keys(cep)

    driver.find_element(By.ID, "continue").click()

    assert "checkout-step-two.html" in driver.current_url

    driver.find_element(By.ID, "finish").click()

    mensagem_confirmacao = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )

    assert mensagem_confirmacao.is_displayed()

    assert mensagem_confirmacao.text == "Thank you for your order!"

    assert "checkout-complete.html" in driver.current_url
