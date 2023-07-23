import time

import pytest

from homework1.base.base_case import BaseCase
from homework1.consts import constants
from homework1.locators import paths


class TestAuthorization(BaseCase):
    def test_log_in_with_correct_data(self):
        """
        Тест проверяет правильность входа в учетную запись пользователя при вводе корректных данных.
        :return:
        """
        self.expected_conditions_element(paths.BUTTON_LOGIN, "clickable").click()
        self.find_element_and_send_text(paths.INPUT_EMAIL, constants.NUMBER_FOR_LOGIN)
        self.find_element_and_send_text(
            paths.INPUT_PASSWORD, constants.PASSWORD_FOR_LOGIN
        )
        self.find(paths.BUTTON_LOGIN_AFTER_INPUT_DATA).click()
        result = self.expected_conditions_element(
            paths.BUTTON_LOGIN, "title", "Кампании"
        )
        assert result == True, "Авторизация прошла безуспешно"

    def test_log_out(self):
        """
        Тест проверяет правильность выхода из учетной записи.
        :return:
        """
        self.test_log_in_with_correct_data()
        self.find(paths.BUTTON_LOGOUT).click()
        time.sleep(3)
        # TODO result = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(expected_conditions.element_located_to_be_selected(paths.LOGOUT)).click()
        self.find(paths.LOGOUT).click()
        result = self.expected_conditions_element(paths.BUTTON_LOGIN, "clickable").text
        assert result == "Войти", "Выход из аккаунта прошел безуспешно"

    def test_log_in_with_incorrect_login(self):
        """
        Тест проверяет процесс входа в учетную запись при вводе неправильного логина.
        :return:
        """
        self.expected_conditions_element(paths.BUTTON_LOGIN, "clickable").click()
        self.find_element_and_send_text(
            paths.INPUT_EMAIL, constants.NUMBER_FOR_INCORRECT_LOGIN
        )
        self.find_element_and_send_text(
            paths.INPUT_PASSWORD, constants.PASSWORD_FOR_LOGIN
        )
        self.find(paths.BUTTON_LOGIN_AFTER_INPUT_DATA).click()
        result = self.expected_conditions_element(
            paths.ERROR_PASSWORD_OR_LOGIN, "located"
        ).text
        assert result == "Error"

    def test_log_in_with_incorrect_password(self):
        """
        Тест проверяет процесс входа в учетную запись при вводе неправильного пароля.
        :return:
        """
        self.expected_conditions_element(paths.BUTTON_LOGIN, "clickable").click()
        self.find_element_and_send_text(paths.INPUT_EMAIL, constants.NUMBER_FOR_LOGIN)
        self.find_element_and_send_text(
            paths.INPUT_PASSWORD, constants.PASSWORD_FOR_INCORRECT_LOGIN
        )
        self.find(paths.BUTTON_LOGIN_AFTER_INPUT_DATA).click()
        result = self.expected_conditions_element(
            paths.ERROR_PASSWORD_OR_LOGIN, "located"
        ).text
        assert result == "Error"

    def test_edit_profile_information(self):
        """
        Тест проверяет корректность редактирования контактной информации пользователя.
        :return:
        """
        DATA = self.generate_data()
        self.test_log_in_with_correct_data()
        self.find(paths.BUTTON_PROFILE).click()
        self.find_element_and_send_text(paths.INPUT_NAME, DATA.get("name"))
        self.find(paths.SAVE_CHANGE).click()
        self.driver.refresh()
        result = self.expected_conditions_element(
            paths.GET_CURRENT_NAME, "located"
        ).text
        assert result == (DATA.get("name")).upper()

    @pytest.mark.parametrize(
        "path,check",
        zip(
            [
                paths.BUTTON_AUDIENCES,
                paths.BUTTON_BALANCE,
                paths.BUTTON_STATISTICS,
                paths.BUTTON_PROFILE,
                paths.BUTTON_TOOLS,
            ],
            [
                paths.CHECK_AUDIENCES,
                paths.CHECK_BALANCE,
                paths.CHECK_STATISTICS,
                paths.CHECK_PROFILE,
                paths.CHECK_TOOLS,
            ],
        ),
        ids=[
            "check button audiences",
            "check button balanca",
            "check button statistics",
            "check button profile",
            "check button tools",
        ],
    )
    def test_go_to_portal_pages(self, path, check):
        """
        Тест переходит по страницам портала и проверяет, что переход на страницу осуществлен.
        :param path:
        :param check:
        :return:
        """
        self.test_log_in_with_correct_data()
        self.find(path).click()
        result = self.expected_conditions_element(check, "located")
        assert result
