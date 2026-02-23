from playwright.sync_api import Page, expect

#Registration Page

#Login with valid username and password:

def test_login_with_standard_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

#assertion added for successful login

    products_header = page.locator("span.title")
    expect(products_header).to_contain_text("Products")

#Login with invalid username and password:

def test_login_with_invalid_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("invalid_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

#assertion added for error message given

    error_message = "Username and password do not match any user in this service"
    error_msg_loc = page.locator("//h3[@data-test='error']")
    expect(error_msg_loc).to_contain_text(error_message)

#Login with no username and password:

def test_login_with_no_credentials(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_text("Login").click()

#assertion added for error message given

    error_message = "Username is required"
    error_msg_loc = page.locator("//h3[@data-test='error']")
    expect(error_msg_loc).to_contain_text(error_message)
