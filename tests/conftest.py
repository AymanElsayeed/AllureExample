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
                # print(f"tags: {tags}", file=sys.stderr)
                allure.dynamic.tag(*tags)
            if severity:
                allure.dynamic.severity(severity)
            if title:
                allure.dynamic.title(title)
            if story:
                allure.dynamic.story(story)
            if feature:
                allure.dynamic.feature(feature)

    # if 'allure' in item.keywords:
        # modified_item = item.copy()
        # modified_item = Function(name=item.name, parent=item.parent, module=item.module, lineno=item)
        # modified_item.config = item.config
        # modified_item.module = item.module
        # modified_item.path = item.path
        # modified_item.lineno = item.lineno
        # modified_item.session = item.session
        # modified_item.keywords = {key: value for key, value in item.keywords.items() if key != 'allure'}
        # modified_item.keywords = {key: value for key, value in item.keywords.items() if key != 'allure'}
        # item.__dict__.update(modified_item.__dict__)
        # item.keywords.pop('allure', None)

    # for mark in item.iter_markers(name="allure"):
    #     # mark.kwargs = {}
    #     print(f"mark: {mark}", file=sys.stderr)
    #     mark = Mark(name="", args=(), kwargs={})

    # remove allure marker form item
    print(f"\n item dir: {dir(item)}", file=sys.stderr)
    print(f"\n item type: {type(item)}", file=sys.stderr)
    # pdb.set_trace()

    print(f"\n item.keywords type: {type(item.keywords)}", file=sys.stderr)
    print(f"\n item.keywords dir: {dir(item.keywords)}", file=sys.stderr)
    print(f"\n item.keywords: {[type(k) for k in item.keywords.items()]}", file=sys.stderr)
    print(f"\n item.keywords: {[(k,item.keywords[k]) for k in item.keywords.keys()]}", file=sys.stderr)
    # node_key_words = NodeKeywords((k, item.keywords[k]) for k in item.keywords.keys())
    # item.keywords.update({"allure": False})
    # item.keywords.update({"allure": Mark(name="", args=(), kwargs={})})
    # print(f"\n item.keywords: {[(k,item.keywords[k]) for k in item.keywords.keys()]}", file=sys.stderr)
    _ = [mark.kwargs.pop("owner", None) for mark in item.iter_markers(name='allure')]
    _ = [mark.kwargs.pop("severity", None) for mark in item.iter_markers(name='allure')]
    _ = [mark.kwargs.pop("allure", None) for mark in item.iter_markers(name='allure')]
    _ = [mark.kwargs.pop("allure", None) for mark in item.iter_markers()]
    pdb.set_trace()
    temp = [k for k in item.keywords if k != 'allure']
    item.keywords = NodeKeywords(temp)
    # _ = [mark.kwargs.pop("owner") for mark in item.parent.iter_markers(name='allure')]
    # print(f"zz: {[mark.kwargs for mark in item.iter_markers(name='allure')]}", file=sys.stderr)
    # print(f"zz: {[mark.kwargs.pop('owner') for mark in item.iter_markers(name='allure')]}", file=sys.stderr)
    return item

    # print(f"name: {item.name}", file=sys.stderr)
    # print(f"config: {dir(item.config)}", file=sys.stderr)
    # print(f"config.args: {item.config.args}", file=sys.stderr)
    # print(item.keywords, file=sys.stderr)
    # print(f"item: {item}", file=sys.stderr)
    # print(f"type item: {type(item)}", file=sys.stderr)
    # print(f"dir item: {dir(item)}", file=sys.stderr)
    #
    # print(f"type item.keywords: {type(item.keywords)}", file=sys.stderr)
    # print(f"item.keywords: {item.keywords}", file=sys.stderr)
    # print(f"dir item.keywords: {dir(item.keywords)}", file=sys.stderr)
    # print(f"item.keywords.items: {item.keywords.values}", file=sys.stderr)
    # item.keywords.pop("allure", None)
    # item.remove_marker("allure")
    # item.keywords.clear()
    # marks = []
    # for mark in item.iter_markers():
    #     # print(f"mark : {mark}", file=sys.stderr)
    #     kwargs2 = mark.kwargs
    #     if kwargs:
    #         # kwargs2 = kwargs2[0]
    #         marks.append(Mark(name="", args=(), kwargs={}))

    # update item marks
    # item.keywords._markers = marks
    # print(f"item.keywords: {next(item.iter_markers())}", file=sys.stderr)
    # print(f"item.keywords: {next(item.iter_markers())}", file=sys.stderr)
