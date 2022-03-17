from Tests.PageObject.Constants import Data


def test_guest_can_register(page_register):
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
    page_register.button_log_out.click()
    assert page_register.should_be_on_home_page, "Image on home page is not present"


def test_guest_use_buttons_gohome_contact_aboutus_from_register_page(page_register):
    page_register.button_go_to_register.click()
    assert page_register.should_be_panel, "Right panel is not present"
    assert page_register.should_be_form, "Customer form is not present"
    page_register.button_go_home.click()
    assert page_register.should_be_image_go_home, "Image on home page is not present"
    page_register.open()
    page_register.button_go_to_register.click()
    page_register.button_go_contact.click()
    assert page_register.should_be_message_go_contact, "Message go contact is not present"
    page_register.open()
    page_register.button_go_to_register.click()
    page_register.button_go_aboutus.click()
    assert page_register.should_be_link_go_aboutus, "Link go aboutus is not present"


def test_negative_guest_can_register_address(page_register):
    page_register.button_go_to_register.click()
    assert page_register.should_be_panel, "Right panel is not present"
    assert page_register.should_be_form, "Customer form is not present"
    page_register.add_first_name.send_keys(Data.first_name)
    page_register.add_last_name.send_keys(Data.last_name)
    page_register.add_city.send_keys(Data.address)
    page_register.add_state.send_keys(Data.address)
    page_register.add_zipcode.send_keys(Data.zipcode)
    page_register.add_phone.send_keys(Data.phone)
    page_register.add_snn.send_keys(Data.snn)
    page_register.add_username.send_keys(f"{Data.first_name + Data.random_number}")
    page_register.add_password.send_keys(Data.password)
    page_register.add_confirm.send_keys(Data.password)
    page_register.button_register.click()
    assert page_register.should_be_text_error_address, "Text error is not present"


def test_negative_guest_can_register_city(page_register):
    page_register.button_go_to_register.click()
    assert page_register.should_be_panel, "Right panel is not present"
    assert page_register.should_be_form, "Customer form is not present"
    page_register.add_first_name.send_keys(Data.first_name)
    page_register.add_last_name.send_keys(Data.last_name)
    page_register.add_address.send_keys(Data.address)
    page_register.add_state.send_keys(Data.address)
    page_register.add_zipcode.send_keys(Data.zipcode)
    page_register.add_phone.send_keys(Data.phone)
    page_register.add_snn.send_keys(Data.snn)
    page_register.add_username.send_keys(f"{Data.first_name + Data.random_number}")
    page_register.add_password.send_keys(Data.password)
    page_register.add_confirm.send_keys(Data.password)
    page_register.button_register.click()
    assert page_register.should_be_text_error_city, "Text error is not present"


def test_negative_guest_can_register_state(page_register):
    page_register.button_go_to_register.click()
    assert page_register.should_be_panel, "Right panel is not present"
    assert page_register.should_be_form, "Customer form is not present"
    page_register.add_first_name.send_keys(Data.first_name)
    page_register.add_last_name.send_keys(Data.last_name)
    page_register.add_address.send_keys(Data.address)
    page_register.add_city.send_keys(Data.address)
    page_register.add_zipcode.send_keys(Data.zipcode)
    page_register.add_phone.send_keys(Data.phone)
    page_register.add_snn.send_keys(Data.snn)
    page_register.add_username.send_keys(f"{Data.first_name + Data.random_number}")
    page_register.add_password.send_keys(Data.password)
    page_register.add_confirm.send_keys(Data.password)
    page_register.button_register.click()
    assert page_register.should_be_text_error_state, "Text error is not present"


def test_negative_guest_can_register_zipcode(page_register):
    page_register.button_go_to_register.click()
    assert page_register.should_be_panel, "Right panel is not present"
    assert page_register.should_be_form, "Customer form is not present"
    page_register.add_first_name.send_keys(Data.first_name)
    page_register.add_last_name.send_keys(Data.last_name)
    page_register.add_address.send_keys(Data.address)
    page_register.add_city.send_keys(Data.address)
    page_register.add_state.send_keys(Data.address)
    page_register.add_phone.send_keys(Data.phone)
    page_register.add_snn.send_keys(Data.snn)
    page_register.add_username.send_keys(f"{Data.first_name + Data.random_number}")
    page_register.add_password.send_keys(Data.password)
    page_register.add_confirm.send_keys(Data.password)
    page_register.button_register.click()
    assert page_register.should_be_text_error_zipcode, "Text error is not present"
