import asyncio
import pytest
import allure


@pytest.mark.duration
@pytest.mark.asyncio
class TestDuration:

    async def test_duration_10(self):
        allure.dynamic.title("Duration 10 seconds")
        await asyncio.sleep(10)
        assert True

    async def test_duration_8(self):
        allure.dynamic.title("Duration 8 seconds")
        await asyncio.sleep(8)
        assert True

    async def test_duration_6(self):
        allure.dynamic.title("Duration 6 seconds")
        await asyncio.sleep(6)
        assert True

    async def test_duration_4(self):
        allure.dynamic.title("Duration 4 seconds")
        await asyncio.sleep(4)
        assert True

    async def test_duration_2(self):
        allure.dynamic.title("Duration 2 seconds")
        await asyncio.sleep(2)
        assert True

    async def test_duration_0(self):
        allure.dynamic.title("Duration 0 seconds")
        assert True
