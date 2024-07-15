import allure
from playwright.sync_api import Page

from pages.login.login_page import LoginPage


class Application:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_page = LoginPage(page=page)
        pass

    @allure.step("Launching application")
    def launch_application(self):
        self.page.goto("/")
        pass

    @allure.step("Wait for Seconds")
    def wait_for_seconds(self, seconds: int):
        self.page.wait_for_timeout(seconds * 1000)
        pass

    pass
