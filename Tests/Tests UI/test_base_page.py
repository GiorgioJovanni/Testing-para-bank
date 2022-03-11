def test_guest_use_buttons_gohome_contact_aboutus_from_register_page(page_base):
    page_base.button_go_home()
    page_base.open()
    page_base.press_the_button_register_base()
    page_base.button_go_contact()
    page_base.open()
    page_base.press_the_button_register_base()
    page_base.button_go_aboutus()


class TestUpMenu:
    def test_guest_use_button_about_us(self, page_base):
        page_base.button_go_about_us()

    def test_guest_use_button_services(self, page_base):
        page_base.button_go_services()

    def test_guest_use_button_products(self, page_base):
        page_base.button_go_products()

    def test_guest_use_button_locations(self, page_base):
        page_base.button_go_locations()

    def test_guest_use_button_admin_page(self, page_base):
        page_base.button_go_admin_page()
