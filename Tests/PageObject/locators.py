from selenium.webdriver.common.by import By


class BasePageLocators:
    FIELD_USERNAME = (By.CSS_SELECTOR, 'input[name="username"]')
    FIELD_PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
    BUTTON_LOG_IN = (By.CSS_SELECTOR, 'input[value="Log In"]')
    BUTTON_FORGOT_LOGIN = (By.CSS_SELECTOR, 'a[href="lookup.htm"]')
    BUTTON_REGISTER = (By.CSS_SELECTOR, 'a[href="register.htm"]')


class RegisterPageLocators:
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
