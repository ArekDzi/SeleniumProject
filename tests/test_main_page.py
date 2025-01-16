from selenium.webdriver.remote.webdriver import WebDriver
from pages import main_page


def test_most_wanted_tab(web_driver: WebDriver):
    assert main_page.most_wanted_initialization(web_driver).casefold() ==\
           main_page.ConstantMostWanted.most_wanted_txt.casefold()


def test_product_purchase(web_driver: WebDriver):
    little_black_top = main_page.buy_product(web_driver)
    assert little_black_top == main_page.ConstantBuyProduct.product_little_black_top.casefold(), \
        f"Product title ({little_black_top}) is not equal to {main_page.ConstantBuyProduct.product_little_black_top}"

"""
def test_newsletter_subscription(web_driver: WebDriver):
    subscription_action = main_page.newsletter_subscribe(web_driver)
    assert not main_page.ConstantNewsletter.confirmation_text.casefold() in subscription_action.casefold(), \
        f"Confirmation text ({subscription_action}) is not equal {main_page.ConstantNewsletter.confirmation_text}"
"""

