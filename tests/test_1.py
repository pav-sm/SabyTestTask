import logging

from pages.saby_contacts import SabyContactsPage
from pages.saby_home import SabyHomePage
from pages.tensor_about import TensorAboutPage, TensorAboutLocators
from pages.tensor_home import TensorHomePage

TENSOR_HOME_PAGE_URL = "https://tensor.ru/"
TENSOR_ABOUT_PAGE_URL = "https://tensor.ru/about"
TENSOR_ABOUT_TAB_TITLE = "О компании | Тензор — IT-компания"

logger = logging.getLogger(__name__)

def get_sizes_of_images(block):
    images = block.find_elements(*TensorAboutLocators.LOCATOR_IMAGE)
    sizes = []
    for image in images:
        sizes.append((image.get_attribute("height"), image.get_attribute("width")))
    return sizes

def test_task_1(browser):
    logger.info("Start the first script")
    saby_home = SabyHomePage(browser)
    logger.info("1.1: Go to the 'Saby' home page")
    saby_home.go_to_site()
    saby_window = browser.current_window_handle
    logger.info("1.2: Go to the 'Контакты'")
    saby_home.go_to_contacts()

    saby_contacts = SabyContactsPage(browser)
    logger.info("2.1: Find the 'Tensor' banner")
    tensor_banner = saby_contacts.tensor_logo
    logger.info("2.2: Click on the banner")
    tensor_banner.click()

    windows = browser.window_handles
    tensor_window = next((window for window in windows if window != saby_window), None)
    logger.info("3: Go to the 'Tensor' home page")
    browser.switch_to.window(tensor_window)
    assert browser.current_url == TENSOR_HOME_PAGE_URL

    tensor_home = TensorHomePage(browser)
    logger.info("4: Find the 'Сила в людях' block")
    sila_v_ludyah = tensor_home.sila_v_ludyah_block
    assert sila_v_ludyah is not None

    logger.info("5: Go to the 'Подробнее' page")
    tensor_home.go_to_about()
    assert browser.current_url == TENSOR_ABOUT_PAGE_URL
    assert browser.title == TENSOR_ABOUT_TAB_TITLE

    tensor_about = TensorAboutPage(browser)
    logger.info("6.1: Find the 'Работаем' block")
    rabotaem = tensor_about.block_rabotaem
    logger.info("6.2: Check of images sizes")
    img_sizes = get_sizes_of_images(rabotaem)
    assert len(set(img_sizes)) == 1
