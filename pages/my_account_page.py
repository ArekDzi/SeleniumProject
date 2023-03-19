import string
import time
from random import choice
from locators.locators import ConstantRegister, ConstantUser, ConstantShippingAddress
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def create_user() -> str:
    user = "".join(choice(string.ascii_letters) for _ in range(10)) + \
           "".join(choice(string.digits) for _ in range(10))
    return user


def create_password() -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(choice(characters) for i in range(15))
    return password


def register_user(web_driver) -> tuple[str, str]:
    user = create_user()
    web_driver.find_element(*ConstantRegister.account_button).click()
    web_driver.find_element(*ConstantRegister.email_input_box).send_keys(user + "@gmail.com")
    time.sleep(1)  # it is needed to slow down password sending, possible bug
    web_driver.find_element(*ConstantRegister.password_input_box).send_keys(create_password())
    WebDriverWait(web_driver, 30).until(ec.element_to_be_clickable(ConstantRegister.register_button))
    web_driver.find_element(*ConstantRegister.register_button).click()
    WebDriverWait(web_driver, 30).until(ec.presence_of_element_located(ConstantRegister.hello_message))
    hello_message = web_driver.find_element(*ConstantRegister.hello_message).text

    return hello_message, user


def login_user(web_driver) -> str:
    web_driver.find_element(*ConstantRegister.account_button).click()
    web_driver.find_element(*ConstantUser.username_input_box).send_keys(ConstantUser.username + "@gmail.com")
    web_driver.find_element(*ConstantUser.password_input_box).send_keys(ConstantUser.password)
    web_driver.find_element(*ConstantUser.login_button).click()
    login_message = web_driver.find_element(*ConstantRegister.hello_message).text

    return login_message


def logout_user(web_driver) -> bool:
    login_user(web_driver)
    web_driver.find_element(*ConstantUser.logout_button).click()
    web_driver.find_element(*ConstantUser.logout_confirmation).click()
    web_driver.find_element(*ConstantRegister.account_button).click()

    return bool(web_driver.find_element(*ConstantRegister.login_title))


def shipping_address_setting(web_driver) -> bool:
    register_user(web_driver)
    web_driver.find_element(*ConstantShippingAddress.addresses_button).click()
    web_driver.find_element(*ConstantShippingAddress.edit_shipping_address).click()

    web_driver.find_element(*ConstantShippingAddress.first_name_box).send_keys(ConstantShippingAddress.first_name)
    web_driver.find_element(*ConstantShippingAddress.last_name_box).send_keys(ConstantShippingAddress.last_name)
    web_driver.find_element(*ConstantShippingAddress.street_box).send_keys(ConstantShippingAddress.street_address)
    web_driver.find_element(*ConstantShippingAddress.postcode_box).send_keys(ConstantShippingAddress.zip_code)
    web_driver.find_element(*ConstantShippingAddress.town_box).send_keys(ConstantShippingAddress.town)
    web_driver.find_element(*ConstantShippingAddress.save_address_button).click()

    return web_driver.find_element(*ConstantShippingAddress.address_confirmation).is_displayed()
