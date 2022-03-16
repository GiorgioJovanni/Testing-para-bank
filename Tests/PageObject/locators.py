from selenium.webdriver.common.by import By


class BasePageLocators:
    MESSAGE = (By.CSS_SELECTOR, '#message')
    LINK = (By.CSS_SELECTOR, '#rightPanel > p:nth-child(4) > a')
    IMAGE = (By.CSS_SELECTOR, 'span.services')
    FIELD_USERNAME = (By.CSS_SELECTOR, 'input[name="username"]')
    FIELD_PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
    TEXT = (By.CSS_SELECTOR, 'body > pre')

    BUTTON_LOG_IN = (By.CSS_SELECTOR, 'input[value="Log In"]')
    BUTTON_FORGOT_LOGIN = (By.CSS_SELECTOR, 'a[href="lookup.htm"]')
    BUTTON_REGISTER = (By.XPATH, '//*[@id="loginPanel"]/p[2]/a')

    BUTTON_GO_BASE_PAGE = (By.CSS_SELECTOR, 'li.home')
    BUTTON_GO_ABOUTUS_PAGE = (By.CSS_SELECTOR, 'li.aboutus')
    BUTTON_GO_CONTACT_PAGE = (By.CSS_SELECTOR, 'li.contact')

    BUTTON_ABOUT_US = (By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[2]/a')
    BUTTON_SERVICES = (By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[3]/a')
    BUTTON_PRODUCTS = (By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[4]/a')
    BUTTON_LOCATIONS = (By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[5]/a')
    BUTTON_ADMIN_PAGE = (By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[6]/a')


class RegisterPageLocators:
    RIGHT_PANEL = (By.CSS_SELECTOR, '#rightPanel')
    CUSTOMER_FORM = (By.CSS_SELECTOR, '#customerForm')
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, '[name = "customer.firstName"]')
    FIELD_LAST_NAME = (By.CSS_SELECTOR, '[name="customer.lastName"]')
    FIELD_ADDRESS = (By.CSS_SELECTOR, '[name="customer.address.street"]')
    FIELD_CITY = (By.CSS_SELECTOR, '[name="customer.address.city"]')
    FIELD_STATE = (By.CSS_SELECTOR, '[name="customer.address.state"]')
    FIELD_ZIPCODE = (By.CSS_SELECTOR, '[name="customer.address.zipCode"]')
    FIELD_PHONE = (By.CSS_SELECTOR, '[name="customer.phoneNumber"]')
    FIELD_SNN = (By.CSS_SELECTOR, '[name="customer.ssn"]')
    FIELD_USERNAME = (By.CSS_SELECTOR, '[name="customer.username"]')
    FIELD_PASSWORD = (By.CSS_SELECTOR, '[name="customer.password"]')
    FIELD_CONFIRM = (By.CSS_SELECTOR, '[name="repeatedPassword"]')
    BUTTON_REGISTER = (By.CSS_SELECTOR, '[value="Register"]')
    BUTTON_LOG_OUT = (By.CSS_SELECTOR, '[href="/parabank/logout.htm"]')

    TEXT_ERROR_ADDRESS = (By.CSS_SELECTOR, '#customerForm > table > tbody > tr:nth-child(3) >'
                                           ' td:nth-child(3) span.error')
    TEXT_ERROR_CITY = (By.CSS_SELECTOR, '#customerForm > table > tbody > tr:nth-child(4) > td:nth-child(3) span.error')
    TEXT_ERROR_STATE = (By.CSS_SELECTOR, '#customerForm > table > tbody > tr:nth-child(5) > td:nth-child(3) span.error')
    TEXT_ERROR_ZIPCODE = (By.CSS_SELECTOR, '#customerForm > table > tbody > tr:nth-child(6) >'
                                           ' td:nth-child(3) span.error')


class AboutUsPageLocators:
    LINK = (By.XPATH, '//*[@id="rightPanel"]/p[3]/a')


class ServicesPageLocators:
    HEADER_AVAILABLE_BOOKSTORE_SOAP = (By.XPATH, '//*[@id="rightPanel"]/span[1]')
    HEADER_BOOKSTORE = (By.XPATH, '//*[@id="rightPanel"]/span[2]')
    HEADER_PARABANK_SOAP = (By.XPATH, '//*[@id="rightPanel"]/span[3]')
    HEADER_PARABANK = (By.XPATH, '//*[@id="rightPanel"]/span[4]')
    HEADER_RESTFUL = (By.XPATH, '//*[@id="rightPanel"]/span[5]')


class ProductsAndLocationsPageLocators:
    LOGO = (By.CSS_SELECTOR, 'div.home-logo img[src="https://www.parasoft.com/'
                             'wp-content/uploads/2020/06/parasoft.svg"]')


class AdminPagePageLocators:
    BOARD = (By.CSS_SELECTOR, '#adminForm .form')
