"""

Pr test module for pull request testing purposes.

"""

import pytest
from src.report2 import allure_hook
from src.report5 import my_custom_decorator3

__all__ = ["TestReport3"]


@pytest.mark.xxx
# @my_custom_decorator3(owner="Report3")
class TestReport3:

    @allure_hook(tag=["Report3"], severity="critical")
    def test_report3_1(self):
        """
        Example on pr, how to write test for syn-engine
        :return: None
        """
        assert True

    @allure_hook(tag=["Report3"], severity="blocker")
    def test_report3_2(self):
        assert True

    @allure_hook(tag=["Report3"], severity="trivial")
    def test_report3_3(self):
        assert True

    def test_change_owner(self, customer):
        assert customer == "customer"
