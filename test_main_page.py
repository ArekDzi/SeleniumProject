from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

uzytkownik = 'l.miotk.py'
haslo = "Aut0m@ty$a$uper!"


def test_zaloguj_uzytkownika(web_driver: WebDriver):
    zakladka_account = web_driver.find_element(By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[3]/a')
    zakladka_account.click()
    user_name_box = web_driver.find_element(By.ID, '//*[@id="username"]')
    user_name_box.send_keys(uzytkownik)
    passowr_box = web_driver.find_element(By.XPATH, '//*[@id="password"]')
    passowr_box.send_keys(haslo)
    login_button = web_driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
    login_button.click()
    strona_account = web_driver.find_element(By.XPATH, '//*[@id="post-8"]/div[2]/div/p[1]').text

    assert "hello ".casefold() in strona_account.casefold()


def test_loguj_uzytkownika(web_driver: WebDriver):
    account_link = web_driver.find_element(By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[3]/a')
    account_link.click()

    username_input = web_driver.find_element(By.ID, "username")
    passowrd_input = web_driver.find_element(By.ID, "password")
    login_button = web_driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')

    username_input.send_keys(uzytkownik + "@gmail.com")
    passowrd_input.send_keys(haslo)
    login_button.click()
    hello_message = web_driver.find_element(By.XPATH, "//div[@class='woocommerce-MyAccount-content']").text

    assert "hello".casefold() in hello_message.casefold()


def test_zakup_produktu(web_driver: WebDriver):
    account_link = web_driver.find_element(By.XPATH, "//li[@class='top-account']/a")
    account_link.click()
    username_input = web_driver.find_element(By.ID, "username")
    password_input = web_driver.find_element(By.ID, "password")
    button_login = web_driver.find_element(By.XPATH, "//input[@name ='login']")

    username_input.send_keys(uzytkownik + "@gmail.com")
    password_input.send_keys(haslo)
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
