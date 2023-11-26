import pandas as pd
import pytest
import allure


@allure.story("Reports")
@pytest.mark.attach
class TestAttach:

    def test_attach_html(self):
        allure.dynamic.title("Attach html")
        allure.attach("<h1>Attach html</h1>", name="Attach html", attachment_type=allure.attachment_type.HTML)
        assert True

    def test_attach_html_table(self):
        allure.dynamic.title("Files Execution Time")
        df = pd.DataFrame({"file name": ['file one', 'file two'], "time": [3, 4]})
        allure.attach(df.to_html(index=False), name="Attach html table", attachment_type=allure.attachment_type.HTML)
        assert True

    def test_attach_data_frame(self):
        allure.dynamic.title("Files info")
        df = pd.DataFrame({"file name": ['file one', 'file two'], "size": [3, 4]})
        allure.attach(df.to_csv(index=False), name="Attach data frame", attachment_type=allure.attachment_type.CSV)
        assert True

    def test_attach_text(self):
        allure.dynamic.title("Attach text")
        allure.attach("Attach text", name="Attach text", attachment_type=allure.attachment_type.TEXT)
        assert True
