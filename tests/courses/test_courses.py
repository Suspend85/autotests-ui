import pytest
import allure
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGISTRATION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.check_visible_create_course_title_and_button()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.check_visible_create_course_form('', '', '', '0', '0')
        create_course_page.fill_create_course_form('Playwright', '3h40m', 'playwright', '130', '30')

        create_course_page.check_visible_exercise_title_and_button()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.jpg')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(index=0, title='Playwright', max_score='130', min_score='30',
                                                    estimated_time='3h40m')

    @allure.title('Edit course')
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.fill_create_course_form('Playwright', '3h40m', 'playwright', '130', '30')
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.jpg')
        create_course_page.click_create_course_button()

        courses_list_page.course_view.check_visible(0, 'Playwright', '130', '30', '3h40m')

        courses_list_page.course_view_menu_component.click_edit(index=0)
        create_course_page.fill_create_course_form('Playwright2', '4h50m', 'playwright2', '140', '40')
        create_course_page.click_create_course_button()
        courses_list_page.course_view.check_visible(0, 'Playwright2', '140', '40', '4h50m')
