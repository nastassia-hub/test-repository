import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) > 0


def test_example(driver):
    driver.get("http://localhost/litecart")
    driver.maximize_window()

    # test
    main_elements = driver.find_elements_by_css_selector("li.product")
    for i in range(0, len(main_elements) - 1):
        are_elements_present(driver, By.CSS_SELECTOR, "[class^=sticker]")
        sticker = main_elements[i].find_elements_by_css_selector("[class^=sticker]")
        x = len(sticker)
        if x == 1:
            return True
        else:
            print(i, "element has more than 1 sticker")
        main_elements = driver.find_elements_by_css_selector("li.product")
