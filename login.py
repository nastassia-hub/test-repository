import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/admin")
    # check checkbox
    check = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[3]/td[2]/label/input')
    check.click()
    check.click()
    # check login without name and password
    button = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button')
    button.click()
    # check login with invalid name and password
    login = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[1]/td[2]/span/input')
    login.send_keys("admin@#$")
    password = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[2]/td[2]/span/input')
    password.send_keys("admin@#$")
    button1 = driver.find_element_by_xpath("//*[@id='box-login']/form/div[2]/button")
    button1.click()
    # check login with valid name and password
    login1 = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[1]/td[2]/span/input')
    login1.clear()
    login1.send_keys("admin")
    password1 = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[2]/td[2]/span/input')
    password1.send_keys("admin")
    button2 = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button')
    button2.click()
