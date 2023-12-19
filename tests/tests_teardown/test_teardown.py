import pytest
import allure


@pytest.mark.xdist_group(name="teardown")
@pytest.mark.teardown
class TestTearDown:

    @pytest.mark.parametrize("file_name", [2, 3, 4])
    def test_teardown_1(self, file_name):
        print(f"test teardown {file_name}")
        assert True

    @pytest.mark.parametrize("file_name", [22, 23, 24])
    def test_teardown_2(self, file_name):
        print(f"test teardown {file_name}")
        assert True

    @pytest.mark.parametrize("file_name", [32, 33, 34])
    def test_teardown_3(self, file_name):
        print(f"test teardown {file_name}")
        assert True

    @staticmethod
    def teardown_method(method):
        """
        teardown method.
        :return: None
        """
        print(f"teardown method {method.__name__}")
        allure.attach(f"teardown method {method.__name__}", name="teardown method",
                      attachment_type=allure.attachment_type.TEXT)

    @classmethod
    def teardown_class(cls, **kwargs):
        """
        teardown class, teardown any state that was previously setup with a call to setup_class.
        :return: None
        """
        allure.attach(f"Ayman Class teardown method ", name="teardown method",
                      attachment_type=allure.attachment_type.TEXT)
