import pytest
import allure


def pytest_sessionstart(session):
    session.results = dict()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        # check if its failure
        if result.failed:
            item.session.results[item] = item.funcargs['param']
            item.add_marker(pytest.mark.xxaymanxx)
            # use allure to add extra data to the report
            allure.attach("ayman text of file go here", str(item.funcargs['param']), allure.attachment_type.TEXT)


def pytest_sessionfinish(session, exitstatus):
    print()
    print('run status code:', exitstatus)
    for item in session.results:
        print(f'Failed Tests: {item.name}, with params: {session.results[item]}')
