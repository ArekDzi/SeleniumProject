import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages import my_account_page
from locators.locators import ConstantMostWanted, ConstantBuyProduct, ConstantNewsletter


def most_wanted_initialization(web_driver: WebDriver) -> str:
    web_driver.find_element(*ConstantMostWanted.zakladka_most_wanted).click()
    return web_driver.find_element(*ConstantMostWanted.naglowek_most_wanted).text


def buy_product(web_driver: WebDriver) -> str:
    my_account_page.login_user(web_driver)
    web_driver.find_element(*ConstantBuyProduct.most_wanted_tap).click()
    web_driver.find_element(*ConstantBuyProduct.add_to_cart_button).click()
    wait = WebDriverWait(web_driver, 10)
    time.sleep(2) # it is needed to slow down
    web_driver.find_element(*ConstantBuyProduct.cart_button).click()
    product_name = web_driver.find_element(*ConstantBuyProduct.product_box).text

    return product_name.casefold()


def newsletter_subscribe(web_driver: WebDriver) -> str:
    name_box = web_driver.find_element(*ConstantNewsletter.input_name_box)
    name_box.click()
    name_box.send_keys(ConstantNewsletter.newsletter_name)
    mail_box = web_driver.find_element(*ConstantNewsletter.input_mail_box)
    mail_box.click()
    mail_box.send_keys(*ConstantNewsletter.newsletter_mail)
    web_driver.find_element(*ConstantNewsletter.subscribe_button).click()

    WebDriverWait(web_driver, 4).until(ec.text_to_be_present_in_element(ConstantNewsletter.confirmation_text_selector,
                                                                        'Subscribed'))

    text_subscribe = web_driver.find_element(*ConstantNewsletter.confirmation_text_selector).text
    return text_subscribe
