import allure


class LoginPage:
    def __init__(self, page):
        self.page = page
        pass

    @allure.step("Logging in with user data: {user_data}")
    def login(self, user_data: dict):
        self.page.fill("//input[@name='user-name']", user_data['username'])
        self.page.fill("//input[@name='password']", user_data['password'])
        self.page.click("//input[@type='submit']")
        pass
