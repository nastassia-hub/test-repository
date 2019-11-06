import pytest
from selenium import webdriver
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


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
    zones = driver.find_element_by_xpath("//*[@id='box-apps-menu']/li[6]/a")
    zones.click()
    time.sleep(3)
    item = driver.find_elements_by_xpath("//*[@class='row']//td[3]/a")
    print(len(item))
    for i in range(0, len(item)):
        item[i].click()
        time.sleep(2)
        zones_ = driver.find_elements_by_xpath("//*[@id='table-zones']//tr/td[3]/select")
        s = []
        for j in range(0, len(zones_)-1):
            a = zones_[j].get_attribute("textContent")
            s.append(a)
        new_s = sorted(s)
        if new_s == s:
            print("Countries are in alphabet order")
        else:
            print("Countries aren't in alphabet order")
        zones_ = driver.find_elements_by_xpath("//*[@id='table-zones']//tr/td[3]/select")
        driver.back()
        time.sleep(2)
        item = driver.find_elements_by_xpath("//*[@class='row']//td[3]/a")
