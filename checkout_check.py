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
    wait = WebDriverWait(driver, 5)
    remove = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='item']//div/p[4]/button")))
    remove.click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.invisibility_of_element_located((By.XPATH, "//*[@id='order_confirmation-wrapper']//tr[4]")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='order_confirmation-wrapper']//tr[4]")))
    remove = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='item']//div/p[4]/button")))
    remove.click()
    # wait = WebDriverWait(driver, 5)
    # wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='order_confirmation-wrapper']//tr[3]"), "&nbsp"))
    # remove = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='item']//div/p[4]/button")))
    # remove.click()
    # wait = WebDriverWait(driver, 5)
    # wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='order_confirmation-wrapper']//tr[2]"), "&nbsp"))
    # time.sleep(5)
