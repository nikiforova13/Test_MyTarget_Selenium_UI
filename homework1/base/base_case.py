import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from russian_names import RussianNames
from random import randint
from phone_gen import PhoneNumber
from homework1.locators.paths import ButtonForInputData, ButtonForAuthorization
from homework1.consts import constants


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
            return WebDriverWait(self.driver, 12, poll_frequency=0.1).until(
                expected_conditions.presence_of_element_located(path)
            )

    def find(self, path: tuple):
        return self.driver.find_element(*path)

    def find_element_and_send_text(self, path: tuple, text: str):
        element = self.find(path)
        element.clear()
        element.send_keys(text)

    @pytest.fixture(scope="function")
    def authorization(self):
        self.expected_conditions_element(
            ButtonForAuthorization.BUTTON_LOGIN, "clickable"
        ).click()
        self.find_element_and_send_text(
            ButtonForInputData.INPUT_EMAIL, constants.NUMBER_FOR_LOGIN
        )
        self.find_element_and_send_text(
            ButtonForInputData.INPUT_PASSWORD, constants.PASSWORD_FOR_LOGIN
        )
        self.find(ButtonForAuthorization.BUTTON_LOGIN_AFTER_INPUT_DATA).click()

    def generate_data(self):
        data = {}
        data["name"] = RussianNames().get_person()
        data["phone"] = PhoneNumber("Russia").get_number()
        data["Inn"] = randint(1000000000, 500000000000)
        return data
