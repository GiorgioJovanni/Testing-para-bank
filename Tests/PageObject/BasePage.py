from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.PageObject.locators import BasePageLocators, ServicesPageLocators, AboutUsPageLocators, \
    ProductsAndLocationsPageLocators, AdminPagePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def click_on_button(self, how, what):
        self.browser.find_element(how, what).click()

    def button_go_home(self):
        self.click_on_button(*BasePageLocators.BUTTON_GO_BASE_PAGE)
        assert self.is_element_present(*BasePageLocators.IMAGE)

    def button_go_aboutus(self):
        self.click_on_button(*BasePageLocators.BUTTON_GO_ABOUTUS_PAGE)
        assert self.is_element_present(*BasePageLocators.LINK)

    def button_go_contact(self):
        self.click_on_button(*BasePageLocators.BUTTON_GO_CONTACT_PAGE)
        assert self.is_element_present(*BasePageLocators.MESSAGE)

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
