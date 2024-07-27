"""

This file contains all the hooks and fixtures that are used in the tests.

"""

import pytest
from pytest_metadata.plugin import metadata_key


def pytest_sessionstart(session):
    """
    called after the ``Session`` object has been created and before performing collection
    and entering the run test loop.
    :param _pytest.main.Session session: the pytest session object
    """
    session.collection = {"ayman": "ayman"}


@pytest.fixture(scope="session", autouse=True, name="customer")
def customer_fixture():
    return "customer"


def pytest_runtest_protocol(item, nextitem):
    # pdb.set_trace()
    args = item.get_closest_marker("parametrize")
    if args is not None:
        name, values = args.args
        if name == "param":
            # Access the parameters without running the test
            param_value = values[0]
            print(f"Test {item.name} has parameter: {param_value}")
            # item.add_report_section("failed", "File not defined in collection")

    # add mark to skip the test
    # item.add_marker(pytest.mark.skip(reason="skipping test"))


def pytest_configure(config):
    config.stash[metadata_key]["foo"] = "bar"


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config.stash[metadata_key]["foo"] = "bar"


def pytest_html_report_title(report):
    report.title = "My very own title! 88"
