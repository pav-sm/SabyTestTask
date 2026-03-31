from selenium.webdriver.common.by import By
from pages.base_locator import BaseLocator
from pages.base_saby_page import BaseSabyPage


class SabyContactsPageLocators(BaseLocator):
    LOCATOR_CONTACTS_CLIENTS = (By.CLASS_NAME, "sbisru-Contacts")
    LOCATOR_TENSOR_CONTACTS = (By.CLASS_NAME, "sbisru-Contacts__border-left")
    LOCATOR_TENSOR_LOGO = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
    LOCATOR_CURRENT_REGION = (By.CLASS_NAME, "sbis_ru-Region-Chooser")
    LOCATOR_PARTNERS_LIST = (By.ID, "contacts_list")
    LOCATOR_PARTNERS_ITEMS = (By.CLASS_NAME, "sbisru-Contacts-List__item")
    LOCATOR_CONTAINER_REGIONS = (By.CLASS_NAME, "sbis_ru-Region-Panel__container")
    LOCATOR_ITEM_REGION = (By.CLASS_NAME, "sbis_ru-Region-Panel__item")
    LOCATOR_LINK = (By.CLASS_NAME, "sbis_ru-link")

class SabyContactsPage(BaseSabyPage):

    @property
    def contacts_clients(self):
        return self.find_element(SabyContactsPageLocators.LOCATOR_CONTACTS_CLIENTS)

    @property
    def tensor_contacts(self):
        element = self.contacts_clients.find_element(*SabyContactsPageLocators.LOCATOR_TENSOR_CONTACTS)
        return self.wait_visibility(element)

    @property
    def tensor_logo(self):
        element = self.tensor_contacts.find_element(*SabyContactsPageLocators.LOCATOR_TENSOR_LOGO)
        return self.wait_clickable(element)

    @property
    def current_region(self):
        element = self.contacts_clients.find_element(*SabyContactsPageLocators.LOCATOR_CURRENT_REGION)
        return self.wait_clickable(element)

    @property
    def partners_list(self):
        element = self.contacts_clients.find_element(*SabyContactsPageLocators.LOCATOR_PARTNERS_LIST)
        return self.wait_visibility(element)

    @property
    def partners_items(self):
        elements = (
            self.partners_list.find_elements(*SabyContactsPageLocators.LOCATOR_PARTNERS_ITEMS))
        partners_items = []
        for e in elements:
            partners_items.append(self.wait_visibility(e))
        return partners_items

    @property
    def regions(self):
        container = self.find_element(SabyContactsPageLocators.LOCATOR_CONTAINER_REGIONS)
        elements = container.find_elements(*SabyContactsPageLocators.LOCATOR_ITEM_REGION)
        regions = []
        for e in elements:
            regions.append(self.wait_clickable(e))
        return regions

    def set_new_region(self, new_region):
        elements = (self.wait_clickable(item.find_element(*SabyContactsPageLocators.LOCATOR_LINK))
                    for item in self.regions)
        link_new_region = next((e for e in elements if e.get_attribute("title") == new_region), None)
        link_new_region.click()
