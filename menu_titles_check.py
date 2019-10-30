import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False


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
    main_elements = driver.find_elements_by_css_selector("li#app-")
    for i in range(0, len(main_elements)-1):
        main_elements[i].click()
        is_element_present(driver, By.CSS_SELECTOR, "td.h1")
        sub_els = driver.find_elements_by_css_selector("[id^=doc-]")
        for a in range(0, len(sub_els)-1):
            sub_els[a].click()
            is_element_present(driver, By.CSS_SELECTOR, "td.h1")
            sub_els = driver.find_elements_by_css_selector("[id^=doc-]")
            print(len(sub_els))
        main_elements = driver.find_elements_by_css_selector("li#app-")
    print(len(main_elements))
