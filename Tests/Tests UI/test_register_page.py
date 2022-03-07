from Tests.PageObject.RegisterPage import RegisterPage
from Tests.PageObject.locators import BasePageLocators


def test_guest_can_register(browser):
    link = "http://parabank.parasoft.com"
    page = RegisterPage(browser, link)
    page.open()
    page.click_on_button(*BasePageLocators.BUTTON_REGISTER)
    page.guest_can_go_to_register_page()
    page.register_new_fake_user()


def test_guest_use_buttons_gohome_contact_aboutus_from_register_page(browser):
    link = "http://parabank.parasoft.com"
    page = RegisterPage(browser, link)
    page.open()
    page.click_on_button(*BasePageLocators.BUTTON_REGISTER)
    page.guest_can_go_to_register_page()
    page.button_go_home_is_working()
    page.open()
    page.click_on_button(*BasePageLocators.BUTTON_REGISTER)
    page.button_go_contact_is_working()
    page.open()
    page.click_on_button(*BasePageLocators.BUTTON_REGISTER)
    page.button_go_aboutus_is_working()
