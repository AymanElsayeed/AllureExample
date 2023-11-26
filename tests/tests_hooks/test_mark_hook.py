import pytest
from src.report2 import allure_hook


@pytest.mark.markhook
@pytest.mark.allure(owner="ayman", severity="critical", tag=["MarkHook"])
class TestMarkHook:
    def test_one(self):
        assert True

    @allure_hook(owner="Ayman.E", description="owner should be Ayman.E")
    def test_change_owner(self, customer):
        assert customer == "customer"

    def test_fixture_usage(self, customer):
        assert customer == "customer"

    @allure_hook(tags=["tag1", "tag2"], description="tag1, tag2 should be added")
    def test_add_tags(self):
        assert True

    @allure_hook(severity="blocker", description="severity should be blocker")
    def test_set_severity_blocker(self):
        assert True
