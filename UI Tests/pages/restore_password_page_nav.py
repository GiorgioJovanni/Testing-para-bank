# from selenium.webdriver.common.by import By
# from conftest import browser
#
#
# def account_validate_for_elements(browser):
#     element_first_name = browser.find_element(By.ID, 'firstName')
#     element_first_name.send_keys('First Name')
#
#     element_last_name = browser.find_element(By.ID, 'lastName')
#     element_last_name.send_keys('Last Name')
#
#     element_address = browser.find_element(By.ID, 'address.street')
#     element_address.send_keys('Address')
#
#     element_address_city = browser.find_element(By.ID, 'address.city')
#     element_address_city.send_keys('City')
#
#     element_address_state = browser.find_element(By.ID, 'address.state')
#     element_address_state.send_keys('State')
#
#     element_address_zipcode = browser.find_element(By.ID, 'address.zipCode')
#     element_address_zipcode.send_keys('12345')
#
#     element_ssn = browser.find_element(By.ID, 'ssn')
#     element_ssn.send_keys('1234567890')
#
#     element_ssn.send_keys(Keys.RETURN)
#     browser.current_url
#
#     expected_customer_lookup_message = 'Your login information was located successfully. You are now logged in.'
#     current_element = browser.find_element(By.XPATH, '//div[@id="rightPanel"]/p[1]')
#     assert current_element.text == expected_customer_lookup_message, 'The customer information provided could not be found.'
#
#
# def account_validate_wrong_data():  # wrong element_ssn
#     element_first_name = browser.find_element(By.ID,
#                                               'firstName')  # 'Last Name', 'Address', 'City', 'State', 'Zip Code', 'SSN'
#     element_first_name.send_keys('First Name')
#
#     element_last_name = browser.find_element(By.ID, 'lastName')
#     element_last_name.send_keys('Last Name')
#
#     element_address = browser.find_element(By.ID, 'address.street')
#     element_address.send_keys('Address')
#
#     element_address_city = browser.find_element(By.ID, 'address.city')
#     element_address_city.send_keys('City')
#
#     element_address_state = browser.find_element(By.ID, 'address.state')
#     element_address_state.send_keys('State')
#
#     element_address_zipcode = browser.find_element(By.ID, 'address.zipCode')
#     element_address_zipcode.send_keys('12345')
#
#     element_ssn = browser.find_element(By.ID, 'ssn')
#     element_ssn.send_keys('12345678901')
#
#     element_ssn.send_keys(Keys.RETURN)
#
#     expected_customer_lookup_message = 'The customer information provided could not be found.'
#     current_element = browser.find_element(By.XPATH, '//div[@id="rightPanel"]/p')
#     assert current_element.text == expected_customer_lookup_message
