from playwright.sync_api import Page, expect


class LoginPage:
    """
    Page Object Model for SauceDemo Login Page
    """

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page

        # Locators (using stable data-test attributes)
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")
        self.products_title = page.locator("span.title")

    # Page Actions

    def navigate(self) -> None:
        """Navigate to login page."""
        self.page.goto(self.URL)

    def login(self, username: str = "", password: str = "") -> None:
        """
        Perform login action.
        Accepts optional username/password to support negative scenarios.
        """
        if username:
            self.username_input.fill(username)

        if password:
            self.password_input.fill(password)

        self.login_button.click()

    def clear_fields(self) -> None:
        """Clear username and password fields."""
        self.username_input.fill("")
        self.password_input.fill("")

    # Assertions

    def assert_login_success(self) -> None:
        """Assert successful login."""
        expect(self.products_title).to_have_text("Products")

    def assert_error_message(self, expected_message: str) -> None:
        """Assert login error message."""
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(expected_message)

    # Utility Methods

    def get_error_text(self) -> str:
        """Return error message text."""
        return self.error_message.inner_text()

    def is_error_visible(self) -> bool:
        """Check if error message is displayed."""
        return self.error_message.is_visible()

    def is_login_button_enabled(self) -> bool:
        """Check if login button is enabled."""
        return self.login_button.is_enabled()