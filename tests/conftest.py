import sys
from pyclbr import Function
import pdb
import allure
import pytest
from _pytest.mark import Mark
from _pytest.mark.structures import NodeKeywords


@pytest.fixture(scope="session", autouse=True, name="customer")
def customer_fixture():
    return "customer"


# def pytest_configure(config):
#     # register an additional marker
#     config.addinivalue_line(
#         "markers", "allure(owner): mark test to run only on named environment"
#     )


def pytest_runtest_setup(item):
    # kwargs = [mark.kwargs for mark in item.iter_markers(name="allure")]
    for mark in item.iter_markers(name="allure"):
        kwargs = mark.kwargs
        if kwargs:
            # kwargs = kwargs[0]
            # get owner from kwargs
            severity = kwargs.get("severity")
            # print(f"kwargs: {kwargs}")
            owner = kwargs.get("owner")
            tags = kwargs.get("tags")
            title = kwargs.get("title")
            story = kwargs.get("story")
            feature = kwargs.get("feature")

            if owner:
                allure.dynamic.label("owner", owner)
            if tags:
                allure.dynamic.tag(*tags)
            if severity:
                allure.dynamic.severity(severity)
            if title:
                allure.dynamic.title(title)
            if story:
                allure.dynamic.story(story)
            if feature:
                allure.dynamic.feature(feature)

    # remove allure marker form item
    print(f"\n item dir: {dir(item)}", file=sys.stderr)
    print(f"\n item type: {type(item)}", file=sys.stderr)
    # pdb.set_trace()

    print(f"\n item.keywords type: {type(item.keywords)}", file=sys.stderr)
    print(f"\n item.keywords dir: {dir(item.keywords)}", file=sys.stderr)
    print(f"\n item.keywords: {[type(k) for k in item.keywords.items()]}", file=sys.stderr)
    print(f"\n item.keywords: {[(k,item.keywords[k]) for k in item.keywords.keys()]}", file=sys.stderr)
    _ = [mark.kwargs.pop("owner", None) for mark in item.iter_markers(name='allure')]
    _ = [mark.kwargs.pop("severity", None) for mark in item.iter_markers(name='allure')]
    _ = [mark.kwargs.pop("allure", None) for mark in item.iter_markers(name='allure')]
    _ = [mark.kwargs.pop("allure", None) for mark in item.iter_markers()]
    pdb.set_trace()
    temp = [k for k in item.keywords if k != 'allure']
    item.keywords = NodeKeywords(temp)
    return item

