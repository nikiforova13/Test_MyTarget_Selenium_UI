from homework1.locators.paths import (
    ButtonForNavigatingPages,
    ButtonForSavingChanges,
    Check,
    FieldsForInputData,
)
from homework1.base.base_case import BaseCase
import pytest
from homework1.helpers.utils import generate_data

@pytest.mark.ui
class TestEditProfileInformation(BaseCase):
    def test_edit_profile_information(self, authorization):
        """
        Тест проверяет, что при редактировании контактной информации пользователя, изменения применяются.
        :return:
        """
        DATA = self.generate_data()
        self.expected_conditions_element(
            ButtonForNavigatingPages.BUTTON_PROFILE, "clickable"
        )
        self.find_element_and_send_text(FieldsForInputData.INPUT_NAME_FIELD, DATA.get("name"))
        self.find(ButtonForSavingChanges.SAVE_CHANGE).click()
        self.driver.refresh()
        result = self.expected_conditions_element(
            Check.CURRENT_USERNAME, "located"
        ).text
        assert result == (DATA.get("name")).upper()
