from selenium.webdriver.common.by import By


class BasePageLocators:
    MESSAGE = (By.CSS_SELECTOR, '#message')
    LINK = (By.CSS_SELECTOR, '#rightPanel > p:nth-child(4) > a')
    IMAGE = (By.CSS_SELECTOR, 'span.services')
    BUTTON_GO_BASE_PAGE = (By.CSS_SELECTOR, 'li.home')
    BUTTON_GO_ABOUTUS_PAGE = (By.CSS_SELECTOR, 'li.aboutus')
    BUTTON_GO_CONTACT_PAGE = (By.CSS_SELECTOR, 'li.contact')
    FIELD_USERNAME = (By.CSS_SELECTOR, 'input[name="username"]')
    FIELD_PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
    BUTTON_LOG_IN = (By.CSS_SELECTOR, 'input[value="Log In"]')
    BUTTON_FORGOT_LOGIN = (By.CSS_SELECTOR, 'a[href="lookup.htm"]')
    BUTTON_REGISTER = (By.XPATH, '//*[@id="loginPanel"]/p[2]/a')
    TEXT = (By.CSS_SELECTOR, 'body > pre')


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
    TEXT_ERROR = (By.CSS_SELECTOR, 'span.error')
