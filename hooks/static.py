
import allure


def static_decorator(cls):
    # Define any modifications or additions to the class here
    class ModifiedTestClass(cls):
        @staticmethod
        def setup(self):
            # super(ModifiedTestClass, self).setup()
            allure.dynamic.tag("BBB")

    return ModifiedTestClass
