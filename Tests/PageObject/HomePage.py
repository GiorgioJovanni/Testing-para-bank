from Tests.PageObject.BasePage import BasePage
from Tests.PageObject.locators import BasePageLocators, AboutUsPageLocators, ServicesPageLocators, \
    ProductsAndLocationsPageLocators, AdminPagePageLocators


class HomePage(BasePage):
    def button_go_about_us(self):
        self.click_on_button(*BasePageLocators.BUTTON_ABOUT_US)
        assert self.is_element_present(*AboutUsPageLocators.LINK)

    def button_go_services(self):
        self.click_on_button(*BasePageLocators.BUTTON_SERVICES)
        assert self.is_element_present(*ServicesPageLocators.HEADER1)
        assert self.is_element_present(*ServicesPageLocators.HEADER2)
        assert self.is_element_present(*ServicesPageLocators.HEADER3)
        assert self.is_element_present(*ServicesPageLocators.HEADER4)
        assert self.is_element_present(*ServicesPageLocators.HEADER5)

    def button_go_products(self):
        self.click_on_button(*BasePageLocators.BUTTON_PRODUCTS)
        assert self.is_element_present(*ProductsAndLocationsPageLocators.HEADER)

    def button_go_locations(self):
        self.click_on_button(*BasePageLocators.BUTTON_LOCATIONS)
        assert self.is_element_present(*ProductsAndLocationsPageLocators.HEADER)

    def button_go_admin_page(self):
        self.click_on_button(*BasePageLocators.BUTTON_ADMIN_PAGE)
        assert self.is_element_present(*AdminPagePageLocators.BOARD)

    def press_the_button_register_base(self):
        self.click_on_button(*BasePageLocators.BUTTON_REGISTER)