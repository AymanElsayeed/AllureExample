"""

This file contains the fixtures that are used in the tests.
those fixtures are available for test_fixtures package only.

"""

import pytest
import allure


@pytest.fixture(scope="function", name="list_of_numbers")
def fixture_list_of_numbers() -> list:
    # allure description
    allure.dynamic.description("This fixture returns a list of numbers")
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


@pytest.fixture(scope="function", name="list_of_even_numbers")
def fixture_list_of_sub_numbers(list_of_numbers) -> list:
    # allure description
    allure.dynamic.description("This fixture returns a list of even numbers")
    return list(filter(lambda x: x % 2 == 0, list_of_numbers))


@pytest.fixture(scope="function", name="list_of_odd_numbers")
def fixture_list_of_odd_numbers(list_of_numbers) -> list:
    # allure description
    allure.dynamic.description("This fixture returns a list of odd numbers")
    return list(filter(lambda x: x % 2 != 0, list_of_numbers))
