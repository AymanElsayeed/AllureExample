"""

Example tests for package one module one

"""

import sys
import datetime
import pytest


@pytest.mark.HookResults
class TestsHookResults:

    def test_hook_results_example_1(self):
        """
        Example one
        :return: None
        """
        print(datetime.datetime.now(), file=sys.stderr)
        assert True

    @pytest.mark.parametrize("param", [2, 3, 4])
    def test_hook_results_example_2(self, param):
        """
        Example two
        :return: None
        """
        print(datetime.datetime.now(), file=sys.stderr)
        assert param % 2 == 0
