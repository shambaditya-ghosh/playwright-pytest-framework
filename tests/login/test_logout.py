import pytest
from playwright.sync_api import Page, expect

def test_logout(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

#assertion added for successful login

    products_header = page.locator("span.title")
    expect(products_header).to_contain_text("Products")

    burger_menu = page.locator("button#react-burger-menu-btn")
    burger_menu.click()

    logout_button = page.locator("//div[@class = 'bm-menu']//a[text()='Logout']")
    logout_button.click()
    expect(page.get_by_text("login")).to_be_visible()


@pytest.mark.cross_browser
@pytest.mark.parametrize("page", ["Chrome","firefox", "webkit"], indirect=True)
def test_logout_all_browser(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

#assertion added for successful login

    products_header = page.locator("span.title")
    expect(products_header).to_contain_text("Products")

    burger_menu = page.locator("button#react-burger-menu-btn")
    burger_menu.click()

    logout_button = page.locator("//div[@class = 'bm-menu']//a[text()='Logout']")
    logout_button.click()
    expect(page.get_by_text("login")).to_be_visible()