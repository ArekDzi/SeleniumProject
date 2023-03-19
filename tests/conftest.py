import json
from pathlib import Path
from typing import Dict
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def config() -> Dict[str, str | int]:
    with open(Path("../config.json")) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture()
def web_driver(config) -> WebDriver:
    if config['browser'] == 'chrome' or 'Chrome':
        driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    elif config['browser'] == 'firefox' or 'Firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif config['browser'] == 'edge' or 'Edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://skleptest.pl')
    yield driver
    driver.quit()
