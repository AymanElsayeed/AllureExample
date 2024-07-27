"""

This file contains the fixtures that are used in the tests.
those fixtures are available for test_fixtures package only.

"""

import pytest


@pytest.fixture(scope="function", name="list_of_numbers")
def fixture_list_of_numbers() -> list:
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


@pytest.fixture(scope="function", name="list_of_even_numbers")
def fixture_list_of_sub_numbers(list_of_numbers) -> list:
    # return only the even numbers
    return list(filter(lambda x: x % 2 == 0, list_of_numbers))


@pytest.fixture(scope="function", name="list_of_odd_numbers")
def fixture_list_of_odd_numbers(list_of_numbers) -> list:
    # return only the odd numbers
    return list(filter(lambda x: x % 2 != 0, list_of_numbers))
