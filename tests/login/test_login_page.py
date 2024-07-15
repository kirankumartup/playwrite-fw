import pytest
import allure
from playwright.sync_api import Page, expect

from lib.csv import read_user_data
from pages.application import Application


# @pytest.mark.parametrize("user_data", [
#     {"username": "standard_user", "password": "secret_sauce"},
#     {"username": "locked_out_user", "password": "secret_sauce"},
# ])
# def test_multiple_users(page: Page, user_data):
#     page.goto("/")
#     page.fill('input[name="user-name"]', user_data["username"])
#     page.fill('input[name="password"]', user_data["password"])
#     allure.attach(page.screenshot(), name="before_login", attachment_type=allure.attachment_type.PNG)
#     page.click('input[type="submit"]')
#     assert page.locator('text=Welcome').is_visible()
#     pass

@allure.feature("User Login Tests")
@pytest.mark.parametrize("user_data", read_user_data(file_name='user_data.csv'))
def test_multiple_users(page: Page, user_data):
    application = Application(page)
    application.launch_application()
    application.login_page.login(user_data)
    application.wait_for_seconds(seconds=1)
    pass
