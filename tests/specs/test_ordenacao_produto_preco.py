import pytest
from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest

@pytest.mark.smoke
def test_ordenar_produtos_por_preco_crescente(driver):
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

    Select(combo_ordenacao).select_by_value("lohi")

    WebDriverWait(driver, 10).until(
        lambda navegador: len(navegador.find_elements(By.CLASS_NAME, "inventory_item_price")) > 0
    )

    elementos_preco = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    precos_exibidos = []

    for elemento in elementos_preco:
        preco = float(elemento.text.replace("$", "").strip())
        precos_exibidos.append(preco)

    assert precos_exibidos == sorted(precos_exibidos), (
        f"Os preços não estão em ordem crescente. " f"Preços exibidos: {precos_exibidos}"
    )
