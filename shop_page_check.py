import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.color import Color


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def com_values(val, val_):
    if val == val_:
        return True
    else:
        print("Error in name/price")


def com_colors(val2, val3):
    color_hex = Color.from_string(val2).hex
    if color_hex == val3:
        return True
    else:
        print("Error in colors")


def com_weights(val4):
    if val4 == "700":
        return True
    else:
        print("Error in weight")


def com_sizes(val5, val6, val7, val8):
    val5 = {}
    val5.update(val6)
    a = val5["height"]
    b = val5["width"]
    val7 = {}
    val7.update(val8)
    c = val7["height"]
    d = val7["width"]
    if c > a and d > b:
        return True
    else:
        print("Eror in sizes")


def com_text_decoration(val9):
    if val9 == "line-through":
        return True
    else:
        print("Error in text decoration")


def test_example(driver):
    driver.get("http://localhost/litecart")
    driver.maximize_window()

    duck = driver.find_element_by_xpath("//*[@id='box-campaigns']//a")
    name = duck.get_attribute("title")
    reg_price = driver.find_element_by_xpath("//*[@id='box-campaigns']//a/div[4]/s")
    reg_color = reg_price.value_of_css_property("color")
    com_colors(reg_color, "#777777")
    reg_size = reg_price.size
    reg_decor = reg_price.value_of_css_property("text-decoration-line")
    com_text_decoration(reg_decor)
    com_price = driver.find_element_by_xpath("//*[@id='box-campaigns']//a/div[4]/strong")
    com_color = com_price.value_of_css_property("color")
    com_colors(com_color, "#cc0000")
    weight = com_price.value_of_css_property("font-weight")
    com_weights(weight)
    com_size = com_price.size
    s = {}
    q = {}
    com_sizes(s, reg_size, q, com_size)
    reg_price = reg_price.get_attribute("textContent")
    com_price = com_price.get_attribute("textContent")

    # new page
    duck.click()
    time.sleep(2)
    title = driver.find_element_by_css_selector("h1.title")
    name_ = title.get_attribute("textContent")
    reg_pr = driver.find_element_by_css_selector("s.regular-price")
    reg_color_ = reg_pr.value_of_css_property("color")
    com_colors(reg_color_, "#666666")
    reg_decor_ = reg_pr.value_of_css_property("text-decoration-line")
    com_text_decoration(reg_decor_)
    reg_size_ = reg_pr.size
    com_pr = driver.find_element_by_css_selector("strong.campaign-price")
    com_color_ = com_pr.value_of_css_property("color")
    com_colors(com_color_, "#cc0000")
    weight_ = com_pr.value_of_css_property("font-weight")
    com_weights(weight_)
    com_size_ = com_pr.size
    s_ = {}
    q_ = {}
    com_sizes(s_, reg_size_, q_, com_size_)
    reg_price_ = reg_pr.get_attribute("textContent")
    com_price_ = com_pr.get_attribute("textContent")
    com_values(name, name_)
    com_values(reg_price, reg_price_)
    com_values(com_price, com_price_)
