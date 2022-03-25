import pytest
from selenium import webdriver

from Tests.PageObject.HomePage import HomePage
from Tests.PageObject.Constants import EndPoint
from Tests.PageObject.RegisterPage import RegisterPage


@pytest.fixture(scope="module")
def page_register():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    page = RegisterPage(browser, EndPoint.base_link)
    page.open()
    yield page
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="module")
def page_home():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    page = HomePage(browser, EndPoint.base_link)
    page.open()
    yield page
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="module")
def page_user():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    page = RegisterPage(browser, EndPoint.base_link)
    page.open()
    yield page
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
