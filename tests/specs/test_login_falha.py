import pytest
from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from guara.application import Application
from guara import it
from tests.transactions.login_transaction import LoginWith
from tests.fixtures.driver import driver


def test_login_com_credenciais_invalidas(driver):
    usuario = "usuario_invalido"
    senha = "senha_invalida"

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys(usuario)

    driver.find_element(By.ID, "password").send_keys(senha)

    driver.find_element(By.ID, "login-button").click()

    mensagem_erro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))

    texto_erro = mensagem_erro.text

    assert mensagem_erro.is_displayed()

    assert "Username and password do not match" in texto_erro

    assert "inventory.html" not in driver.current_url



def test_login_usuario_invalido_2(driver):
    app = Application(driver)

    app.given(
        LoginWith,
        url="https://www.saucedemo.com",
        user="login_incorreto",
        password="senha_incorreta",
    ).then(
        it.Contains,
        "inventory"
    )
    