import pytest
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


# def there_is_window_other_than(driver, a, new_windows, old_windows):
    # new = driver.window_handles
    # print(new)
    # # new.remove(old_windows)
    # # return new
    # old_windows = driver.window_handles
    # a.click()
    # if new_windows != old_windows:
    #     new_window = new_windows.remove(old_windows)
    #     driver.switch_to_window(new_window)


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
    countries = driver.find_element_by_xpath("//*[@id='box-apps-menu']/li[3]/a")
    countries.click()
    countrie = driver.find_element_by_xpath("//*[@id='content']/form/table/tbody/tr[2]/td[5]/a")
    countrie.click()
    link = driver.find_elements_by_css_selector("i.fa.fa-external-link")
    main_window = driver.current_window_handle
    main_window = driver.current_window_handle
    for i in range(0, len(link) - 1):
        # main_window = driver.current_window_handle
        # old_windows = driver.window_handles
        # print(old_windows)
        # size = len(old_windows)
        # link[i].click()
        # new_windows = driver.window_handles
        # for j in range(0, size - 1):
        #     there_is_window_other_than(driver, new_windows, old_windows)
        old_windows = driver.window_handles
        link[i].click()
        time.sleep(2)
        new_windows = driver.window_handles
        print(main_window)
        print(old_windows)
        print(new_windows)

        for old_windows in new_windows:
            new_windows.remove(old_windows)
            print(new_windows)
            new_window = ''
            new_window.join(new_windows)
            # print(new_window)
            print(type(new_window))

            print(new_windows)
            driver.switch_to_window(new_window)
            time.sleep(2)
            driver.close()
            driver.switch_to_window(main_window)

