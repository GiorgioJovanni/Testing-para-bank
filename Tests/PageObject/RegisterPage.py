import faker

from Tests.PageObject.BasePage import BasePage
from Tests.PageObject.locators import RegisterPageLocators

fake = faker.Faker()
password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()


class RegisterPage(BasePage):
    def open_register_page(self):
        self.should_be_panel()
        self.should_be_form()

    def should_be_panel(self):
        assert self.is_element_present(*RegisterPageLocators.RIGHT_PANEL), "Right panel is not present"

    def should_be_form(self):
        assert self.is_element_present(*RegisterPageLocators.CUSTOMER_FORM), "Customer form is not present"

    def add_text_in_border_first_name(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_FIRST_NAME).send_keys(first_name)

    def add_text_in_border_last_name(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_LAST_NAME).send_keys(last_name)

    def add_text_in_border_address(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_ADDRESS).send_keys('New York')

    def add_text_in_border_city(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_CITY).send_keys('New York')

    def add_text_in_border_state(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_STATE).send_keys('New York')

    def add_text_in_border_zipcode(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_ZIPCODE).send_keys('0007')

    def add_text_in_border_phone(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_PHONE).send_keys('+01234241231')

    def add_text_in_border_snn(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_SNN).send_keys('23412341234123')

    def add_text_in_border_username(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_USERNAME).send_keys(f"-1{first_name}1-")

    def add_text_in_border_password(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_PASSWORD).send_keys(password)

    def add_text_in_border_confirm(self):
        self.browser.find_element(*RegisterPageLocators.FIELD_CONFIRM).send_keys(password)

    def press_the_button_register(self):
        self.click_on_button(*RegisterPageLocators.BUTTON_REGISTER)

    def should_not_be_button_register(self):
        assert self.is_not_element_present(*RegisterPageLocators.BUTTON_REGISTER), "Button register is not disappear"

    def should_be_text_error(self):
        assert self.is_element_present(*RegisterPageLocators.TEXT_ERROR), "Text error is not present"
