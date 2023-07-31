import pytest

from homework1.base.base_case import BaseCase
from homework1.consts import constants
from homework1.locators.paths import FieldsForInputData, Check, ButtonForAuthorization


@pytest.mark.ui
class TestAuthorization(BaseCase):
    def test_log_in_with_correct_data(self):
        """
        Тест проверяет, что при вводе корректных данных осуществляется вход в учетную запись пользователя.
        :return:
        """
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
        result = self.expected_conditions_element(
            ButtonForAuthorization.BUTTON_LOGIN, "title", "Кампании"
        )
        assert result == True

    def test_log_in_with_incorrect_login(self):
        """
        Тест проверяет, что при вводе невалидного логина, вход в учетную запись пользователя не осуществляется.
        :return:
        """
        self.expected_conditions_element(
            ButtonForAuthorization.BUTTON_LOGIN, "clickable"
        )
        self.find_element_and_send_text(
            FieldsForInputData.INPUT_EMAIL_FIELD, constants.INVALID_NUMBER
        )
        self.find_element_and_send_text(
            FieldsForInputData.INPUT_PASSWORD_FIELD, constants.PASSWORD_FOR_LOGIN
        )
        self.find(ButtonForAuthorization.BUTTON_LOGIN_AFTER_INPUT_DATA).click()
        result = self.expected_conditions_element(
            Check.ERROR_LOGIN_WITH_INVALID_DATA, "located"
        )
        assert result

    def test_log_in_with_incorrect_password(self):
        """
        Тест проверяет, что при вводе неправильного пароля, вход в учетную запись пользователя не происходит.
        :return:
        """
        self.expected_conditions_element(
            ButtonForAuthorization.BUTTON_LOGIN, "clickable"
        )
        self.find_element_and_send_text(
            FieldsForInputData.INPUT_EMAIL_FIELD, constants.NUMBER_FOR_LOGIN
        )
        self.find_element_and_send_text(
            FieldsForInputData.INPUT_PASSWORD_FIELD, constants.INVALID_PASSWORD
        )
        self.find(ButtonForAuthorization.BUTTON_LOGIN_AFTER_INPUT_DATA).click()
        result = self.expected_conditions_element(
            Check.ERROR_LOGIN_WITH_INVALID_DATA, "located"
        )
        assert result
