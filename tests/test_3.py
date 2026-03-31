import time
import os
from pathlib import Path
import logging

from pages.saby_download import SabyDownloadPage
from pages.saby_home import SabyHomePage

logger = logging.getLogger(__name__)

FILE_NAME = "saby-setup.exe"
FILE_SIZE = 7377600
DIR_PATH = "./tests"

def test_task_3(browser):
    logger.info("Start the third script")
    saby_home = SabyHomePage(browser)
    logger.info("1: Go to the 'Saby' home page")
    saby_home.go_to_site()

    logger.info("2.1: Find 'Скачать локальные версии' link")
    download_page_link = saby_home.download_link
    saby_home.scroll_to_element(download_page_link)
    logger.info("2.2: Go to 'Скачать локальные версии' page")
    download_page_link.click()

    saby_download = SabyDownloadPage(browser)
    saby_download.select_app_desktop()
    logger.info("3: Download plugin")
    saby_download.download()
    time.sleep(10)

    logger.info("4: Check if the file exists")
    files_list = [p.name.title().lower() for p in Path(DIR_PATH).iterdir() if p.is_file()]
    assert FILE_NAME in files_list

    logger.info("5: Check file size")
    assert os.path.getsize(f"{DIR_PATH}/{FILE_NAME}") == FILE_SIZE