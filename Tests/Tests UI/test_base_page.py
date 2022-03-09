from Tests.PageObject.BasePage import BasePage
from Tests.PageObject.locators import BasePageLocators

base_link = "http://parabank.parasoft.com"


def test_guest_use_buttons_gohome_contact_aboutus_from_register_page(browser):
    page = BasePage(browser, base_link)
    page.open()
    page.button_go_home_is_working()
    page.open()
    page.click_on_button(*BasePageLocators.BUTTON_REGISTER)
    page.button_go_contact_is_working()
    page.open()
    page.click_on_button(*BasePageLocators.BUTTON_REGISTER)
    page.button_go_aboutus_is_working()


class TestUpMenu:
    def test_guest_use_button_about_us(self, browser):
        page = BasePage(browser, base_link)
        page.open()
        page.button_go_about_us_is_working()

    def test_guest_use_button_services(self, browser):
        page = BasePage(browser, base_link)
        page.open()
        page.button_go_services_is_working()

    def test_guest_use_button_products(self, browser):
        page = BasePage(browser, base_link)
        page.open()
        page.button_go_products_is_working()

    def test_guest_use_button_locations(self, browser):
        page = BasePage(browser, base_link)
        page.open()
        page.button_go_locations_is_working()

    def test_guest_use_button_admin_page(self, browser):
        page = BasePage(browser, base_link)
        page.open()
        page.button_go_admin_page_is_working()

