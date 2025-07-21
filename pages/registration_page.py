from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = page.get_by_test_id('registration-page-registration-button')

        self.login_link = page.get_by_test_id('registration-page-login-link')

    def fill_registration_form(self, email: str, username: str, password: str):
        self.registration_form.fill(email, username, password)

    def check_visible_form_inputs_and_fills(self, email: str, username: str, password: str):
        self.registration_form.check_visible(email, username, password)

    def click_registration_button(self):
        expect(self.registration_button).to_be_enabled()
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()




