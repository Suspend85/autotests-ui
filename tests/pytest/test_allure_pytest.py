import allure


@allure.step("Opening browser")
def open_browser():
    with allure.step('Get browser'):
        ...

    with allure.step('Start browser'):
        with allure.step('Get data for browser'):
            ...


@allure.step("Creating course with title '{title123}' ")
def create_course(title123: str):
    ...


@allure.step("Edit course")
def edit_course(title: str):
    with allure.step(f'Edit course with "{title}"'):
        ...


@allure.step("Closing browser")
def close_browser():
    ...


def test_feature():
    open_browser()
    create_course('Playwright1')
    create_course('Playwright2')
    create_course('Playwright3')
    edit_course('Python')
    close_browser()


