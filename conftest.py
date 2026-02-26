import pytest
from playwright.sync_api import sync_playwright
import allure


@pytest.fixture(scope="function")
def page(request):
    with sync_playwright() as p:

        # Default browser
        browser_type = "chromium"
        channel = None

        # If test has cross_browser marker → override
        if request.node.get_closest_marker("cross_browser"):
            # Parametrized browsers for this test
            browser_type = request.param

        # Launch logic
        if browser_type == "firefox":
            browser = p.firefox.launch(headless=False, slow_mo=1500)
        elif browser_type == "safari":
            browser = p.webkit.launch(channel="safari", headless=False, slow_mo=1500)
        else:
            browser = p.chromium.launch(headless=False, slow_mo=1500)

        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name=f"{item.name}_failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )