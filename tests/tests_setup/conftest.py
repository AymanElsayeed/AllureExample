
import pytest

data = dict()


@pytest.fixture(scope="session", autouse=True, name="data")
def data_fixture():
    """
    Data fixture
    :return: data dict
    :rtype: dict
    """
    yield data
