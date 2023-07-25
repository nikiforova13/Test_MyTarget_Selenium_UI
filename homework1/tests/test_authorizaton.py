import time

import pytest

from homework1.base.base_case import BaseCase
from homework1.consts import constants
from homework1.locators.paths import ButtonForInputData, ButtonForNavigatingPages, Check, ButtonForAuthorization, ButtonForSavingChanges


@pytest.mark.ui
class TestAuthorization(BaseCase):
    def test_log_in_with_correct_data(self):
        """
        Тест проверяет, что при вводе корректных данных осуществляется вход в учетную запись пользователя.
        :return:
        """
        self.expected_conditions_element(ButtonForAuthorization.BUTTON_LOGIN, "clickable").click()
        self.find_element_and_send_text(ButtonForInputData.INPUT_EMAIL, constants.NUMBER_FOR_LOGIN)
        self.find_element_and_send_text(
            ButtonForInputData.INPUT_PASSWORD, constants.PASSWORD_FOR_LOGIN
        )
        self.find(ButtonForAuthorization.BUTTON_LOGIN_AFTER_INPUT_DATA).click()
        result = self.expected_conditions_element(
            ButtonForAuthorization.BUTTON_LOGIN, "title", "Кампании"
        )
        assert result == True

    def test_log_out(self):
        """
        Тест проверяет, что при нажатии кнопки "Выход", происходит выход из учетной записи пользователя.
        :return:
        """
        self.test_log_in_with_correct_data()
        self.find(ButtonForAuthorization.BUTTON_PROFILE).click()
        time.sleep(3)
        # TODO result = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(expected_conditions.element_located_to_be_selected(paths.LOGOUT)).click()
        self.find(ButtonForAuthorization.BUTTON_LOGOUT).click()
        result = self.expected_conditions_element(ButtonForAuthorization.BUTTON_LOGIN, "clickable").text
        assert result == "Войти"
    def test_log_in_with_incorrect_login(self):
        """
        Тест проверяет, что при вводе неправильного логина, вход в учетную запись пользователя не осуществляется.
        :return:
        """
        self.expected_conditions_element(ButtonForAuthorization.BUTTON_LOGIN, "clickable").click()
        self.find_element_and_send_text(
            ButtonForInputData.INPUT_EMAIL, constants.INVALID_NUMBER
        )
        self.find_element_and_send_text(
            ButtonForInputData.INPUT_PASSWORD, constants.PASSWORD_FOR_LOGIN
        )
        self.find(ButtonForAuthorization.BUTTON_LOGIN_AFTER_INPUT_DATA).click()
        result = self.expected_conditions_element(
            Check.ERROR_LOGIN_WITH_INVALID_DATA, "located"
        ).text
        assert result == "Error"
    def test_log_in_with_incorrect_password(self):
        """
        Тест проверяет, что при вводе неправильного пароля, вход в учетную запись пользователя не происходит.
        :return:
        """
        self.expected_conditions_element(ButtonForAuthorization.BUTTON_LOGIN, "clickable").click()
        self.find_element_and_send_text(ButtonForInputData.INPUT_EMAIL, constants.NUMBER_FOR_LOGIN)
        self.find_element_and_send_text(
            ButtonForInputData.INPUT_PASSWORD, constants.INVALID_PASSWORD
        )
        self.find(ButtonForAuthorization.BUTTON_LOGIN_AFTER_INPUT_DATA).click()
        result = self.expected_conditions_element(
            Check.ERROR_LOGIN_WITH_INVALID_DATA, "located"
        ).text
        assert result == "Error"


