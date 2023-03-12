from selenium.webdriver.remote.webdriver import WebDriver
from pages import my_account_page


def test_register_user(web_driver: WebDriver):
    hello_message = my_account_page.register_user(web_driver)
    assert hello_message[1] in hello_message[0], f"{hello_message[1]} dose not present in {hello_message[0]}"


def test_login_user(web_driver: WebDriver):
    login_message = my_account_page.login_user(web_driver)
    assert my_account_page.ConstantUser.username in login_message, + \
        f"{my_account_page.ConstantUser.username} dose not present in {login_message}"


def test_logout_user(web_driver: WebDriver):
    successful_logout = my_account_page.logout_user(web_driver)
    assert True == successful_logout, + \
        f"User dose not logout properly "


def test_shipping_address_setting(web_driver: WebDriver):
    successful_change = my_account_page.shipping_address_setting(web_driver)
    assert True == successful_change, + \
        "Shipping address editing went wrong"
