from Tests.PageObject.BasePage import BasePage
from Tests.PageObject.locators import RegisterPageLocators


class RegisterPage(BasePage):
    def guest_can_go_to_register_page(self):
        self.should_be_customer_form()

    def should_be_customer_form(self):
        self.is_element_present(RegisterPageLocators.CUSTOMER_FORM)
