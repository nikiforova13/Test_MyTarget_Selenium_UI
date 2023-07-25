from homework1.locators.paths import ButtonForAuthorization, Check
from homework1.base.base_case import BaseCase
import time
import pytest


@pytest.mark.ui
class TestLogOut(BaseCase):
    def test_log_out(self, authorization):
        """
        Тест проверяет, что при нажатии кнопки "Выход", происходит выход из учетной записи пользователя.
        :return:
        """
        self.expected_conditions_element(Check.MENU_AUDIENCES, "clickable")
        self.expected_conditions_element(
            ButtonForAuthorization.BUTTON_PROFILE, "clickable"
        ).click()
        # TODO result = WebDriverWait(self.driver, 10, poll_frequency=0.1).until(expected_conditions.element_located_to_be_selected(paths.LOGOUT)).click()
        time.sleep(4)
        self.find(ButtonForAuthorization.BUTTON_LOGOUT).click()
        result = self.expected_conditions_element(
            ButtonForAuthorization.BUTTON_LOGIN, "located"
        ).text
        assert result
