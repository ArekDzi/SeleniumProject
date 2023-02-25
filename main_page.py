from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import my_account_page


class Constant_newsletter:
    newsletter_name = 'adsdada'
    newsletter_mail = "assd@gmail.com"
    input_name_box = (By.ID, 'es_txt_name')
    input_mail_box = (By.ID, 'es_txt_email')
    subscribe_button = (By.ID, 'es_txt_button')
    confirmation_text_selector = (By.ID, 'es_msg')
    confirmation_text = 'Successfully Subscribed'

class Constant_user_abcd:
    haslo = "Abcd123456789!"
    uzytkownik = "abcdf@gmail.com"


class Constant_user_automaty:
    login = 'l.miotk.py'
    password = "Aut0m@ty$a$uper!"


class Cosntant_most_wnated:
    zakladka_most_wanted = (By.XPATH, '//*[@id="menu-item-128"]/a')
    naglowek_most_wanted = (By.XPATH, '//*[@id="page"]/div/div/div[2]/div/h1')
    most_wanted_txt = "most wanted"


class Constant_Buy_product:
    shop_tab = (By.ID, "menu-item-142")
    add_to_cart_button = (By.XPATH, "//a[@data-product_id='17']")
    cart_button = (By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[2]/a')
    product_box = (By.XPATH, '//*[@id="post-6"]/div[2]/form/table/tbody/tr[1]/td[3]')
    product_little_black_top = "Little Black Top"


def most_wanted_initialization(web_driver: WebDriver):
    web_driver.find_element(*Cosntant_most_wnated.zakladka_most_wanted).click()
    return web_driver.find_element(*Cosntant_most_wnated.naglowek_most_wanted).text


def buy_product(web_driver: WebDriver):
    my_account_page.login_user(web_driver)
    web_driver.find_element(*Constant_Buy_product.shop_tab).click()
    web_driver.find_element(*Constant_Buy_product.add_to_cart_button).click()
    web_driver.find_element(*Constant_Buy_product.cart_button).click()
    product_name = web_driver.find_element(*Constant_Buy_product.product_box).text

    return product_name.casefold()


def newsletter_subscribe(web_driver: WebDriver,):
    name_box = web_driver.find_element(*Constant_newsletter.input_name_box)
    name_box.click()
    name_box.send_keys(Constant_newsletter.newsletter_name)
    mail_box = web_driver.find_element(*Constant_newsletter.input_mail_box)
    mail_box.click()
    mail_box.send_keys(*Constant_newsletter.newsletter_mail)
    web_driver.find_element(*Constant_newsletter.subscribe_button).click()

    WebDriverWait(web_driver, 4).until(ec.text_to_be_present_in_element(Constant_newsletter.confirmation_text_selector,
                                                                        'Subscribed'))

    text_subscribe = web_driver.find_element(*Constant_newsletter.confirmation_text_selector).text
    return text_subscribe


