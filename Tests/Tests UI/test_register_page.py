import time
from random import randint

from Tests.PageObject.RegisterPage import RegisterPage
from Tests.PageObject.locators import BasePageLocators


def test_guest_can_register(browser):
    link = "http://parabank.parasoft.com"
    page = RegisterPage(browser, link)
    page.open()
    page.click_on_button(*BasePageLocators.BUTTON_REGISTER)
    page.guest_can_go_to_register_page()
    page.register_new_fake_user()


def test_register(browser):
    # id_account = randint(100000, 999999)
    # link = f"https://parabank.parasoft.com/parabank/services/bank/accounts/{id_account}"
    # page = RegisterPage(browser, link)
    # page.open()
    # text = browser.find_element(*BasePageLocators.TEXT).get_attribute('textContent')
    i = 0
    while i < 20:
        id_account = randint(10000, 99999)
        link = f"https://parabank.parasoft.com/parabank/services/bank/accounts/{id_account}"
        page = RegisterPage(browser, link)
        page.open()
        i += 1

    """
    Could not find account #85672
    body > pre
    """