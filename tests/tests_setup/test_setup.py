
import pytest
import allure


@pytest.mark.setup
class TestSetUp:

    class_data = []

    @pytest.mark.parametrize("file_name", [2, 3, 4])
    def test_setup_1(self, file_name):
        print(f"test setup {file_name}")
        assert True

    @pytest.mark.parametrize("file_name", [22, 23, 24])
    def test_setup_2(self, file_name):
        print(f"test setup {file_name}")
        assert True

    @pytest.mark.parametrize("file_name", [32, 33, 34])
    def test_setup_3(self, file_name):
        print(f"test setup {file_name}")
        assert True

    def setup_method(self, method):
        """
        setup method.
        :return: None
        """
        self.class_data.append(method.__name__)
        print(f"setup method {method.__name__}")
        allure.attach(f"setup method {method.__name__}", name="setup method",
                      attachment_type=allure.attachment_type.TEXT)

    @classmethod
    def setup_class(cls, **kwargs):
        """
        setup any state specific to the execution of the given class (which usually contains tests).
        :return: None
        """
        allure.attach(f"Ayman Class setup method ", name="setup method",
                      attachment_type=allure.attachment_type.TEXT)
