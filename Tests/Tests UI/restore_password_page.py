import faker
from selenium import webdriver
from selenium.webdriver.common.by import By

#global driver
driver = webdriver.Edge()
driver.get('https://parabank.parasoft.com/parabank/lookup.htm')

def test_account_validate():
    element = driver.find_element(By.ID, 'firstName') #'Last Name', 'Address', 'City', 'State', 'Zip Code', 'SSN')
    element.send_keys('')
    # b = el.get_attribute('value')
    # assert b == 'or.amoyal'

from faker import Faker
fake = Faker()

print(fake.name())



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
