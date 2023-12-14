"""

Example tests for package one module one

"""

import sys
import datetime
import pytest
import pdb


@pytest.mark.one
@pytest.mark.xdist_group(name="group1")
class TestsOne:
    """
    All tests will run on the same worker if you pass '--dist loadgroup'
    """

    shared_items = []
    failed_tests = []

    # @pytest.hookimpl(tryfirst=True)
    # def pytest_runtest_protocol(self, item, nextitem):
    #     result = nextitem._result  # Access the result object
    #
    #     # Check if the test has failed
    #     if result and result.when == "call" and result.failed:
    #         test_info = {
    #             "name": item.name,
    #             "location": item.location,
    #             "parameters": item.keywords.get("fixturemanager").params
    #         }
    #         self.failed_tests.append(test_info)
    #         print(f"Failed test: {test_info}", file=sys.stderr)

    def test_one_example_1(self):
        """
        Example one
        :return: None
        """
        print(datetime.datetime.now(), file=sys.stderr)
        self.shared_items.append((1, datetime.datetime.now()))
        assert True

    @pytest.mark.parametrize("param", [2, 3, 4])
    def test_one_example_2(self, param):
        """
        Example two
        :return: None
        """
        print(datetime.datetime.now(), file=sys.stderr)
        self.shared_items.append((2, datetime.datetime.now()))

        assert param % 2 == 0

    @pytest.mark.run("last")
    def test_one_last_example(self,):
        """
        Last Example
        :return:
        """
        self.shared_items.append((3, datetime.datetime.now()))
        assert True

    @classmethod
    def teardown_class(cls):
        """
        teardown any state that was previously setup with a call to setup_class.
        """
        print(f"Class shared items: {cls.failed_tests}", file=sys.stderr)

    # def teardown_method(self, method):
    #     """
    #     teardown method, teardown any state that was previously setup with a setup_method call.
    #     :return: None
    #     """
    #     # get method results
    #     pdb.set_trace()
