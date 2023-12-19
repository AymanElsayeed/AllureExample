import sys
import pdb
import pytest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == 'call':
        # pdb.set_trace()
        args = item.get_closest_marker("parametrize")
        if args is not None:
            name, values = args.args
            if name == "file_name":
                for file_name in values:
                    # print(f" file is: {file_name}", file=sys.stderr)
                    with open("finished_files.txt", "a+") as file:
                        file.write(f"{file_name}\n")
    #
    # pdb.set_trace()
    # if not any(item.session.items_left):
    #     # print("All tests are finished", file=sys.stderr)
    #     with open("finished_files.txt", "a+") as file:
    #         file.write("All tests are finished")
