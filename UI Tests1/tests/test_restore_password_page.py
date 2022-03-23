from pages.restore_password_page import CustomerLookupPage


def test_should_be_lookup_page_url(browser):
    link = 'https://parabank.parasoft.com/parabank/lookup.htm'
    page = CustomerLookupPage(browser, link)
    page.open()
    page.should_be_lookup_page_url(browser)


def test_account_validate(browser):
    browser.get(link)
    account_validate_for_elements(browser)
    time.sleep(2)
    browser.quit()


def test_account_validate_wrongdata(browser):  # wrong element_ssn
    browser.get(link)
    account_validate_wrong_data(browser)
    time.sleep(2)
    browser.quit()
