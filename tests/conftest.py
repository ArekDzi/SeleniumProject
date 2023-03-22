import json
from pathlib import Path
from typing import Dict, Union
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService


@pytest.fixture()
def config():
    with open(Path("../config.json")) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture()
def web_driver(config) -> WebDriver:
    if config["browser"] == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif config['browser'] == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif config['browser'] == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif config['browser'] == 'chromium':
        driver = webdriver.Chrome(
            service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://skleptest.pl')
    yield driver
    driver.quit()
