import pytest


@pytest.mark.allure(owner="ayman", severity="critical")
class TestReport8:

    def test_example1_report8(self):
        assert 1 + 1 == 2

    def test_example2_report8(self, customer):
        assert customer == "customer"
