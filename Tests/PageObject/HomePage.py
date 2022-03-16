from Tests.PageObject.BasePage import BasePage
from Tests.PageObject.locators import BasePageLocators, AboutUsPageLocators, ServicesPageLocators, \
    ProductsAndLocationsPageLocators, AdminPagePageLocators


class HomePage(BasePage):
    def button_go_home(self):
        self.browser.find_element(*BasePageLocators.BUTTON_GO_BASE_PAGE).click()
        assert self.is_element_present(*BasePageLocators.IMAGE)

    def button_go_aboutus(self):
        self.browser.find_element(*BasePageLocators.BUTTON_GO_ABOUTUS_PAGE).click()
        assert self.is_element_present(*BasePageLocators.LINK)

    def button_go_contact(self):
        self.browser.find_element(*BasePageLocators.BUTTON_GO_CONTACT_PAGE).click()
        assert self.is_element_present(*BasePageLocators.MESSAGE)

    def button_go_about_us(self):
        self.browser.find_element(*BasePageLocators.BUTTON_ABOUT_US).click()
        assert self.is_element_present(*AboutUsPageLocators.LINK)

    def button_go_services(self):
        self.browser.find_element(*BasePageLocators.BUTTON_SERVICES).click()
        assert self.is_element_present(*ServicesPageLocators.HEADER1)
        assert self.is_element_present(*ServicesPageLocators.HEADER2)
        assert self.is_element_present(*ServicesPageLocators.HEADER3)
        assert self.is_element_present(*ServicesPageLocators.HEADER4)
        assert self.is_element_present(*ServicesPageLocators.HEADER5)

    def button_go_products(self):
        self.browser.find_element(*BasePageLocators.BUTTON_PRODUCTS).click()
        assert self.is_element_present(*ProductsAndLocationsPageLocators.HEADER)

    def button_go_locations(self):
        self.browser.find_element(*BasePageLocators.BUTTON_LOCATIONS).click()
        assert self.is_element_present(*ProductsAndLocationsPageLocators.HEADER)

    def button_go_admin_page(self):
        self.browser.find_element(*BasePageLocators.BUTTON_ADMIN_PAGE).click()
        assert self.is_element_present(*AdminPagePageLocators.BOARD)

    def press_the_button_register_base(self):
        self.browser.find_element(*BasePageLocators.BUTTON_REGISTER).click()
