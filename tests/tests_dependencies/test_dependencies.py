"""

This test file is used to test the order of execution of tests

"""

import pytest
import allure


@pytest.mark.dependencies
class TestDependencies:

    n_executed = 0

    @pytest.mark.order(0)
    def test_dependencies_1(self):
        allure.description("""this test should run first """)
        print(f"test run last 1")
        TestDependencies.n_executed += 1
        assert TestDependencies.n_executed == 1

    @pytest.mark.order(1)
    def test_dependencies_2(self):
        allure.description(""" this test should run second """)
        print(f"test dependencies 2")
        TestDependencies.n_executed += 1
        assert TestDependencies.n_executed == 2

    @pytest.mark.order(2)
    def test_dependencies_3(self):
        allure.description(""" this test should run third """)
        print(f"test dependencies 3")
        TestDependencies.n_executed += 1
        assert TestDependencies.n_executed == 3

    @pytest.mark.order(3)
    def test_dependencies_4(self):
        allure.description(""" this test should run last 4 """)
        print(f"test run last 4")
        TestDependencies.n_executed += 1

        assert TestDependencies.n_executed == 4

    @pytest.mark.order(after="test_dependencies_3")
    def test_dependencies_5(self):
        allure.description(""" this test should run after test_dependencies_3 """)
        print(f"test dependencies 5")
        TestDependencies.n_executed += 1
        assert TestDependencies.n_executed == 5

    @pytest.mark.order("last")
    def test_dependencies_last(self):
        allure.description(""" this test should run last """)
        print(f"test dependencies 6")
        TestDependencies.n_executed += 1
        assert TestDependencies.n_executed == 6
