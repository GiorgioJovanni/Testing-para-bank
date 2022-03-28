from restore_password_page import CustomerLookupPage


def test_should_be_lookup_page_url(browser):
    link = 'https://parabank.parasoft.com/parabank/lookup.htm'
    page = CustomerLookupPage(browser, link)
    page.open()
    page.should_be_lookup_page_url()


def test_should_be_lookup_page_form(browser):
    link = 'https://parabank.parasoft.com/parabank/lookup.htm'
    page = CustomerLookupPage(browser, link)
    page.open()
    page.should_be_lookup_page_form()


def test_should_be_lookup_page_form_data(browser):
    link = 'https://parabank.parasoft.com/parabank/lookup.htm'
    page = CustomerLookupPage(browser, link)
    page.open()
    page.should_be_lookup_page_form_data()


def test_account_validate(browser):
    link = 'https://parabank.parasoft.com/parabank/lookup.htm'
    page = CustomerLookupPage(browser, link)
    page.open()
    page.account_validate()


# def test_account_validate_wrongdata(browser):  # wrong element_ssn
#     browser.get(link)
#     account_validate_wrong_data(browser)
#     time.sleep(2)
#     browser.quit()
