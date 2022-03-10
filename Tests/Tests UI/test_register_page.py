from Tests.PageObject.RegisterPage import RegisterPage
from Tests.PageObject.locators import BasePageLocators

base_link = "http://parabank.parasoft.com"


def test_guest_can_register(browser):
    page = RegisterPage(browser, base_link)
    page.open()
    page.click_on_button(*BasePageLocators.BUTTON_REGISTER)
    page.open_register_page()
    page.register_new_fake_user()


def test_negative_guest_can_register(browser):
    page = RegisterPage(browser, base_link)
    page.open()
    page.click_on_button(*BasePageLocators.BUTTON_REGISTER)
    page.open_register_page()
    page.negative_register_new_fake_user()


def test_guest_use_buttons_gohome_contact_aboutus_from_register_page(browser):
    page = RegisterPage(browser, base_link)
    page.open()
    page.click_on_button(*BasePageLocators.BUTTON_REGISTER)
    page.open_register_page()
    page.button_go_home()
    page.open()
    page.click_on_button(*BasePageLocators.BUTTON_REGISTER)
    page.button_go_contact()
    page.open()
    page.click_on_button(*BasePageLocators.BUTTON_REGISTER)
    page.button_go_aboutus()
