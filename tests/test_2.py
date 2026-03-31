import logging

from pages.saby_contacts import SabyContactsPage
from pages.saby_home import SabyHomePage

logger = logging.getLogger(__name__)

ORIGINAL_REGION = "Ивановская обл."
PARTNERS_LIST_OF_ORIGINAL_REGION = [
    """Saby - Иваново
пл.Пушкина, 13, оф.308
+7 4932 34-60-56
+7 4932 26-27-73
saby.ru
info@ivanovo.tensor.ru""".rstrip(),
    """Сервис ТВ-Инфо
ул. Парижской Коммуны, 16
+7 4932 93-09-09
budalova@stv.indi.ru""".rstrip(),
    """Ванесс
ул. 9 Января, д. 7А, помещ. 305
+7 4932 59-17-49
+7 901 686-89-51
vaness.org@yandex.ru""".rstrip(),
    """ИП Молодкина Ирина Юрьевна
ул. Садовая, д. 35, пом. 1001
+7 960 511-58-42
1c-mkt@mail.ru""".rstrip()
]
CONTACT_PAGE_URL_ORIGINAL_REGION = "https://saby.ru/contacts/37-ivanovskaya-oblast?tab=clients"
CONTACT_PAGE_TITLE_ORIGINAL_REGION = "Saby Контакты — Ивановская область"

NEW_REGION = "Камчатский край"
PARTNERS_LIST_OF_NEW_REGION = [
    """Saby - Камчатка
пр-кт Карла Маркса, д. 31/2, оф. 315
+7 4152 21-56-60
+7 4152 34-01-08
saby.ru
info@kamchatka.tensor.ru""".rstrip()
]
CONTACT_PAGE_URL_NEW_REGION = "https://saby.ru/contacts/41-kamchatskij-kraj?tab=clients"
CONTACT_PAGE_TITLE_NEW_REGION = "Saby Контакты — Камчатский край"


def test_task_2(browser):
    logger.info("Start the second script")
    saby_home = SabyHomePage(browser)
    logger.info("1.1: Go to the 'Saby' home page")
    saby_home.go_to_site()
    logger.info("1.2: Go to the 'Контакты'")
    saby_home.go_to_contacts()

    saby_contacts = SabyContactsPage(browser)
    logger.info("2.1: Check the current region")
    region = saby_contacts.current_region
    assert region.text == ORIGINAL_REGION
    assert browser.current_url == CONTACT_PAGE_URL_ORIGINAL_REGION
    assert browser.title == CONTACT_PAGE_TITLE_ORIGINAL_REGION
    logger.info("2.2: Check the partners list")
    contacts = saby_contacts.partners_items
    contacts_list = [contact.text for contact in contacts]
    assert len(contacts_list) > 0
    assert contacts_list == PARTNERS_LIST_OF_ORIGINAL_REGION

    logger.info("3: Change the region")
    region.click()
    saby_contacts.set_new_region(NEW_REGION)

    saby_contacts.url_change(CONTACT_PAGE_URL_ORIGINAL_REGION)
    logger.info("4.1: Check of update region")
    region = saby_contacts.current_region
    assert region.text == NEW_REGION
    logger.info("4.2: Check of update partners list")
    contacts = saby_contacts.partners_items
    contacts_list = [contact.text for contact in contacts]
    assert len(contacts_list) > 0
    assert contacts_list == PARTNERS_LIST_OF_NEW_REGION
    logger.info("4.3: Check of update url")
    assert browser.current_url == CONTACT_PAGE_URL_NEW_REGION
    logger.info("4.4: Check of update tab title")
    assert browser.title == CONTACT_PAGE_TITLE_NEW_REGION
