import pytest
from playwright.sync_api import sync_playwright
import allure


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
<<<<<<< HEAD
        browser = p.chromium.launch(
            headless=False,  #  headed mode
            slow_mo=1500     #  1.5s delay
        )
=======
        browser = p.chromium.launch(headless=False)
>>>>>>> parent of 02033d3 (Changes in conftest.py & Readme.md)
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