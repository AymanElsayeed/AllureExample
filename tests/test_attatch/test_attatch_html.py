
import pandas as pd
import pytest
import allure


@pytest.mark.attach
class TestAttach:

    def test_attach_html(self):
        allure.dynamic.title("Attach html")
        allure.attach("<h1>Attach html</h1>", name="Attach html", attachment_type=allure.attachment_type.HTML)
        assert True

    def test_attach_html_table(self):
        allure.dynamic.story("Attach html table")
        allure.dynamic.title("Attach html table")
        df = pd.DataFrame({"file name": ['file one', 'file two'], "time": [3, 4]})
        allure.attach(df.to_html(index=False), name="Attach html table", attachment_type=allure.attachment_type.HTML)
        assert True
