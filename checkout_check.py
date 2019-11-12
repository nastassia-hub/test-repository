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
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def is_element_present(driver):
    try:
        driver.find_element(By.NAME, "options[Size]")
        return True
    except NoSuchElementException:
        return


def add_duck(driver):
    duck = driver.find_element_by_xpath("//*[@id='box-most-popular']//a")
    duck.click()
    is_element_present(driver)
    if is_element_present(driver):
        Select(driver.find_element_by_xpath("//*[@class='options']/select")).select_by_visible_text(
            "Small")
        add = driver.find_element_by_xpath("//*[@class='quantity']/button")
        add.click()
    else:
        add = driver.find_element_by_xpath("//*[@class='quantity']/button")
        add.click()


def test_example(driver):
    driver.get("http://litecart.stqa.ru/ru/")
    driver.maximize_window()

    # add 3 ducks
    add_duck(driver)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), "1"))
    driver.back()
    add_duck(driver)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), "2"))
    driver.back()
    add_duck(driver)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), "3"))

    # go to checkout
    driver.find_element_by_xpath("//*[@id='cart']/a[3]").click()
    table = driver.find_element_by_css_selector("div#box-checkout-summary.box")
    driver.find_element_by_xpath("//*[@name='cart_form']//div//p[4]").click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.staleness_of(table))
    driver.find_element_by_css_selector("[name=remove_cart_item]").click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.staleness_of(table))
    driver.find_element_by_css_selector("[name=remove_cart_item]").click()
    time.sleep(5)
