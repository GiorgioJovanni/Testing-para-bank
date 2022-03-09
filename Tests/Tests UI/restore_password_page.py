import faker
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# global driver
driver = webdriver.Edge()
driver.get('https://parabank.parasoft.com/parabank/lookup.htm')


def test_account_validate():
    element_firstName = driver.find_element(By.ID,'firstName')  # 'Last Name', 'Address', 'City', 'State', 'Zip Code', 'SSN'
    element_firstName.send_keys('First Name')

    element_lastName = driver.find_element(By.ID, 'lastName')
    element_lastName.send_keys('Last Name')

    element_Address = driver.find_element(By.ID, 'address.street')
    element_Address.send_keys('Address')

    element_address_city = driver.find_element(By.ID, 'address.city')
    element_address_city.send_keys('City')

    element_address_state = driver.find_element(By.ID, 'address.state')
    element_address_state.send_keys('State')

    element_address_zipCode = driver.find_element(By.ID, 'address.zipCode')
    element_address_zipCode.send_keys('12345')

    element_ssn = driver.find_element(By.ID, 'ssn')
    element_ssn.send_keys('1234567890')

    element_ssn.send_keys(Keys.RETURN)
    # The customer information provided could not be found.

    driver.current_url
    expected_customer_lookup_message = 'Your login information was located successfully. You are now logged in.'
    #assert expected_customer_lookup_message == driver.find_element(By.XPATH, '//div[@id="rightPanel"]/p[1]')
    element = driver.find_element(By.XPATH, '//div[@id="rightPanel"]/p[1]')
    #print(element.text)
    assert element.text == expected_customer_lookup_message, 'The customer information provided could not be found.'
    #print(expected_customer_lookup_message.text)
    # Your login information was located successfully. You are now logged in.

def test_account_validate_wrongdata():
    element_firstName = driver.find_element(By.ID,'firstName')  # 'Last Name', 'Address', 'City', 'State', 'Zip Code', 'SSN'
    element_firstName.send_keys('First Name')

    element_lastName = driver.find_element(By.ID, 'lastName')
    element_lastName.send_keys('Last Name')

    element_Address = driver.find_element(By.ID, 'address.street')
    element_Address.send_keys('Address')

    element_address_city = driver.find_element(By.ID, 'address.city')
    element_address_city.send_keys('City')

    element_address_state = driver.find_element(By.ID, 'address.state')
    element_address_state.send_keys('State')

    element_address_zipCode = driver.find_element(By.ID, 'address.zipCode')
    element_address_zipCode.send_keys('12345')

    element_ssn = driver.find_element(By.ID, 'ssn')
    element_ssn.send_keys('12345678901')

    element_ssn.send_keys(Keys.RETURN)

    expected_customer_lookup_message = 'The customer information provided could not be found.'
    element = driver.find_element(By.XPATH, '//div[@id="rightPanel"]/p')
    assert element.text == expected_customer_lookup_message

# from faker import Faker
#
# fake = Faker()
#
# print(fake.name())

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Edge()
#
# driver.get('https://bing.com')
#
# element = driver.find_element(By.ID, 'sb_form_q')
# element.send_keys('WebDriver')
# element.submit()
#
# time.sleep(5)
# driver.quit()

