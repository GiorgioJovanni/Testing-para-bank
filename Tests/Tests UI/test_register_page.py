import time

from Tests.PageObject.Constants import EndPoint
from Tests.PageObject.RegisterPage import RegisterPage


class TestPositive:
    def test_guest_can_register(self, browser):
        page = RegisterPage(browser, EndPoint.base_link)
        page.open()
        page.press_the_button_go_to_register()
        page.should_be_panel()
        page.should_be_form()
        page.add_first_name()
        page.add_last_name()
        page.add_address()
        page.add_city()
        page.add_state()
        page.add_zipcode()
        page.add_phone()
        page.add_snn()
        page.add_username()
        page.add_password()
        page.add_confirm()
        page.press_the_button_register()
        page.should_not_be_button_register()

    def test_guest_use_buttons_gohome_contact_aboutus_from_register_page(self, browser):
        page = RegisterPage(browser, EndPoint.base_link)
        page.open()
        page.press_the_button_go_to_register()
        page.should_be_panel()
        page.should_be_form()
        page.button_go_home()
        page.open()
        page.press_the_button_go_to_register()
        page.button_go_contact()
        page.open()
        page.press_the_button_go_to_register()
        page.button_go_aboutus()


class TestNegative:
    def test_negative_guest_can_register_address(self, browser):
        page = RegisterPage(browser, EndPoint.base_link)
        page.open()
        page.press_the_button_go_to_register()
        page.should_be_panel()
        page.should_be_form()
        page.add_first_name()
        page.add_last_name()
        page.add_city()
        page.add_state()
        page.add_zipcode()
        page.add_phone()
        page.add_snn()
        page.add_username()
        page.add_password()
        page.add_confirm()
        page.press_the_button_register()
        page.should_be_text_error_address()

    def test_negative_guest_can_register_city(self, browser):
        page = RegisterPage(browser, EndPoint.base_link)
        page.open()
        page.press_the_button_go_to_register()
        page.should_be_panel()
        page.should_be_form()
        page.add_first_name()
        page.add_last_name()
        page.add_address()
        page.add_state()
        page.add_zipcode()
        page.add_phone()
        page.add_snn()
        page.add_username()
        page.add_password()
        page.add_confirm()
        page.press_the_button_register()
        page.should_be_text_error_city()

    def test_negative_guest_can_register_state(self, browser):
        page = RegisterPage(browser, EndPoint.base_link)
        page.open()
        page.press_the_button_go_to_register()
        page.should_be_panel()
        page.should_be_form()
        page.add_first_name()
        page.add_last_name()
        page.add_address()
        page.add_city()
        page.add_zipcode()
        page.add_phone()
        page.add_snn()
        page.add_username()
        page.add_password()
        page.add_confirm()
        page.press_the_button_register()
        page.should_be_text_error_state()

    def test_negative_guest_can_register_zipcode(self, browser):
        page = RegisterPage(browser, EndPoint.base_link)
        page.open()
        page.press_the_button_go_to_register()
        page.should_be_panel()
        page.should_be_form()
        page.add_first_name()
        page.add_last_name()
        page.add_address()
        page.add_city()
        page.add_state()
        page.add_phone()
        page.add_snn()
        page.add_username()
        page.add_password()
        page.add_confirm()
        page.press_the_button_register()
        page.should_be_text_error_zipcode()
