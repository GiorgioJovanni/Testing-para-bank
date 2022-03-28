import time

from Tests.PageObject.Constants import Data


def test_guest_can_reg(page_user):
    page_user.button_go_to_register.click()
    assert page_user.should_be_panel, "Right panel is not present"
    assert page_user.should_be_form, "Customer form is not present"
    page_user.add_first_name.send_keys(Data.first_name)
    page_user.add_last_name.send_keys(Data.last_name)
    page_user.add_address.send_keys(Data.address)
    page_user.add_city.send_keys(Data.address)
    page_user.add_state.send_keys(Data.address)
    page_user.add_zipcode.send_keys(Data.zipcode)
    page_user.add_phone.send_keys(Data.phone)
    page_user.add_snn.send_keys(Data.snn)
    page_user.add_username.send_keys(f"{Data.first_name + Data.random_number}")
    page_user.add_password.send_keys(Data.password)
    page_user.add_confirm.send_keys(Data.password)
    page_user.button_register.click()
    assert page_user.should_not_be_button_register, "Button register is not disappear"


def test_user_can_go_new_account(page_user):
    page_user.button_open_new_account.click()
    assert page_user.should_be_slider_type, "Slider type is not present"
    assert page_user.should_be_slider_from_account, "Slider from account is not present"
    assert page_user.should_be_button_open_new_account, 'Button open new account account is not present'


def test_user_can_open_new_saving_account(page_user):
    page_user.button_open_new_account.click()
    page_user.slider_type_saving()
    time.sleep(1)
    page_user.button_register_new_account.click()
    assert page_user.should_be_new_id_account, "New id account is not present"


def test_user_can_open_new_checking_account(page_user):
    page_user.button_open_new_account.click()
    page_user.slider_type_checking()
    time.sleep(1)
    page_user.button_register_new_account.click()
    assert page_user.should_be_new_id_account, "New id account is not present"


def test_user_can_go_accounts_overview(page_user):
    page_user.button_overview.click()
    assert page_user.should_be_text_balance, "Text balance is not present"
    assert page_user.should_be_text_id_account, "Text id account is not present"


def test_user_can_go_transfer(page_user):
    page_user.button_transfer_funds.click()
    assert page_user.should_be_amount, "Amount is not present"
    assert page_user.should_be_button_transfer, "Button transfer is not present"


def test_user_transfer(page_user):
    page_user.button_transfer_funds.click()
    time.sleep(1)
    page_user.box_amount.send_keys(Data.amount)
    page_user.button_transfer.click()
    assert page_user.should_be_slider_from_account, "Slider from account is not present"
    assert page_user.should_be_slider_to_account, "Slider to account is not present"


def test_guest_can_go_bill_pay(page_user):
    page_user.button_bill_pay.click()
    assert page_user.should_be_button_send_payment, "Button send payment is not present"
    assert page_user.should_be_box_payee_name, "Box payee name is not present"
