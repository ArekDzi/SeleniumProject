import string
from random import choice
from typing import Tuple
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ConstantRegister:
    account_button: Tuple[str, str] = (By.XPATH, "//li[@class='top-account']")
    register_button: Tuple[str, str] = (By.XPATH, "//input[@class='woocommerce-Button button' and @name='register']")
    email_input_box: Tuple[str, str] = (By.XPATH, "//input[@id='reg_email']")
    password_input_box: Tuple[str, str] = (By.XPATH, '//*[@id="reg_password"]')
    hello_message: Tuple[str, str] = (By.XPATH, "//div[@class='woocommerce-MyAccount-content']")
    register_title: Tuple[str, str] = (By.XPATH, "//h2[contains(text(),'Register')]")
    login_title: Tuple[str, str] = (By.XPATH, '//*[@id="customer_login"]/div[1]/h2')


class ConstantUser:
    username_input_box: Tuple[str, str] = (By.XPATH, '//*[@id="username"]')
    password_input_box: Tuple[str, str] = (By.XPATH, '//*[@id="password"]')
    login_button: Tuple[str, str] = (By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
    username: str = 'l.miotk.py'
    password: str = "Aut0m@ty$a$uper!"
    logout_button: Tuple[str, str] = (By.XPATH, '//*[@id="post-8"]/div[2]/nav/ul/li[6]/a')
    logout_confirmation: Tuple[str, str] = (By.XPATH, '//*[@id="post-8"]/div[2]/div[1]/a')


class ConstantShippingAddress:
    addresses_button: Tuple[str, str] = (By.XPATH, '//*[@id="post-8"]/div[2]/nav/ul/li[4]/a')
    edit_shipping_address: Tuple[str, str] = (By.XPATH, '//*[@id="post-8"]/div[2]/div/div/div[2]/header/a')
    first_name_box: Tuple[str, str] = (By.ID, 'shipping_first_name')
    last_name_box: Tuple[str, str] = (By.ID, 'shipping_last_name')
    street_box: Tuple[str, str] = (By.ID, 'shipping_address_1')
    postcode_box: Tuple[str, str] = (By.ID, 'shipping_postcode')
    town_box: Tuple[str, str] = (By.ID, 'shipping_city')
    first_name: str = "Jan"
    last_name: str = "Kowalski"
    street_address: str = "Budowlanych 15"
    town: str = "Gdańsk"
    zip_code: str = "80-298"
    save_address_button: Tuple[str, str] = (By.XPATH, '//*[@id="post-8"]/div[2]/div/form/div/p/input[1]')
    address_confirmation: Tuple[str, str] = (By.XPATH, '//*[@id="post-8"]/div[2]/div[1]')
    address_confirmation_text: str = 'Address changed successfully.'


def create_user():
    user = "".join(choice(string.ascii_letters) for i in range(10)) + \
           "".join(choice(string.digits) for i in range(10))
    return user


def create_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(choice(characters) for i in range(15))
    return password


def register_user(web_driver):
    user = create_user()
    web_driver.find_element(*ConstantRegister.account_button).click()
    web_driver.find_element(*ConstantRegister.email_input_box).send_keys(user + "@gmail.com")
    web_driver.find_element(*ConstantRegister.password_input_box).send_keys(create_password())
    web_driver.find_element(*ConstantRegister.email_input_box).click()
    web_driver.find_element(*ConstantRegister.password_input_box).send_keys(Keys.BACKSPACE)
    # it is needed to delete last char from password to make Register button available
    WebDriverWait(web_driver, 30).until(ec.element_to_be_clickable(ConstantRegister.register_button))
    web_driver.find_element(*ConstantRegister.register_button).click()
    WebDriverWait(web_driver, 30).until(ec.presence_of_element_located(ConstantRegister.hello_message))
    hello_message = web_driver.find_element(*ConstantRegister.hello_message).text

    return hello_message, user


def login_user(web_driver):
    web_driver.find_element(*ConstantRegister.account_button).click()
    web_driver.find_element(*ConstantUser.username_input_box).send_keys(ConstantUser.username + "@gmail.com")
    web_driver.find_element(*ConstantUser.password_input_box).send_keys(ConstantUser.password)
    web_driver.find_element(*ConstantUser.login_button).click()
    login_message = web_driver.find_element(*ConstantRegister.hello_message).text

    return login_message


def logout_user(web_driver):
    login_user(web_driver)
    web_driver.find_element(*ConstantUser.logout_button).click()
    web_driver.find_element(*ConstantUser.logout_confirmation).click()
    web_driver.find_element(*ConstantRegister.account_button).click()

    return bool(web_driver.find_element(*ConstantRegister.login_title))


def shipping_address_setting(web_driver):
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
