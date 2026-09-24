from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver


def test_checkout(driver):

    # =========================
    # 1. LOGIN
    # =========================
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Validação login
    assert "inventory.html" in driver.current_url

    # =========================
    # 2. ADICIONAR PRODUTO
    # =========================
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # =========================
    # 3. IR PARA CARRINHO
    # =========================
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    assert "cart.html" in driver.current_url

    # =========================
    # 4. INICIAR CHECKOUT
    # =========================
    driver.find_element(By.ID, "checkout").click()

    assert "checkout-step-one.html" in driver.current_url

    # =========================
    # 5. PREENCHER DADOS
    # =========================
    driver.find_element(By.ID, "first-name").send_keys("Douglas")
    driver.find_element(By.ID, "last-name").send_keys("Teste")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()

    assert "checkout-step-two.html" in driver.current_url

    # =========================
    # 6. FINALIZAR COMPRA
    # =========================
    driver.find_element(By.ID, "finish").click()

    # =========================
    # 7. VALIDAÇÃO FINAL
    # =========================
    mensagem = driver.find_element(By.CLASS_NAME, "complete-header")

    assert mensagem.is_displayed()
    assert "Thank you" in mensagem.text
