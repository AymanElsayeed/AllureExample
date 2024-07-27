"""

Tests for the fixtures

"""
import pytest


class TestFixtures:
    var = 0

    @pytest.fixture(scope="function", name="numbers")
    def fixture_numbers(self, list_of_even_numbers) -> list:
        """
        This fixture returns a list of numbers (this is python docstring)
        :param list_of_even_numbers:
        :return: None
        """
        return list_of_even_numbers

    def test_even_numbers_list_len(self, list_of_even_numbers):
        """
        This test checks the length of the list of even numbers (this is python docstring)
        :param list_of_even_numbers:
        :return: None
        """
        print(f"list_of_even_numbers: {list_of_even_numbers}")
        assert len(list_of_even_numbers) == 4

    def test_odd_numbers_list_len(self, list_of_odd_numbers):
        """
        This test checks the length of the list of odd numbers (this is python docstring)
        :param list_of_odd_numbers:
        :return:
        """
        print(f"list_of_odd_numbers: {list_of_odd_numbers}")
        assert len(list_of_odd_numbers) == 5

    @pytest.fixture(scope="function", name="xx", params=[1, 2, 3, 4, 5, 6, 8, 10])
    def get_numbers(self, request):
        """
        This fixture returns a number (this is python docstring)
        :param request: request object
        :return: an even number
        :rtype: int
        """
        n = request.param
        if n % 2 == 0:
            return n
        else:
            # ignore odd numbers
            pytest.skip(f"skipping odd number {n}")

    def test_get_number(self, xx):
        """
        This test checks if the number is even (this is python docstring)
        :param xx: number
        :return: None
        """
        assert xx % 2 == 0
