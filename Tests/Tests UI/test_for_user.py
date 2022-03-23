import time

from Tests.PageObject.Constants import Data


def test_guest_can_reg(page_register):
    page_register.button_go_to_register.click()
    assert page_register.should_be_panel, "Right panel is not present"
    assert page_register.should_be_form, "Customer form is not present"
    page_register.add_first_name.send_keys(Data.first_name)
    page_register.add_last_name.send_keys(Data.last_name)
    page_register.add_address.send_keys(Data.address)
    page_register.add_city.send_keys(Data.address)
    page_register.add_state.send_keys(Data.address)
    page_register.add_zipcode.send_keys(Data.zipcode)
    page_register.add_phone.send_keys(Data.phone)
    page_register.add_snn.send_keys(Data.snn)
    page_register.add_username.send_keys(f"{Data.first_name + Data.random_number}")
    page_register.add_password.send_keys(Data.password)
    page_register.add_confirm.send_keys(Data.password)
    page_register.button_register.click()
    assert page_register.should_not_be_button_register, "Button register is not disappear"
    time.sleep(999)


def test_user_can_go_new_account(page_register):
    page_register.button_open_new_account.click()
    assert page_register.should_be_slider_type, "Slider type is not present"
    assert page_register.should_be_slider_from_account, "Slider from account is not present"
    assert page_register.should_be_button_open_new_account, 'Button open new account account is not present'


