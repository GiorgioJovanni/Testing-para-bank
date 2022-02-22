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
    pass
