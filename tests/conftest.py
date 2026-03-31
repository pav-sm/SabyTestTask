import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture(scope="session")
def browser():
    options = Options()
    download_dir = os.path.abspath("./tests")
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()