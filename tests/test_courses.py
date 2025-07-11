from playwright.sync_api import expect, Page
import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from pages.dashboard_page import DashboardPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    title_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(title_courses).to_be_enabled()
    expect(title_courses).to_have_text('Courses')

    content_courses = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(content_courses).to_be_enabled()
    expect(content_courses).to_have_text('There is no results')


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(chromium_page_with_state: Page, courses_list_page: CoursesListPage,
                       create_course_page: CreateCoursePage
                       ):
    page = chromium_page_with_state
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form('', '', '',
                                                        '0', '0')
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image('./testdata/files/image.jpg')
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form('Playwright', '2 weeks', 'Playwright', '100', '10')
    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(index=0, title='Playwright', max_score='100', min_score='10', estimated_time='2 weeks')





