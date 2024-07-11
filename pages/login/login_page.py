from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.example_element = ("ID", "example_id")
        pass

    def get_example_text(self):
        return self.find_element(*self.example_element).text
