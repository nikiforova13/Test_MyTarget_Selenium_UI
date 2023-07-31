import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from homework1.locators.paths import FieldsForInputData, ButtonForAuthorization
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
            WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
                expected_conditions.element_to_be_clickable(path)
            ).click()
        if what == "title":
            return WebDriverWait(self.driver, 10, poll_frequency=0.1).until(
                expected_conditions.title_is(text)
            )
        if what == "located":
            return WebDriverWait(self.driver, 12, poll_frequency=0.1).until(
                expected_conditions.presence_of_element_located(path)
            )
        if what == "visibility":
            return WebDriverWait(self.driver, 12, poll_frequency=0.1).until(expected_conditions.visibility_of_element_located(path))

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
        )
        self.find_element_and_send_text(
            FieldsForInputData.INPUT_EMAIL_FIELD, constants.NUMBER_FOR_LOGIN
        )
        self.find_element_and_send_text(
            FieldsForInputData.INPUT_PASSWORD_FIELD, constants.PASSWORD_FOR_LOGIN
        )
        self.find(ButtonForAuthorization.BUTTON_LOGIN_AFTER_INPUT_DATA).click()


