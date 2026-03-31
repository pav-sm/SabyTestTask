from selenium.webdriver.common.by import By

from pages.base_locator import BaseLocator
from pages.base_saby_page import BaseSabyPage


class SabyDownloadPageLocators(BaseLocator):
    LOCATOR_APPLICATION_TYPE = (By.CLASS_NAME, "controls-TabButton")
    LOCATOR_APPLICATION_INFO = (By.CLASS_NAME, "ws-SwitchableArea__item")
    LOCATOR_DOWNLOAD_BLOCK = (By.CLASS_NAME, "sbis_ru-DownloadNew-block")
    LOCATOR_DOWNLOAD_PLUGIN_BUTTON = (By.XPATH, '//a[@title="Скачать"]')

class SabyDownloadPage(BaseSabyPage):
    @property
    def applications(self):
        return self.find_elements(SabyDownloadPageLocators.LOCATOR_APPLICATION_TYPE)

    @property
    def app_desktop(self):
        element = next((app for app in self.applications if app.text == "Saby (десктоп)"), None)
        return self.wait_clickable(element)

    @property
    def applications_info(self):
        return self.find_elements(SabyDownloadPageLocators.LOCATOR_APPLICATION_INFO)

    @property
    def app_desktop_info(self):
        element = next((e for e in self.applications_info if e.get_attribute("data-for") == "plugin"), None)
        return self.wait_visibility(element)

    @property
    def app_desktop_download_button(self):
        blocks = self.app_desktop_info.find_elements(*SabyDownloadPageLocators.LOCATOR_DOWNLOAD_BLOCK)
        block = next((b for b in blocks if "Ручная установка" in b.text), None)
        button = block.find_element(*SabyDownloadPageLocators.LOCATOR_DOWNLOAD_PLUGIN_BUTTON)
        return self.wait_clickable(button)

    def select_app_desktop(self):
        self.app_desktop.click()

    def download(self):
        self.app_desktop_download_button.click()

