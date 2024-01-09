import pytest
import allure


@pytest.mark.xdist_group(name="setup")
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

        if method.__name__ == "test_setup_failed_1":
            self.valid = False

        if method.__name__.startswith("test_setup_failed"):
            # get number from the test parm
            for mark in method.pytestmark:
                if mark.name == "parametrize":

                    if mark.args[0] != "number":
                        self.valid = True

                    for number in mark.args[1]:
                        if number % 2 == 0:
                            self.valid = False

    @classmethod
    def setup_class(cls, **kwargs):
        """
        setup any state specific to the execution of the given class (which usually contains tests).
        :return: None
        """
        allure.attach(f"Ayman Class setup method ", name="setup method",
                      attachment_type=allure.attachment_type.TEXT)

    def test_setup_failed_1(self):
        """
        test setup failed
        :return: None
        """
        assert self.valid is False

    @pytest.mark.parametrize("number", [20])
    def test_setup_failed_2(self, number):
        """
        test setup failed
        :return: None
        """
        assert self.valid is False

    @pytest.mark.parametrize("a_number", [21, 20])
    def test_setup_failed_3(self, a_number):
        """
        test setup failed
        :return: None
        """
        assert self.valid
