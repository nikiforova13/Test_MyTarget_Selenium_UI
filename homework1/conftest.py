import pytest
from selenium import webdriver
from homework1.consts.constants import URL
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def init_webdriver():
    """
    Инициализация веб-драйвера Chrome.
    :return: Объект Webdriver.
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url=URL)
    driver.maximize_window()
    yield driver
    driver.quit()

