import pytest
from selenium import webdriver

from Tests.PageObject.BasePage import BasePage
from Tests.PageObject.Constants import EndPoint
from Tests.PageObject.RegisterPage import RegisterPage


@pytest.fixture
def page_register():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    page = RegisterPage(browser, EndPoint.base_link)
    page.open()
    yield page
    print("\nquit browser..")
    browser.quit()


@pytest.fixture
def page_base():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    page = BasePage(browser, EndPoint.base_link)
    page.open()
    yield page
    print("\nquit browser..")
    browser.quit()


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
