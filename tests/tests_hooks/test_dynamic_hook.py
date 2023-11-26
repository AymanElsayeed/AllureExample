"""

Pr test module for pull request testing purposes.

"""

import pytest
from src.report2 import allure_hook
from hooks.dynamic import dynamic_decorator


@pytest.mark.hook
@dynamic_decorator(owner="ayman", tag=["Hook"])
class TestDynamicHook:

    @allure_hook(severity="critical")
    def test_set_severity_critical(self):
        """
        Example on pr, how to write test for syn-engine
        :return: None
        """
        assert True

    @allure_hook(severity="blocker")
    def test_test_set_severity_blocker(self):
        assert True

    @allure_hook(severity="trivial")
    def test_test_set_severity_trivial(self):
        assert True

    def test_fixture_usage(self, customer):
        assert customer == "customer"

    @allure_hook(owner="Ayman.E")
    def test_change_owner(self):
        assert True

    @allure_hook(tags=["tag1", "tag2"])
    def test_add_tags(self):
        assert True
