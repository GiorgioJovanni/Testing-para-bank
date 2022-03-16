def test_guest_use_buttons_gohome_contact_aboutus_from_register_page(page_home):
    page_home.button_go_home.click()
    page_home.should_be_image_go_home()
    page_home.open()
    page_home.press_the_button_register_base.click()
    page_home.button_go_contact.click()
    page_home.should_be_message_go_contact()
    page_home.open()
    page_home.press_the_button_register_base.click()
    page_home.button_go_aboutus.click()
    page_home.should_be_link_go_aboutus()


def test_guest_use_button_about_us(page_home):
    page_home.button_go_about_us.click()
    page_home.should_be_link_go_about_us()


def test_guest_use_button_services(page_home):
    page_home.button_go_services.click()
    page_home.should_be_soap_go_services()
    page_home.should_be_bookstore_go_services()
    page_home.should_be_parabank_soap_go_services()
    page_home.should_be_parabank_go_services()
    page_home.should_be_restful_go_services()


def test_guest_use_button_admin_page(page_home):
    page_home.button_go_admin_page.click()
    page_home.should_be_header_go_admin_page()


def test_guest_use_button_locations(page_home):
    page_home.button_go_locations.click()
    page_home.should_be_logo_go_locations()
    page_home.open()


def test_guest_use_button_products(page_home):
    page_home.button_go_products.click()
    page_home.should_be_logo_go_products()
    page_home.open()
