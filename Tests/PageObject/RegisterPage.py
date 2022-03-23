from Tests.PageObject.HomePage import HomePage
from Tests.PageObject.locators import RegisterPageLocators, HomePageLocators, UserPageLocators


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
        return self.browser.find_element(*HomePageLocators.BUTTON_REGISTER)

    @property
    def button_register(self):
        return self.browser.find_element(*RegisterPageLocators.BUTTON_REGISTER)

    @property
    def button_log_out(self):
        return self.browser.find_element(*RegisterPageLocators.BUTTON_LOG_OUT)

    @property
    def should_be_panel(self):
        return self.is_element_present(*RegisterPageLocators.RIGHT_PANEL)

    @property
    def should_be_form(self):
        return self.is_element_present(*RegisterPageLocators.CUSTOMER_FORM)

    @property
    def should_not_be_button_register(self):
        return self.is_not_element_present(*RegisterPageLocators.BUTTON_REGISTER)

    @property
    def should_be_text_error_address(self):
        return self.is_element_present(*RegisterPageLocators.TEXT_ERROR_ADDRESS)

    @property
    def should_be_text_error_city(self):
        return self.is_element_present(*RegisterPageLocators.TEXT_ERROR_CITY)

    @property
    def should_be_text_error_state(self):
        return self.is_element_present(*RegisterPageLocators.TEXT_ERROR_STATE)

    @property
    def should_be_text_error_zipcode(self):
        return self.is_element_present(*RegisterPageLocators.TEXT_ERROR_ZIPCODE)

    @property
    def button_open_new_account(self):
        return self.browser.find_element(*UserPageLocators.OPEN_NEW_ACCOUNT)

    @property
    def should_be_slider_type(self):
        return self.is_element_present(*UserPageLocators.TYPE)

    @property
    def slider_type(self):
        return self.browser.find_element(*UserPageLocators.TYPE)

    @property
    def should_be_slider_from_account(self):
        return self.is_element_present(*UserPageLocators.FROM_ACCOUNT)

    @property
    def slider_from_account(self):
        return self.browser.find_element(*UserPageLocators.FROM_ACCOUNT)

    @property
    def should_be_button_open_new_account(self):
        return self.is_element_present(*UserPageLocators.BUTTON_OPEN_NEW_ACCOUNT)

    @property
    def button_overview(self):
        return self.browser.find_element(*UserPageLocators.OVERVIEW)

    @property
    def button_transfer_funds(self):
        return self.browser.find_element(*UserPageLocators.TRANSFER_FUNDS)
