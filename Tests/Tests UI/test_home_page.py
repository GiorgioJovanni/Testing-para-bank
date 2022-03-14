def test_guest_use_buttons_gohome_contact_aboutus_from_register_page(page_home):
    page_home.button_go_home()
    page_home.open()
    page_home.press_the_button_register_base()
    page_home.button_go_contact()
    page_home.open()
    page_home.press_the_button_register_base()
    page_home.button_go_aboutus()


def test_guest_use_button_about_us(page_home):
    page_home.button_go_about_us()


def test_guest_use_button_services(page_home):
    page_home.button_go_services()


def test_guest_use_button_products(page_home):
    page_home.button_go_products()


def test_guest_use_button_locations(page_home):
    page_home.button_go_locations()


def test_guest_use_button_admin_page(page_home):
    page_home.button_go_admin_page()
