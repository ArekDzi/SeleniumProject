from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Constant_newsleeter:
    newsletter_name = 'adsdada'
    newsletter_mail = "assd@gmail.com"


class Constant_user_abcd:
    haslo = "Abcd123456789!"
    uzytkownik = "abcdf@gmail.com"


class Constant_user_automaty:
    login = 'l.miotk.py'
    password = "Aut0m@ty$a$uper!"


def test_tab_most_wanted(web_driver: WebDriver):
    zakladka_most_wanted = web_driver.find_element(By.XPATH, '//*[@id="menu-item-128"]/a')
    zakladka_most_wanted.click()
    naglowek_most_wanted = web_driver.find_element(By.XPATH, '//*[@id="page"]/div/div/div[2]/div/h1').text

    assert naglowek_most_wanted.casefold() == "most wanted".casefold()


def test_zaloguj_uzytkownika(web_driver: WebDriver):
    temp_user = Constant_user_abcd

    zakladka_account = web_driver.find_element(By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[3]/a')
    zakladka_account.click()
    user_name_box = web_driver.find_element(By.ID, 'username')
    user_name_box.send_keys(temp_user.uzytkownik)
    passowr_box = web_driver.find_element(By.XPATH, '//*[@id="password"]')
    passowr_box.send_keys(temp_user.haslo)
    login_button = web_driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
    login_button.click()
    strona_account = web_driver.find_element(By.XPATH, '//*[@id="post-8"]/div[2]/div/p[1]').text

    assert "hello ".casefold() in strona_account.casefold()


def test_loguj_uzytkownika(web_driver: WebDriver):
    temp_user = Constant_user_abcd

    account_link = web_driver.find_element(By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[3]/a')
    account_link.click()

    username_input = web_driver.find_element(By.ID, "username")
    passowrd_input = web_driver.find_element(By.ID, "password")
    login_button = web_driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')

    username_input.send_keys(temp_user.uzytkownik + "@gmail.com")
    passowrd_input.send_keys(temp_user.haslo)
    login_button.click()
    hello_message = web_driver.find_element(By.XPATH, "//div[@class='woocommerce-MyAccount-content']").text

    assert "hello".casefold() in hello_message.casefold()


def test_zakup_produktu(web_driver: WebDriver):
    temp_user = Constant_user_automaty
    account_link = web_driver.find_element(By.XPATH, "//li[@class='top-account']/a")
    account_link.click()
    username_input = web_driver.find_element(By.ID, "username")
    password_input = web_driver.find_element(By.ID, "password")
    button_login = web_driver.find_element(By.XPATH, "//input[@name ='login']")

    username_input.send_keys(temp_user.login + "@gmail.com")
    password_input.send_keys(temp_user.password)
    button_login.click()
    sklep_link = web_driver.find_element(By.ID, "menu-item-142")
    sklep_link.click()
    add_to_cart_button = web_driver.find_element(By.XPATH, "//a[@data-product_id='17']")
    add_to_cart_button.click()
    cart_button = web_driver.find_element(By.XPATH, f'//*/li[@class="top-cart"]/a')
    cart_button.click()
    my_cart = web_driver.find_element(By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[2]/a')
    my_cart.click()
    dodany_produkt = web_driver.find_element(By.XPATH, '//*[@id="post-6"]/div[2]/form/table/tbody/tr[1]/td[3]/a').text

    assert dodany_produkt.casefold() == 'little black top'.casefold(), "cos nie tak"


def test_newsletter(web_driver: WebDriver):
    temp_newsletter = Constant_newsleeter
    input_name_box = web_driver.find_element(By.ID, 'es_txt_name')
    input_name_box.click()
    input_name_box.send_keys(temp_newsletter.newsletter_name)

    input_mail_box = web_driver.find_element(By.ID, 'es_txt_email')
    input_mail_box.click()
    input_mail_box.send_keys(temp_newsletter.newsletter_mail)

    web_driver.find_element(By.ID, 'es_txt_button').click()

    WebDriverWait(web_driver, 4).until(ec.text_to_be_present_in_element((By.ID, 'es_msg'), 'Subscribed'))
    text_subscribe = web_driver.find_element(By.ID, 'es_msg')

    assert text_subscribe.text.casefold() == "Successfully Subscribed.".casefold(), "nie jest ok"
