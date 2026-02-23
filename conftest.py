import pytest
from playwright.sync_api import sync_playwright
import allure


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # We take screenshot only after test execution phase
    if rep.when == "call":
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name=f"{item.name}_screenshot",
                attachment_type=allure.attachment_type.PNG
            )