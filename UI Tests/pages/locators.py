from selenium.webdriver.common.by import By


class CustomerLookupPageLocators():
    LOOKUP_PAGE_FORM = (By.XPATH, "//div[@id='rightPanel']/form[@id='lookupForm']")


class CustomerLookupPageLocatorsData():
    FIRST_NAME = (By.ID, 'firstName')
    LAST_NAME = (By.ID, 'lastName')
    ADDRESS = (By.ID, 'address.street')
    CITY = (By.ID, 'address.city')
    STATE = (By.ID, 'address.state')
    ZIP_CODE = (By.ID, 'address.zipCode')
    SSN = (By.ID, 'ssn')
