# Assuming you have an async fixture for creating a browser
import pytest
from playwright.async_api import async_playwright

@pytest.fixture(scope="session")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = browser.new_page()
        yield page
        await browser.close()