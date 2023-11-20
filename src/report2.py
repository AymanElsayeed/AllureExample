import functools
import allure


def allure_hook(**params):

    severity = params.get("severity")
    owner = params.get("owner")
    tag = params.get("tag")
    title = params.get("title")
    story = params.get("story")
    feature = params.get("feature")

    def decorate(function):
        """
        This is my decorator
        :param function: function to decorate
        :return: decorated function
        """

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
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
            result = function(*args, **kwargs)
            return result

        return wrapper

    return decorate
