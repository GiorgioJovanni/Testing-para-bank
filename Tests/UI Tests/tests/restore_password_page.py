import time


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.get('https://parabank.parasoft.com/parabank/lookup.htm')
driver.delete_all_cookies()

def test_account_validate():
    element_first_name = driver.find_element(By.ID, 'firstName')  # 'Last Name', 'Address', 'City', 'State', 'Zip Code', 'SSN'
    element_first_name.send_keys('First Name')

    element_last_name = driver.find_element(By.ID, 'lastName')
    element_last_name.send_keys('Last Name')

    element_address = driver.find_element(By.ID, 'address.street')
    element_address.send_keys('Address')

    element_address_city = driver.find_element(By.ID, 'address.city')
    element_address_city.send_keys('City')

    element_address_state = driver.find_element(By.ID, 'address.state')
    element_address_state.send_keys('State')

    element_address_zipcode = driver.find_element(By.ID, 'address.zipCode')
    element_address_zipcode.send_keys('12345')

    element_ssn = driver.find_element(By.ID, 'ssn')
    element_ssn.send_keys('1234567890')

    element_ssn.send_keys(Keys.RETURN)
    # The customer information provided could not be found.
    #time.sleep(5)
    driver.current_url
    expected_customer_lookup_message = 'Your login information was located successfully. You are now logged in.'
    # assert expected_customer_lookup_message == driver.find_element(By.XPATH, '//div[@id="rightPanel"]/p[1]')
    current_element = driver.find_element(By.XPATH, '//div[@id="rightPanel"]/p[1]')
    # print(element.text)
    assert current_element.text == expected_customer_lookup_message, 'The customer information provided could not be found.'
    # print(expected_customer_lookup_message.text)
    # Your login information was located successfully. You are now logged in.
    driver.quit()


def test_account_validate_wrongdata():  # wrong element_ssn
    element_first_name = driver.find_element(By.ID,
                                            'firstName')  # 'Last Name', 'Address', 'City', 'State', 'Zip Code', 'SSN'
    element_first_name.send_keys('First Name')

    element_last_name = driver.find_element(By.ID, 'lastName')
    element_last_name.send_keys('Last Name')

    element_address = driver.find_element(By.ID, 'address.street')
    element_address.send_keys('Address')

    element_address_city = driver.find_element(By.ID, 'address.city')
    element_address_city.send_keys('City')

    element_address_state = driver.find_element(By.ID, 'address.state')
    element_address_state.send_keys('State')

    element_address_zipcode = driver.find_element(By.ID, 'address.zipCode')
    element_address_zipcode.send_keys('12345')

    element_ssn = driver.find_element(By.ID, 'ssn')
    element_ssn.send_keys('12345678901')

    element_ssn.send_keys(Keys.RETURN)
    time.sleep(2)

    expected_customer_lookup_message = 'The customer information provided could not be found.'
    current_element = driver.find_element(By.XPATH, '//div[@id="rightPanel"]/p')
    assert current_element.text == expected_customer_lookup_message
    driver.quit()
