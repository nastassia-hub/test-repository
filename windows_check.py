import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def there_is_window_other_than(driver, old_windows):
    handles = driver.window_handles
    for handle in handles:
        while True:
            try:
                handles.remove(old_windows)
            except:
                break
    return driver


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
    driver.find_element_by_xpath("//*[@id='box-apps-menu']/li[3]/a").click()
    driver.find_element_by_xpath("//*[@id='content']/form/table/tbody/tr[2]/td[5]/a").click()
    link = driver.find_elements_by_css_selector("i.fa.fa-external-link")

    for i in range(0, len(link)):
        main_window = driver.current_window_handle
        old_windows = driver.window_handles
        link[i].click()
        time.sleep(2)
        new_windows = driver.window_handles
        wait = WebDriverWait(driver, 5)
        new_window = wait.until(there_is_window_other_than(driver, old_windows))
        driver.switch_to_window(new_window)
        time.sleep(2)
        driver.close()
        driver.switch_to_window(main_window)
