from selenium.webdriver.common.by import By
from pages.base_locator import BaseLocator
from pages.base_tensor_page import BaseTensorPage


class TensorHomeLocators(BaseLocator):
    LOCATOR_TITLES = (By.CLASS_NAME, "tensor_ru-Index__card-title")
    LOCATOR_LINK = (By.CLASS_NAME, "tensor_ru-link")

class TensorHomePage(BaseTensorPage):

    @property
    def titles(self):
        return self.find_elements(TensorHomeLocators.LOCATOR_TITLES)

    @property
    def sila_v_ludyah_block(self):
        title = next((e for e in self.titles if e.text == "Сила в людях"), None)
        return title.find_element(*TensorHomeLocators.parent_locator(1)) if title is not None else None

    def go_to_about(self):
        self.sila_v_ludyah_block.find_element(*TensorHomeLocators.LOCATOR_LINK).click()


