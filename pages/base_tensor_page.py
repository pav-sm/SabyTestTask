from pages.base_page import BasePage


class BaseTensorPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.base_url = "https://tensor.ru/"