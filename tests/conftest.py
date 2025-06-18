from playwright.sync_api import sync_playwright, Page, Playwright
import pytest


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    # print("Before")
    yield browser.new_page()
    # print("After")
    browser.close()
