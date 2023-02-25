import string
from random import choice
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Constant_Register:
    account_button = (By.XPATH, "//li[@class='top-account']")
    register_button = (By.XPATH, "//input[@class='woocommerce-Button button' and @name='register']")
    email_input_box = (By.XPATH, "//input[@id='reg_email']")
    password_input_box = (By.XPATH, '//*[@id="reg_password"]')
    hello_message = (By.XPATH, "//div[@class='woocommerce-MyAccount-content']")
    register_title = (By.XPATH, "//h2[contains(text(),'Register')]")
    login_title = (By.XPATH, '//*[@id="customer_login"]/div[1]/h2')


class Constant_User:
    username_input_box = (By.XPATH, '//*[@id="username"]')
    password_input_box = (By.XPATH, '//*[@id="password"]')
    login_button = (By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
    username = 'l.miotk.py'
    password = "Aut0m@ty$a$uper!"
    logout_button = (By.XPATH, '//*[@id="post-8"]/div[2]/nav/ul/li[6]/a')
    logout_confirmation = (By.XPATH, '//*[@id="post-8"]/div[2]/div[1]/a')


class Constant_shipping_address:
    addresses_button = (By.XPATH, '//*[@id="post-8"]/div[2]/nav/ul/li[4]/a')
    edit_shipping_address = (By.XPATH, '//*[@id="post-8"]/div[2]/div/div/div[2]/header/a')
    first_name_box = (By.ID, 'shipping_first_name')
    last_name_box = (By.ID, 'shipping_last_name')
    street_box = (By.ID, 'shipping_address_1')
    postcode_box = (By.ID, 'shipping_postcode')
    town_box = (By.ID, 'shipping_city')
    first_name = "Jan"
    last_name = "Kowalski"
    street_address = "Budowlanych 15"
    town = "Gdańsk"
    zip_code = "80-298"
    save_address_button = (By.XPATH, '//*[@id="post-8"]/div[2]/div/form/div/p/input[1]')
    adress_confirmation = (By.XPATH, '//*[@id="post-8"]/div[2]/div[1]')
    address_confirmation_text = 'Address changed successfully.'


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
    web_driver.find_element(*Constant_Register.account_button).click()
    web_driver.find_element(*Constant_Register.email_input_box).send_keys(user + "@gmail.com")
    web_driver.find_element(*Constant_Register.password_input_box).send_keys(create_password())
    web_driver.find_element(*Constant_Register.register_title).click()
    WebDriverWait(web_driver, 30).until(ec.element_to_be_clickable(Constant_Register.register_button))
    web_driver.find_element(*Constant_Register.register_button).click()
    WebDriverWait(web_driver, 30).until(ec.presence_of_element_located(Constant_Register.hello_message))
    hello_message = web_driver.find_element(*Constant_Register.hello_message).text

    return hello_message, user


def login_user(web_driver):
    web_driver.find_element(*Constant_Register.account_button).click()
    web_driver.find_element(*Constant_User.username_input_box).send_keys(Constant_User.username + "@gmail.com")
    web_driver.find_element(*Constant_User.password_input_box).send_keys(Constant_User.password)
    web_driver.find_element(*Constant_User.login_button).click()
    login_message = web_driver.find_element(*Constant_Register.hello_message).text

    return login_message


def logout_user(web_driver):
    login_user(web_driver)
    web_driver.find_element(*Constant_User.logout_button).click()
    web_driver.find_element(*Constant_User.logout_confirmation).click()
    web_driver.find_element(*Constant_Register.account_button).click()

    return bool(web_driver.find_element(*Constant_Register.login_title))


def shipping_address_setting(web_driver):
    register_user(web_driver)
    web_driver.find_element(*Constant_shipping_address.addresses_button).click()
    web_driver.find_element(*Constant_shipping_address.edit_shipping_address).click()

    web_driver.find_element(*Constant_shipping_address.first_name_box).send_keys(Constant_shipping_address.first_name)
    web_driver.find_element(*Constant_shipping_address.last_name_box).send_keys(Constant_shipping_address.last_name)
    web_driver.find_element(*Constant_shipping_address.street_box).send_keys(Constant_shipping_address.street_address)
    web_driver.find_element(*Constant_shipping_address.postcode_box).send_keys(Constant_shipping_address.zip_code)
    web_driver.find_element(*Constant_shipping_address.town_box).send_keys(Constant_shipping_address.town)
    web_driver.find_element(*Constant_shipping_address.save_address_button).click()

    return web_driver.find_element(*Constant_shipping_address.adress_confirmation).is_displayed()
