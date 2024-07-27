import sys
from pyclbr import Function
import pdb
import allure
import pytest
from _pytest.mark import Mark
from _pytest.mark.structures import NodeKeywords
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


# def pytest_runtest_setup(item):
#     for mark in item.iter_markers(name="allure"):
#         kwargs = mark.kwargs
#         if kwargs:
#             # kwargs = kwargs[0]
#             # get owner from kwargs
#             severity = kwargs.get("severity")
#             # print(f"kwargs: {kwargs}")
#             owner = kwargs.get("owner")
#             tags = kwargs.get("tags")
#             title = kwargs.get("title")
#             story = kwargs.get("story")
#             feature = kwargs.get("feature")
#
#             if owner:
#                 allure.dynamic.label("owner", owner)
#             if tags:
#                 allure.dynamic.tag(*tags)
#             if severity:
#                 allure.dynamic.severity(severity)
#             if title:
#                 allure.dynamic.title(title)
#             if story:
#                 allure.dynamic.story(story)
#             if feature:
#                 allure.dynamic.feature(feature)
#
#     # remove allure marker form item
#     # pdb.set_trace()
#     _ = [mark.kwargs.pop("owner", None) for mark in item.iter_markers(name='allure')]
#     _ = [mark.kwargs.pop("severity", None) for mark in item.iter_markers(name='allure')]
#     _ = [mark.kwargs.pop("allure", None) for mark in item.iter_markers(name='allure')]
#     _ = [mark.kwargs.pop("allure", None) for mark in item.iter_markers()]
#     pdb.set_trace()
#     temp = [k for k in item.keywords if k != 'allure']
#     item.keywords = NodeKeywords(temp)
#     return item


# conftest.py

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
