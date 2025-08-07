from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)  # create-course-exercise-1000-box-toolbar-subtitle-text
        return self.page.get_by_test_id(locator).nth(nth)
        # return self.page.locator(locator)  # как вариант, если на странице нет test_id

    def click(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_text(text)


# def base():
#     page = ...
#     login_button = BaseElement(page, 'test-login-button', 'Login button')
#
#     login_button.click()
#     login_button.check_visible()
