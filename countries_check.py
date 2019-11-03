import pytest
from selenium import webdriver
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def countries_check_1(driver):
    # check all countries
    countries = driver.find_element_by_xpath("//*[@id='box-apps-menu']/li[3]/a")
    countries.click()
    time.sleep(3)
    s = []
    con = driver.find_elements_by_xpath("//*[@class='row']//td[5]/a")
    for i in range(0, len(con) - 1):
        a = con[i].get_attribute("textContent")
        s.append(a)
    new_s = sorted(s)
    if new_s == s:
        return True
    else:
        print("Countries aren't in alphabet order")


def countries_check_2(driver):
    # check countries where zones != 0
    zone = driver.find_elements_by_xpath("//*[@class='row']//td[6]")
    for j in range(0, len(zone)):
        numb = zone[j].get_attribute("textContent")
        if numb != "0":
            con = driver.find_elements_by_xpath("//*[@class='row']//td[5]/a")
            con[j].click()
            time.sleep(3)
            con2 = driver.find_elements_by_xpath("//*[@class='dataTable']//tr/td[3]")
            q = []
            for k in range(0, len(con2) - 1):
                z = con2[k].get_attribute("textContent")
                q.append(z)
            new_q = sorted(q)
            if new_q == q:
                print("Countries are in alphabet order")
            else:
                print("Countries aren't in alphabet order")
            driver.back()
            time.sleep(2)
        zone = driver.find_elements_by_xpath("//*[@class='row']//td[6]")


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
    countries_check_1(driver)
    countries_check_2(driver)
