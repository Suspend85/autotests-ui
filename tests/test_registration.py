from playwright.sync_api import Page, expect
import pytest
from pages.base_page import BasePage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize('email, username, password',
                         [('user.name@gmail.com', 'username', 'password'),
                          ('user.name@gmail.com', 'username', ''),
                          ('user.name@gmail.com', '', 'password'),
                          ('', 'username', 'password'),
                          ('', 'username', ''),
                          ('', '', 'password')]
                         )
def test_successful_registration(email: str, username: str, password: str, registration_page: RegistrationPage,
                                 dashboard_page: DashboardPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form(email=email, username=username, password=password)
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()

    # registration_page.check_registration_success()

    # chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    #
    # email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    # email_input.clear()
    # email_input.fill('user.name@gmail.com')
    #
    # username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    # username_input.clear()
    # username_input.fill('username')
    #
    # password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    # password_input.clear()
    # password_input.fill('password')
    #
    # login_button = chromium_page.get_by_test_id('registration-page-registration-button')
    # login_button.click()
    #
    # dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    # expect(dashboard_title).to_be_visible()
