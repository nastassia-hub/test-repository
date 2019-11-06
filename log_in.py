import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import random


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def find_by_name(driver, val1, val2):
    driver.find_element_by_name(val1).send_keys(val2)


def email():
    domain = "@gmail.com"
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    name = ""
    for i in range(6):
        name = name + letters[random.randint(0, 11)]
    name = name + domain
    return name


def test_example(driver):
    driver.get("http://localhost/litecart/en/create_account")
    driver.maximize_window()
    find_by_name(driver, "firstname", "Nas1")
    find_by_name(driver, "lastname", "Rad1")
    find_by_name(driver, "address1", "Gazety street")
    find_by_name(driver, "postcode", "12345")
    find_by_name(driver, "city", "New York")
    Select(driver.find_element_by_css_selector("select.select2-hidden-accessible")).select_by_visible_text(
        "United States")
    # find_by_name(driver, 'email', "nas@mail.ru")
    email()
    name_ = email()
    find_by_name(driver, 'email', name_)
    find_by_name(driver, 'phone', "+12312322334")
    find_by_name(driver, "password", "123456789qwer")
    find_by_name(driver, "confirmed_password", "123456789qwer")
    time.sleep(3)
    driver.find_element_by_name("create_account").click()
    time.sleep(5)
    Select(driver.find_element_by_xpath("//*[@id='create-account']//table//tr[5]/td[2]/select")).select_by_value(
        "AL")
    find_by_name(driver, "password", "123456789qwer")
    find_by_name(driver, "confirmed_password", "123456789qwer")
    time.sleep(3)
    driver.find_element_by_name("create_account").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='box-account']/div/ul/li[4]/a").click()
    time.sleep(3)
    find_by_name(driver, 'email', name_)
    find_by_name(driver, "password", "123456789qwer")
    driver.find_element_by_name("login").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='box-account']/div/ul/li[4]/a").click()
    time.sleep(3)
