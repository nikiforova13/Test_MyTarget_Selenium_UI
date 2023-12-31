from homework1.locators.paths import ButtonForNavigatingPages, Check
import pytest
from homework1.base.base_case import BaseCase


@pytest.mark.ui
class TestsPortalPages(BaseCase):
    @pytest.mark.parametrize(
        "path,check",
        zip(
            [
                ButtonForNavigatingPages.BUTTON_AUDIENCES,
                ButtonForNavigatingPages.BUTTON_BALANCE,
                ButtonForNavigatingPages.BUTTON_STATISTICS,
                ButtonForNavigatingPages.BUTTON_PROFILE,
                ButtonForNavigatingPages.BUTTON_TOOLS,
            ],
            [
                Check.PAGE_AUDIENCES,
                Check.PAGE_BALANCE,
                Check.PAGE_STATISTICS,
                Check.PAGE_PROFILE,
                Check.PAGE_TOOLS,
            ],
        ),
        ids=[
            "checking the transition to the audiences page",
            "checking the transition to the balanca page",
            "checking the transition to the statistics page",
            "checking the transition to the profile page",
            "checking the transition to the tools page",
        ],
    )
    def test_go_to_portal_pages(self, path, check, authorization):
        """
        Тест переходит по страницам портала и проверяет, что переход на соответствующую страницу осуществлен.
        :param path:
        :param check:
        :return:
        """
        self.expected_conditions_element(path, "clickable")
        result = self.expected_conditions_element(check, "located")
        assert result
