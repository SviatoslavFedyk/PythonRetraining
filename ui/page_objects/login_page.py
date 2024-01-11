from .base_page import BasePage

class LoginPage(BasePage):

    header_user = "//div[@class='AppHeader-user']"
    login_field = "#login_field"
    password_field = "#password"
    sign_in_button = "//input[@type='submit']"
    account_modal = "//modal-dialog//ancestor::span[contains(text(), 'Sign out')]"
    header_sign_in_button= "(// a[contains(text(), 'Sign in')])[2]"

    username = "uitestdurotan"
    password = "uitestdurotan123456"

    def verify_login_page(self):
        return self.page.url == "https://github.com/login"

    def input_username(self):
        self.page.locator(self.login_field).fill(self.username)

    def input_password(self):
        self.page.locator(self.password_field).fill(self.password)

    def click_sign_in(self):
        self.page.click(self.sign_in_button)

    def is_logged_in(self):
        self.page.click(self.header_user)
        print(self.page.locator(self.account_modal))

    def open_login_page(self):
        self.page.click(self.header_sign_in_button)
