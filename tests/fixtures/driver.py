from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import tempfile
import pytest


@pytest.fixture
def driver():
    driver = driver_func()
    yield driver

    driver.quit()

def driver_func():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }

    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-features=PasswordLeakDetection")
    chrome_options.add_argument("--safebrowsing-disable-leakdetection")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver
