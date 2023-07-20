import pytest
from selenium import webdriver
from consts.constants import URL
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture(scope="function")
def init_webdriver():
    """
    Инициализация веб-драйвера Chrome.
    :return: Объект Webdriver.
    """
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url=URL)
    yield driver
    driver.quit()

