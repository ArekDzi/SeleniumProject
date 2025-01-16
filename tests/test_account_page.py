from selenium.webdriver.remote.webdriver import WebDriver
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages import my_account_page



def test_register_user(web_driver: WebDriver):
    hello_message = my_account_page.register_user(web_driver)
    assert hello_message[1].lower() in hello_message[0], f"{hello_message[1]} dose not present in {hello_message[0]}"


def test_login_user(web_driver: WebDriver):
    login_message = my_account_page.login_user(web_driver)
    assert my_account_page.ConstantUser.username in login_message, + \
        f"{my_account_page.ConstantUser.username} dose not present in {login_message}"


def test_logout_user(web_driver: WebDriver):
    assert my_account_page.logout_user(web_driver), + \
        f"User dose not logout properly "


def test_shipping_address_setting(web_driver: WebDriver):
    assert my_account_page.shipping_address_setting(web_driver), + \
        "Shipping address editing went wrong"
