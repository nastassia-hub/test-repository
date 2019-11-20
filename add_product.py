import os
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def clear_and_send(driver, par, par1):
    el = driver.find_element_by_name(par)
    el.clear()
    el.send_keys(par1)


def send_home(driver, par2, par3):
    el1 = driver.find_element_by_name(par2)
    el1.send_keys(Keys.HOME + par3)


def test_example(driver):
    driver.get("http://localhost/litecart/admin")
    driver.maximize_window()

    # log in
    login = driver.find_element_by_xpath('//*[@id="box-login"]//tr[1]/td[2]/span/input')
    login.send_keys("admin")
    password = driver.find_element_by_xpath('//*[@id="box-login"]//tr[2]/td[2]/span/input')
    password.send_keys("admin")
    button = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button')
    button.click()

    # test
    driver.find_element_by_xpath("//*[@id='box-apps-menu']/li[2]/a").click()
    driver.find_element_by_xpath("//*[@id='content']/div/a[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@type='radio' and @value='1']").click()
    driver.find_element_by_name("name[en]").send_keys("New product")
    driver.find_element_by_name("code").send_keys("1234")
    driver.find_element_by_xpath("//input[@type='checkbox' and @value='0']").click()
    driver.find_element_by_xpath("//input[@type='checkbox' and @value='1']").click()
    driver.find_element_by_xpath("//input[@type='checkbox' and @value='1-3']").click()
    clear_and_send(driver, "quantity", "1")
    driver.find_element_by_name("new_images[]").send_keys(os.getcwd()+"/12.jpg")
    send_home(driver, "date_valid_from", "12.12.2012")
    send_home(driver, "date_valid_to", "16.12.2012")
    driver.find_element_by_xpath("//*[@id='content']/form/div/ul/li[2]/a").click()
    time.sleep(2)
    Select(driver.find_element_by_name("manufacturer_id")).select_by_visible_text(
        "ACME Corp.")
    driver.find_element_by_name("keywords").send_keys("duck")
    driver.find_element_by_name("short_description[en]").send_keys("shot description")
    driver.find_element_by_css_selector("[class=trumbowyg-editor]").send_keys("large description")
    driver.find_element_by_name("head_title[en]").send_keys("title")
    driver.find_element_by_name("meta_description[en]").send_keys("description")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='content']/form/div/ul/li[4]/a").click()
    clear_and_send(driver, "purchase_price", "10")
    Select(driver.find_element_by_name("purchase_price_currency_code")).select_by_visible_text(
        "US Dollars")
    clear_and_send(driver, "gross_prices[USD]", "10")
    clear_and_send(driver, "gross_prices[EUR]", "10")
    time.sleep(2)
    driver.find_element_by_xpath("//button[@name='save']").click()
