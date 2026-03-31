from selenium.webdriver.common.by import By
from pages.base_locator import BaseLocator
from pages.base_tensor_page import BaseTensorPage


class TensorAboutLocators(BaseLocator):
    LOCATOR_ABOUT_TITLE = (By.CLASS_NAME, "tensor_ru-About__block-title")
    LOCATOR_IMAGE = (By.TAG_NAME, "img")

class TensorAboutPage(BaseTensorPage):

    @property
    def titles(self):
        return self.find_elements(TensorAboutLocators.LOCATOR_ABOUT_TITLE)

    @property
    def block_rabotaem(self):
        block = next((block for block in self.titles if block.text == "Работаем"), None)
        return block.find_element(*TensorAboutLocators.parent_locator(2)) if block is not None else None