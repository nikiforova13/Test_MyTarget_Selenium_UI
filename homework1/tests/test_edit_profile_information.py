
class TestEditProfileInformation(BaseCase):
    def test_edit_profile_information(self):
        """
        Тест проверяет, что при редактировании контактной информации пользователя, изменения применяются.
        :return:
        """
        DATA = self.generate_data()
        self.test_log_in_with_correct_data()
        self.find(ButtonForNavigatingPages.BUTTON_PROFILE).click()
        self.find_element_and_send_text(ButtonForInputData.INPUT_NAME, DATA.get("name"))
        self.find(ButtonForSavingChanges.SAVE_CHANGE).click()
        self.driver.refresh()
        result = self.expected_conditions_element(
            Check.CURRENT_USERNAME, "located"
        ).text
        assert result == (DATA.get("name")).upper()