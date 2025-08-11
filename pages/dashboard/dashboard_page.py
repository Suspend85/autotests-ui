from playwright.sync_api import Page

from components.charts.chart_view_conponent import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard = DashboardToolbarViewComponent(page)

        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")

    def check_visible_dashboard_title(self):
        self.dashboard.check_visible()

    def check_visible_students_chart(self):
        self.students_chart_view.check_visible(title='Students')

    def check_visible_activities_chart(self):
        self.activities_chart_view.check_visible(title='Activities')

    def check_visible_courses_chart(self):
        self.courses_chart_view.check_visible(title='Courses')

    def check_visible_scores_chart(self):
        self.scores_chart_view.check_visible(title='Scores')
