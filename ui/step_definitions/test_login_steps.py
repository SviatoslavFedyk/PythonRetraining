from pytest_bdd import scenarios, given, when, then
from playwright.async_api import Page, expect
from page_objects.login_page import LoginPage
from page_objects.dashboard_page import DashboardPage

scenarios('../features/functional_login_test.feature')

@given('the dashboard page is open')
def open_dashboard(page: Page):
    DashboardPage(page).open_site()

@then('I should see the dashboard page')
def verify_dashboard_page(page: Page):
    assert DashboardPage(page).verify_dashboard_page()

@when('I click the Sign In button in the header')
def open_login_page(page: Page):
    LoginPage(page).open_login_page()

@when('I enter the password in the field')
def input_password(page: Page):
    LoginPage(page).input_password()

@when('I enter the username in the field')
def input_username(page: Page):
    LoginPage(page).input_username()

@when('I press the Sign In button')
def click_sign_in(page: Page):
    LoginPage(page).click_sign_in()

@then('I should see the login page')
def verify_login_page(page: Page):
    assert LoginPage(page).verify_login_page()

@then('I log into my account')
def is_logged_in(page: Page):
    assert LoginPage(page).is_logged_in()