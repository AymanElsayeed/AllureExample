
import allure


def allure_wrapper(**params):
    """
    This is my decorator
    :param params: params to decorate
    :return: decorated function
    """

    severity = params.get("severity")
    owner = params.get("owner")
    tag = params.get("tag")
    title = params.get("title")
    story = params.get("story")
    feature = params.get("feature")
    description = params.get("description")

    if owner:
        allure.dynamic.label("owner", owner)
    if tag:
        allure.dynamic.tag(*tag)
    if severity:
        allure.dynamic.severity(severity)
    if title:
        allure.dynamic.title(title)
    if story:
        allure.dynamic.story(story)
    if feature:
        allure.dynamic.feature(feature)
    if description:
        allure.dynamic.description(description)
