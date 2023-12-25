import asyncio
import pytest
import allure
import pdb


@pytest.mark.asyncio
@pytest.mark.xdist_group(name="teardown")
@pytest.mark.teardown
class TestTearDown:
    class_data = {}

    def setup_method(self, method):
        """
        setup method.
        :return: None
        """
        # pdb.set_trace()

        parameters = [i.args[1] for i in method.pytestmark if i.args[0] == "file_name"]
        if parameters:
            self.class_data[method.__name__] = parameters[0]
        else:
            self.class_data[method.__name__] = [0]

        print(f"setup method {method.__name__}")
        allure.attach(f"setup method {method.__name__}", name="setup method",
                      attachment_type=allure.attachment_type.TEXT)

    @pytest.mark.parametrize("file_name", [1, 2, 3])
    async def test_teardown_1(self, file_name):
        print(f"test teardown {file_name}")
        await asyncio.sleep(file_name)
        assert True

    @pytest.mark.parametrize("file_name", [4, 5, 6])
    async def test_teardown_2(self, file_name):
        print(f"test teardown {file_name}")
        await asyncio.sleep(file_name)
        assert True

    @pytest.mark.parametrize("file_name", [7, 8, 9])
    async def test_teardown_3(self, file_name):
        print(f"test teardown {file_name}")
        await asyncio.sleep(file_name)
        assert True

    @pytest.mark.run("last")
    def test_running_time(self):
        pdb.set_trace()
        print(f"running time: {self.class_data}")
        assert sum(map(sum, self.class_data.values())) == 45

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
