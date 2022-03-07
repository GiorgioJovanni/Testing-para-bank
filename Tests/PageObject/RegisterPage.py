import faker

from Tests.PageObject.BasePage import BasePage
from Tests.PageObject.locators import RegisterPageLocators


class RegisterPage(BasePage):
    def guest_can_go_to_register_page(self):
        self.should_be_customer_form()

    def should_be_customer_form(self):
        assert self.is_element_present(*RegisterPageLocators.RIGHT_PANEL), "Right panel is not present"
        assert self.is_element_present(*RegisterPageLocators.CUSTOMER_FORM), "Customer form is not present"

    def register_new_fake_user(self):
        fake = faker.Faker()
        password = fake.password()
        first_name = fake.first_name()
        last_name = fake.last_name()
        self.browser.find_element(*RegisterPageLocators.FIELD_FIRST_NAME).send_keys(first_name)
        self.browser.find_element(*RegisterPageLocators.FIELD_LAST_NAME).send_keys(last_name)
        self.browser.find_element(*RegisterPageLocators.FIELD_ADDRESS).send_keys('New York')
        self.browser.find_element(*RegisterPageLocators.FIELD_CITY).send_keys('New York')
        self.browser.find_element(*RegisterPageLocators.FIELD_STATE).send_keys('New York')
        self.browser.find_element(*RegisterPageLocators.FIELD_ZIPCODE).send_keys('0007')
        self.browser.find_element(*RegisterPageLocators.FIELD_PHONE).send_keys('+01234241231')
        self.browser.find_element(*RegisterPageLocators.FIELD_SNN).send_keys('23412341234123')
        self.browser.find_element(*RegisterPageLocators.FIELD_USERNAME).send_keys(f"-1{first_name}1-")
        self.browser.find_element(*RegisterPageLocators.FIELD_PASSWORD).send_keys(password)
        self.browser.find_element(*RegisterPageLocators.FIELD_CONFIRM).send_keys(password)
        self.click_on_button(*RegisterPageLocators.BUTTON_REGISTER)
        assert self.is_element_present(*RegisterPageLocators.TEXT_WELCOME), "Text welcome is not present"

