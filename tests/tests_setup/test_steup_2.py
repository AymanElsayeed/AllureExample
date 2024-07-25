import pytest

Collection = {i: i for i in range(0, 100)}


class TestSetup2:
    counter = 1

    def setup_method(self, method):
        # remove all odd numbers from the collection
        # for i in range(1, 100, 2):
        Collection.pop(self.counter)
        print(f"remove {self.counter} from the collection")
        self.counter += 2

    @pytest.mark.parametrize("number", [i for i in range(1, 100, 1)])
    def test_setup_1(self, number):
        assert Collection.get(number + 1) % 2 == 0
