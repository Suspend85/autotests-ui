from playwright.sync_api import sync_playwright, expect


def login_test():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill('')
        email_input.fill('user.name@gmail.com')

        password_input = page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill('')
        password_input.fill('Password')

        login_button = page.get_by_test_id('login-page-login-button')
        login_button.click()

        wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")


def registration_test():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('')
        password_input.fill('password')

        login_button = page.get_by_test_id('registration-page-registration-button')
        login_button.click()

        dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_title).to_be_visible()
        expect(dashboard_title).to_have_text("Dashboard")


registration_test()
