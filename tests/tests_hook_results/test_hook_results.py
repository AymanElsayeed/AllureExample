"""

Example tests for package one module one

"""

import sys
import datetime
import pytest


@pytest.mark.HookResults
class TestsHookResults:

    @pytest.mark.xfail(reason="This test is not implemented yet")
    def test_hook_results_example_1(self):
        """
        Example one
        :return: None
        """
        print(datetime.datetime.now(), file=sys.stderr)
        assert False

    @pytest.mark.parametrize("param", [2, 3, 4])
    def test_hook_results_example_2(self, param):
        """
        Example two
        :return: None
        """
        print(datetime.datetime.now(), file=sys.stderr)
        assert param % 2 == 0

    @pytest.mark.parametrize("param", [2, 6, 4])
    def test_hook_results_example_3(self, param):
        """
        Example two
        :return: None
        """
        print(datetime.datetime.now(), file=sys.stderr)
        pytest.xfail(reason="This test is not implemented yet")
