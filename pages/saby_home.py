from selenium.webdriver.common.by import By

from pages.base_locator import BaseLocator
from pages.base_saby_page import BaseSabyPage


class SabyHomePageLocators(BaseLocator):
    LOCATOR_MENU_ITEMS = (By.CLASS_NAME, "sbisru-Header__menu-item")
    LOCATOR_CONTACTS_POPUP = (By.CLASS_NAME, "sbisru-MenuPopupTemplate__loaded-template")
    LOCATOR_CONTACTS_LINK = (By.CLASS_NAME, "sbisru-link")
    LOCATOR_FOOTER_CONTAINER = (By.CLASS_NAME, "sbisru-Footer__container")
    LOCATOR_FOOTER_CELL_TITLE = (By.CLASS_NAME, "sbisru-Footer__title")
    LOCATOR_FOOTER_LIST_ITEM = (By.CLASS_NAME, "sbisru-Footer__list-item")
    LOCATOR_FOOTER_LINK = (By.CLASS_NAME, "sbisru-Footer__link")

class SabyHomePage(BaseSabyPage):

    @property
    def menu_items(self):
        return self.find_elements(SabyHomePageLocators.LOCATOR_MENU_ITEMS)

    @property
    def tensor_contacts(self):
        element = next((e for e in self.menu_items if e.text == "Контакты"), None)
        return self.wait_visibility(element)

    @property
    def contacts_popup(self):
        self.move_to_element(self.tensor_contacts)
        return self.find_element(SabyHomePageLocators.LOCATOR_CONTACTS_POPUP)

    @property
    def contacts_link(self):
        element = self.contacts_popup.find_element(*SabyHomePageLocators.LOCATOR_CONTACTS_LINK)
        return self.wait_clickable(element)

    @property
    def footer_container(self):
        return self.find_element(SabyHomePageLocators.LOCATOR_FOOTER_CONTAINER)

    @property
    def footer_titles(self):
        return self.footer_container.find_elements(*SabyHomePageLocators.LOCATOR_FOOTER_CELL_TITLE)

    @property
    def useful_footer_cell(self):
        title_cell = next((title for title in self.footer_titles if title.text == "Полезное"), None)
        return title_cell.find_element(*SabyHomePageLocators.parent_locator(1))

    @property
    def download_link(self):
        links = self.useful_footer_cell.find_elements(*SabyHomePageLocators.LOCATOR_FOOTER_LIST_ITEM)
        d_link = next(
            (link.find_element(*SabyHomePageLocators.LOCATOR_FOOTER_LINK)
             for link in links if link.text == "Скачать локальные версии"),
            None)
        return self.wait_clickable(d_link)

    def go_to_contacts(self):
        self.contacts_link.click()

