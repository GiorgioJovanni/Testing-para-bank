from Tests.PageObject.BasePage import BasePage
from Tests.PageObject.Constants import EndPoint
from Tests.PageObject.locators import BasePageLocators


def test_guest_use_buttons_gohome_contact_aboutus_from_register_page(browser):
    page = BasePage(browser, EndPoint.base_link)
    page.open()
    page.button_go_home()
    page.open()
    page.click_on_button(*BasePageLocators.BUTTON_REGISTER)
    page.button_go_contact()
    page.open()
    page.click_on_button(*BasePageLocators.BUTTON_REGISTER)
    page.button_go_aboutus()


class TestUpMenu:
    def test_guest_use_button_about_us(self, browser):
        page = BasePage(browser, EndPoint.base_link)
        page.open()
        page.button_go_about_us()

    def test_guest_use_button_services(self, browser):
        page = BasePage(browser, EndPoint.base_link)
        page.open()
        page.button_go_services()

    def test_guest_use_button_products(self, browser):
        page = BasePage(browser, EndPoint.base_link)
        page.open()
        page.button_go_products()

    def test_guest_use_button_locations(self, browser):
        page = BasePage(browser, EndPoint.base_link)
        page.open()
        page.button_go_locations()

    def test_guest_use_button_admin_page(self, browser):
        page = BasePage(browser, EndPoint.base_link)
        page.open()
        page.button_go_admin_page()

