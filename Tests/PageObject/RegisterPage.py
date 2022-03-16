from Tests.PageObject.HomePage import HomePage
from Tests.PageObject.locators import RegisterPageLocators, BasePageLocators


class RegisterPage(HomePage):

    @property
    def add_first_name(self):
        return self.browser.find_element(*RegisterPageLocators.FIELD_FIRST_NAME)

    @property
    def add_last_name(self):
        return self.browser.find_element(*RegisterPageLocators.FIELD_LAST_NAME)

    @property
    def add_address(self):
        return self.browser.find_element(*RegisterPageLocators.FIELD_ADDRESS)

    @property
    def add_city(self):
        return self.browser.find_element(*RegisterPageLocators.FIELD_CITY)

    @property
    def add_state(self):
        return self.browser.find_element(*RegisterPageLocators.FIELD_STATE)

    @property
    def add_zipcode(self):
        return self.browser.find_element(*RegisterPageLocators.FIELD_ZIPCODE)

    @property
    def add_phone(self):
        return self.browser.find_element(*RegisterPageLocators.FIELD_PHONE)

    @property
    def add_snn(self):
        return self.browser.find_element(*RegisterPageLocators.FIELD_SNN)

    @property
    def add_username(self):
        return self.browser.find_element(*RegisterPageLocators.FIELD_USERNAME)

    @property
    def add_password(self):
        return self.browser.find_element(*RegisterPageLocators.FIELD_PASSWORD)

    @property
    def add_confirm(self):
        return self.browser.find_element(*RegisterPageLocators.FIELD_CONFIRM)

    @property
    def button_go_to_register(self):
        return self.browser.find_element(*BasePageLocators.BUTTON_REGISTER)

    @property
    def button_register(self):
        return self.browser.find_element(*RegisterPageLocators.BUTTON_REGISTER)

    @property
    def button_log_out(self):
        return self.browser.find_element(*RegisterPageLocators.BUTTON_LOG_OUT)

    def should_be_panel(self):
        assert self.is_element_present(*RegisterPageLocators.RIGHT_PANEL), "Right panel is not present"

    def should_be_form(self):
        assert self.is_element_present(*RegisterPageLocators.CUSTOMER_FORM), "Customer form is not present"

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
