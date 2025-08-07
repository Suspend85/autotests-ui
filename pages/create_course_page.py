from playwright.sync_api import Page

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage
from components.views.empty_view_component import EmptyViewComponent


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_exercise_toolbar = CreateCourseExercisesToolbarViewComponent(page)
        self.create_course_toolbar = CreateCourseToolbarViewComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_course_exercise_form = CreateCourseExerciseFormComponent(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')

    def check_visible_create_course_title_and_button(self):
        self.create_course_toolbar.check_visible(True)

    def click_create_course_button(self):
        self.create_course_toolbar.click_create_course_button()

    def check_visible_create_course_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.create_course_form.check_visible(title, estimated_time, description, max_score, min_score)

    def fill_create_course_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.create_course_form.fill(title, estimated_time, description, max_score, min_score)

    def check_visible_exercise_title_and_button(self):
        self.create_course_exercise_toolbar.check_visible()

    def click_create_exercise_button(self):
        self.create_course_exercise_toolbar.click_create_exercise_button()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )

