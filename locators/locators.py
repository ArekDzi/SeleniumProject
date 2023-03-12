from typing import Tuple
from selenium.webdriver.common.by import By


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


class ConstantNewsletter:
    newsletter_name: str = 'adsdada'
    newsletter_mail: str = "assd@gmail.com"
    input_name_box: str = (By.ID, 'es_txt_name')
    input_mail_box: str = (By.ID, 'es_txt_email')
    subscribe_button: str = (By.ID, 'es_txt_button')
    confirmation_text_selector: str = (By.ID, 'es_msg')
    confirmation_text: str = 'Successfully Subscribed'


class ConstantUserAbcd:
    haslo: str = "Abcd123456789!"
    uzytkownik: str = "abcdf@gmail.com"


class ConstantUserAutomaty:
    login: str = 'l.miotk.py'
    password: str = "Aut0m@ty$a$uper!"


class ConstantMostWanted:
    zakladka_most_wanted: str = (By.XPATH, '//*[@id="menu-item-128"]/a')
    naglowek_most_wanted: str = (By.XPATH, '//*[@id="page"]/div/div/div[2]/div/h1')
    most_wanted_txt: str = "most wanted"


class ConstantBuyProduct:
    shop_tab: str = (By.ID, "menu-item-142")
    add_to_cart_button: str = (By.XPATH, "//a[@data-product_id='17']")
    cart_button: str = (By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[2]/a')
    product_box: str = (By.XPATH, '//*[@id="post-6"]/div[2]/form/table/tbody/tr[1]/td[3]')
    product_little_black_top: str = "Little Black Top"