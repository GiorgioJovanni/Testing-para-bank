from Tests.PageObject.BasePage import BasePage
from Tests.PageObject.locators import BasePageLocators, AboutUsPageLocators, ServicesPageLocators, \
    ProductsAndLocationsPageLocators, AdminPagePageLocators


class HomePage(BasePage):
    @property
    def button_go_home(self):
        return self.browser.find_element(*BasePageLocators.BUTTON_GO_BASE_PAGE)

    @property
    def button_go_aboutus(self):
        return self.browser.find_element(*BasePageLocators.BUTTON_GO_ABOUTUS_PAGE)

    @property
    def button_go_contact(self):
        return self.browser.find_element(*BasePageLocators.BUTTON_GO_CONTACT_PAGE)

    @property
    def button_go_about_us(self):
        return self.browser.find_element(*BasePageLocators.BUTTON_ABOUT_US)

    @property
    def button_go_services(self):
        return self.browser.find_element(*BasePageLocators.BUTTON_SERVICES)

    @property
    def button_go_products(self):
        return self.browser.find_element(*BasePageLocators.BUTTON_PRODUCTS)

    @property
    def button_go_locations(self):
        return self.browser.find_element(*BasePageLocators.BUTTON_LOCATIONS)

    @property
    def button_go_admin_page(self):
        return self.browser.find_element(*BasePageLocators.BUTTON_ADMIN_PAGE)

    @property
    def press_the_button_register_base(self):
        return self.browser.find_element(*BasePageLocators.BUTTON_REGISTER)

    @property
    def should_be_image_go_home(self):
        return self.is_element_present(*BasePageLocators.IMAGE)

    @property
    def should_be_link_go_aboutus(self):
        return self.is_element_present(*BasePageLocators.LINK)

    @property
    def should_be_message_go_contact(self):
        return self.is_element_present(*BasePageLocators.MESSAGE)

    @property
    def should_be_link_go_about_us(self):
        return self.is_element_present(*AboutUsPageLocators.LINK)

    @property
    def should_be_soap_go_services(self):
        return self.is_element_present(*ServicesPageLocators.HEADER_AVAILABLE_BOOKSTORE_SOAP)

    @property
    def should_be_bookstore_go_services(self):
        return self.is_element_present(*ServicesPageLocators.HEADER_BOOKSTORE)

    @property
    def should_be_parabank_soap_go_services(self):
        return self.is_element_present(*ServicesPageLocators.HEADER_PARABANK_SOAP)

    @property
    def should_be_parabank_go_services(self):
        return self.is_element_present(*ServicesPageLocators.HEADER_PARABANK)

    @property
    def should_be_restful_go_services(self):
        return self.is_element_present(*ServicesPageLocators.HEADER_RESTFUL)

    @property
    def should_be_logo_go_products(self):
        return self.is_element_present(*ProductsAndLocationsPageLocators.LOGO)

    @property
    def should_be_logo_go_locations(self):
        return self.is_element_present(*ProductsAndLocationsPageLocators.LOGO)

    @property
    def should_be_header_go_admin_page(self):
        return self.is_element_present(*AdminPagePageLocators.BOARD)
