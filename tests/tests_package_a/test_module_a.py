"""

Pr test module for pull request testing purposes.

"""

import pytest
from src.report2 import allure_hook

__all__ = ["TestPr"]


@pytest.mark.a1
class TestPr:
    """
    Pull request test class
    """

    @allure_hook(tag=["PR"], owner="Ayman.E", severity="critical")
    def test_example_pr(self):
        """
        Example on pr, how to write test for syn-engine
        :return: None
        """
        assert True

    @allure_hook(tag=[1, 2], owner="Ayman.E", severity="blocker")
    def test_2(self):
        assert True

    @allure_hook(tag=["custom"], owner="Iman", severity="trivial", feature="Example")
    def test_customer(self, customer):
        assert customer == "customer"
