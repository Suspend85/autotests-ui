from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    title_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(title_courses).to_be_enabled()
    expect(title_courses).to_have_text('Courses')

    content_courses = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(content_courses).to_be_enabled()
    expect(content_courses).to_have_text('There is no results')

