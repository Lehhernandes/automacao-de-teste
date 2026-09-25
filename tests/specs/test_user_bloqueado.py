import pytest
from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from guara.application import Application
from guara import it
from tests.fixtures.driver import driver
from tests.transactions.login_transaction import LoginWith


def test_usuario_bloqueado(driver):
    usuario = "locked_out_user"
    senha = "secret_sauce"

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys(usuario)

    driver.find_element(By.ID, "password").send_keys(senha)

    driver.find_element(By.ID, "login-button").click()

    mensagem_erro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    texto_erro = mensagem_erro.text

    assert mensagem_erro.is_displayed(), "A mensagem de usuário bloqueado não foi exibida."

    assert (
        "locked out" in texto_erro.lower()
    ), f"Mensagem retornada diferente da esperada: {texto_erro}"

    assert (
        "inventory.html" not in driver.current_url
    ), "O usuário bloqueado conseguiu acessar a área de produtos."

    assert "saucedemo.com" in driver.current_url, "A aplicação não permaneceu na página de login."


