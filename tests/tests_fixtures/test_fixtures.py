import pytest


class TestFixtures:
    var = 0

    @pytest.fixture(scope="function", name="numbers")
    def fixture_numbers(self, list_of_even_numbers) -> list:
        return list_of_even_numbers

    def test_even_numbers_list_len(self, list_of_even_numbers):
        print(f"list_of_even_numbers: {list_of_even_numbers}")
        assert len(list_of_even_numbers) == 4

    def test_odd_numbers_list_len(self, list_of_odd_numbers):
        print(f"list_of_odd_numbers: {list_of_odd_numbers}")
        assert len(list_of_odd_numbers) == 5

    @pytest.fixture(scope="function", name="xx", params=[1, 2, 3, 4, 5, 6, 8, 10])
    def get_numbers(self, request):
        n = request.param
        if n % 2 == 0:
            return n
        else:
            # ignore odd numbers
            pytest.skip(f"skipping odd number {n}")

    def test_get_number(self, xx):
        assert xx % 2 == 0
