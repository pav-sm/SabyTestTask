from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    base_url: str

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def wait_visibility(self, element, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of(element))

    def wait_clickable(self, element, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(element))

    def url_change(self, old_url, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_changes(old_url))

    def move_to_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)