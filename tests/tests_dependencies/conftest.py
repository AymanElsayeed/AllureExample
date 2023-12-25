

# def pytest_collection_modifyitems(config, items):
#     # Find the test_end function in the test collection
#     test_end_item = None
#     for item in items:
#         if item.name == 'test_run_last_las':
#             test_end_item = item
#             break
#     if test_end_item is not None:
#         items.remove(test_end_item)
#     # Append the test_end function to the end of the test collection
#     if test_end_item is not None:
#         items.append(test_end_item)
