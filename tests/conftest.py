
import pytest


@pytest.fixture(scope="session", autouse=True, name="customer")
def customer_fixture():
    return "customer"
