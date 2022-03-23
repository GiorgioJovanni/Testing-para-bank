from selenium.webdriver import Keys

from base_page import BasePage
from locators import CustomerLookupPageLocators
from locators import CustomerLookupPageLocatorsData
from conftest import browser


class CustomerLookupPage(BasePage):
    def should_be_lookup_page_url(browser):
        "lookup" in browser.current_url
        assert True

    def should_be_lookup_page_form(self):
        self.is_element_present(*CustomerLookupPageLocators.LOOKUP_PAGE_FORM)
        assert True

    def should_be_lookup_page_form_data(self):
        self.is_element_present(*CustomerLookupPageLocatorsData.FIRST_NAME)
        self.is_element_present(*CustomerLookupPageLocatorsData.LAST_NAME)
        self.is_element_present(*CustomerLookupPageLocatorsData.ADDRESS)
        self.is_element_present(*CustomerLookupPageLocatorsData.CITY)
        self.is_element_present(*CustomerLookupPageLocatorsData.STATE)
        self.is_element_present(*CustomerLookupPageLocatorsData.ZIP_CODE)
        self.is_element_present(*CustomerLookupPageLocatorsData.SSN)
        assert True

    def account_validate(self):
        element = self.find_element(*CustomerLookupPageLocatorsData.FIRST_NAME)
        element.send_keys('First Name')

        element = self.browser.find_element(*CustomerLookupPageLocatorsData.LAST_NAME)
        element.send_keys('Last Name')

        element = self.browser.find_element(*CustomerLookupPageLocatorsData.ADDRESS)
        element.send_keys('Address')

        element = self.browser.find_element(*CustomerLookupPageLocatorsData.CITY)
        element.send_keys('City')

        element = self.browser.find_element(*CustomerLookupPageLocatorsData.STATE)
        element.send_keys('State')

        element = self.browser.find_element(*CustomerLookupPageLocatorsData.ZIP_CODE)
        element.send_keys('12345')

        element = self.browser.find_element(*CustomerLookupPageLocatorsData.SSN)
        element.send_keys('1234567890')
        element.send_keys(Keys.RETURN)

        assert "Your login information was located successfully. You are now logged in." in browser.page_source, \
            'The customer information provided could not be found.'
