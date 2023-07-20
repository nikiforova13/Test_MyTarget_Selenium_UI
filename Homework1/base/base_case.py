import pytest


class BaseCase:

    @pytest.fixture(scope="function", autouse=True)
    def init_auto_webdriver(self, init_webdriver):
        """
        Автоматическая инициализация драйвера.
        :param init_webdriver:
        :return:
        """
        self.driver = init_webdriver
