from selenium.webdriver.common.by import By

class BaseLocator:
    @staticmethod
    def parent_locator(level = 1):
        return By.XPATH, f"./{'../' * level}"[:-1]
