from pages.base_page import BasePage


class BaseSabyPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.base_url = "https://saby.ru/"