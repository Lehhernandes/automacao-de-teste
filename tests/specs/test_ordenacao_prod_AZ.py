import pytest
from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest

@pytest.mark.smoke

def test_ordenar_produtos_por_nome_az(driver):
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    titulo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert titulo.text == "Products"

    combo_ordenacao = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container"))
    )

    Select(combo_ordenacao).select_by_value("az")

    elementos_produto = WebDriverWait(driver, 10).until(
        lambda navegador: navegador.find_elements(By.CLASS_NAME, "inventory_item_name")
    )

    nomes_produtos = [elemento.text for elemento in elementos_produto]

    assert nomes_produtos == sorted(nomes_produtos), (
        f"Os produtos não estão em ordem alfabética. " f"Ordem exibida: {nomes_produtos}"
    )
