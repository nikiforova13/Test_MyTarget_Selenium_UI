import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BaseCase:
    @pytest.fixture(scope="function", autouse=True)
    def init_auto_webdriver(self, init_webdriver):
        """
        Автоматическая инициализация драйвера.
        :param init_webdriver:
        :return:
        """
        self.driver = init_webdriver

    def expected_conditions_element(
        self, path: tuple, what: str, text: str | None = None
    ):
        if what == "clickable":
            return WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
                expected_conditions.element_to_be_clickable(path)
            )
        if what == "title":
            return WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
                expected_conditions.title_is(text)
            )
        if what == "located":
            return WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
                expected_conditions.presence_of_element_located(path))

    def find(self, path: tuple):
        return self.driver.find_element(*path)

    def find_element_and_send_text(self, path: tuple, text: str):
        element = self.find(path)
        element.clear()
        element.send_keys(text)
