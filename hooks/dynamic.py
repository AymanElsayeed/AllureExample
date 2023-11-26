

from shared.allure_wrapper import allure_wrapper


def dynamic_decorator(**params):
    def decorator(cls):
        # Define any modifications or additions to the class using params
        class ModifiedTestClass(cls):
            @staticmethod
            def setup():
                allure_wrapper(**params)

        return ModifiedTestClass

    return decorator
