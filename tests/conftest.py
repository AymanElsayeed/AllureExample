import pytest
from xml.etree import ElementTree


@pytest.fixture(scope="session", autouse=True, name="dict_to_xml")
def dict_to_xml(root_name='environment'):
    dictionary = {"1": 1}

    root = ElementTree.Element(root_name)

    for key, value in dictionary.items():

        if key.startswith('__'):
            continue

        if "password" in key.lower():
            value = '********'

        # create parameter element
        parameter = ElementTree.SubElement(root, 'parameter')
        # create key element
        key_element = ElementTree.SubElement(parameter, 'key')
        # create value element
        value_element = ElementTree.SubElement(parameter, 'value')

        key_element.text = str(key)
        value_element.text = str(value)

    tree = ElementTree.ElementTree(root)
    # with open("environment.xml", "w") as file:
    tree.write("environment.xml")
    return tree


@pytest.fixture(scope="session", autouse=True, name="customer")
def customer_fixture():
    return "customer"


@pytest.fixture(scope="session", autouse=True, name="customer2")
def customer2_fixture():
    return "customer"
