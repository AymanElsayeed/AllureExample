import functools
from shared.allure_wrapper import allure_wrapper


def allure_hook(**params):
    def decorate(function):
        """
        This is my decorator
        :param function: function to decorate
        :return: decorated function
        """

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            allure_wrapper(**params)
            result = function(*args, **kwargs)
            return result

        return wrapper

    return decorate
