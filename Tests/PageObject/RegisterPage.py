from Tests.PageObject.BasePage import BasePage
from Tests.PageObject.locators import RegisterPageLocators, BasePageLocators


class RegisterPage(BasePage):

    def should_be_panel(self):
        assert self.is_element_present(*RegisterPageLocators.RIGHT_PANEL), "Right panel is not present"

    def should_be_form(self):
        assert self.is_element_present(*RegisterPageLocators.CUSTOMER_FORM), "Customer form is not present"

    def add_first_name(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_FIRST_NAME)

    def add_last_name(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_LAST_NAME)

    def add_address(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_ADDRESS)

    def add_city(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_CITY)

    def add_state(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_STATE)

    def add_zipcode(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_ZIPCODE)

    def add_phone(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_PHONE)

    def add_snn(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_SNN)

    def add_username(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_USERNAME)

    def add_password(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_PASSWORD)

    def add_confirm(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_CONFIRM)

    def press_the_button_register(self):
        self.click_on_button(*RegisterPageLocators.BUTTON_REGISTER)

    def press_the_button_go_to_register(self):
        self.click_on_button(*BasePageLocators.BUTTON_REGISTER)

    def should_not_be_button_register(self):
        assert self.is_not_element_present(*RegisterPageLocators.BUTTON_REGISTER), "Button register is not disappear"

    def should_be_text_error_address(self):
        assert self.is_element_present(*RegisterPageLocators.TEXT_ERROR_ADDRESS), "Text error is not present"

    def should_be_text_error_city(self):
        assert self.is_element_present(*RegisterPageLocators.TEXT_ERROR_CITY), "Text error is not present"

    def should_be_text_error_state(self):
        assert self.is_element_present(*RegisterPageLocators.TEXT_ERROR_STATE), "Text error is not present"

    def should_be_text_error_zipcode(self):
        assert self.is_element_present(*RegisterPageLocators.TEXT_ERROR_ZIPCODE), "Text error is not present"
