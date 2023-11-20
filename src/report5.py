import allure


def my_custom_decorator(cls):
    # Define any modifications or additions to the class here
    class ModifiedTestClass(cls):
        def setup(self):
            # super(ModifiedTestClass, self).setup()
            print("Custom setup for the test class")
            allure.dynamic.tag("BBB")

    return ModifiedTestClass


def my_custom_decorator2(**params):
    severity = params.get("severity")
    owner = params.get("owner")
    tag = params.get("tag")
    title = params.get("title")
    story = params.get("story")
    feature = params.get("feature")

    def decorator(cls):
        # Define any modifications or additions to the class using params
        class ModifiedTestClass(cls):
            def setup(self):
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

        return ModifiedTestClass

    return decorator


def my_custom_decorator3(**params):
    severity = params.get("severity")
    owner = params.get("owner")
    tag = params.get("tag")
    title = params.get("title")
    story = params.get("story")
    feature = params.get("feature")

    def decorator(cls):
        class ModifiedTestClass(cls):
            def __call__(self, *args, **kwargs):
                # wraps = self.func.__wrapped__
                # parametrized_decorator(tag="PR", owner="Eman", severity="critical")
                if owner:
                    print(f"owner: {owner}")
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
                return self.func(*args, **kwargs)

        # return wraps(*args, **kwargs)
        # return decorator.decorator(parametrized_decorator, self.func)
        # pass  # Define any common modifications to the class here

        # Iterate over the attributes of the class
        # for name, value in cls.__dict__.items():
        #     # Check if the attribute is a callable (method)
        #     if callable(value) and name.startswith('test_'):
        #         # Apply the decorator to each test method
        #         setattr(ModifiedTestClass, name,
        #                 apply_decorators(my_custom_method_decorator(**params))(value),
        #                 # apply_decorators(decorate_method3(**params))(value)
        #                 # decorate_method3(value, **params)
        #                 )

        return ModifiedTestClass

    return decorator


def my_custom_method_decorator(**params):
    def decorator(original_method):
        # Define any modifications to the method here
        def wrapper(*args, **kwargs):
            # print(f"Decorator before calling method {original_method.__name__} with params: {param1}, {param2}")
            result = original_method(*args, **kwargs)
            return result

        return wrapper

    return decorator


def apply_decorators(*decorators):
    def decorator(original_method):
        for dec in decorators:
            original_method = dec(original_method)
        return original_method

    return decorator


def decorate_method3(method, **params):
    # Define any modifications to the method here
    severity = params.get("severity")
    owner = params.get("owner")
    tag = params.get("tag")
    title = params.get("title")
    story = params.get("story")
    feature = params.get("feature")

    def wrapper(*args, **kwargs):
        # print(f"Decorator before calling method {method.__name__} with params: {param1}, {param2}")
        result = method(*args, **kwargs)
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
            return result

    return wrapper
