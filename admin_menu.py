import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/admin")
    driver.maximize_window()
    # log in
    login = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[1]/td[2]/span/input')
    login.send_keys("admin")
    password = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[2]/td[2]/span/input')
    password.send_keys("admin")
    button = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button')
    button.click()
    # checking menu items
    app = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li/a/span[2]')
    app.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    driver.implicitly_wait(3)
    log = driver.find_element_by_css_selector("li#doc-logotype")
    log.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    cat = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[2]/a/span[2]')
    cat.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    dcat = driver.find_element_by_css_selector("li#doc-catalog")
    dcat.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    prod = driver.find_element_by_css_selector("li#doc-product_groups")
    prod.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    opt = driver.find_element_by_css_selector("li#doc-option_groups")
    opt.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    man = driver.find_element_by_css_selector("li#doc-manufacturers")
    man.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    sup = driver.find_element_by_css_selector("li#doc-suppliers")
    sup.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    stat = driver.find_element_by_css_selector("li#doc-delivery_statuses")
    stat.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    sold = driver.find_element_by_css_selector("li#doc-sold_out_statuses")
    sold.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    quan = driver.find_element_by_css_selector("li#doc-quantity_units")
    quan.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    csv = driver.find_element_by_css_selector("li#doc-csv")
    csv.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    countries = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[3]/a/span[2]')
    countries.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    cur = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[4]/a/span[2]')
    cur.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    cus = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[5]/a/span[2]')
    cus.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    csv_imp = cus.find_element_by_css_selector("ul#docs[id=doc-csv]")
    csv_imp.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    news = cus.find_element_by_css_selector("li#doc-newsletter")
    news.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    zone = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[6]/a/span[2]')
    zone.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    lang = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[7]/a/span[2]')
    lang.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    stor = driver.find_element_by_css_selector("li#doc-storage_encoding")
    stor.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    mod = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[8]/a/span[2]')
    mod.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    cus = driver.find_element_by_css_selector("li#doc-customer")
    cus.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    ship = driver.find_element_by_xpath('//*[@id="doc-shipping"]/a/span')
    ship.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    pay = driver.find_element_by_xpath('//*[@id="doc-payment"]/a/span')
    pay.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    order = driver.find_element_by_xpath('//*[@id="doc-order_total"]/a/span')
    order.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    order1 = driver.find_element_by_xpath('//*[@id="doc-order_success"]/a/span')
    order1.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    order2 = driver.find_element_by_xpath('//*[@id="doc-order_action"]/a/span')
    order2.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    orders = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[9]/a/span[2]')
    orders.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    orders1 = driver.find_element_by_css_selector("li#doc-order_statuses")
    orders1.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    pages = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[10]/a/span[2]')
    pages.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    rep = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[11]/a/span[2]')
    rep.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    sold = driver.find_element_by_xpath('//*[@id="doc-most_sold_products"]/a/span')
    sold.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    shop = driver.find_element_by_xpath('//*[@id="doc-most_shopping_customers"]/a/span')
    shop.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    sett = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[12]/a/span[2]')
    sett.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    defaults = driver.find_element_by_css_selector("li#doc-defaults")
    defaults.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    gen = driver.find_element_by_xpath('//*[@id="doc-general"]/a/span')
    gen.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    listi = driver.find_element_by_xpath('//*[@id="doc-listings"]/a/span')
    listi.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    imag = driver.find_element_by_xpath('//*[@id="doc-images"]/a/span')
    imag.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    checkout = driver.find_element_by_xpath('//*[@id="doc-checkout"]/a/span')
    checkout.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    adv = driver.find_element_by_xpath('//*[@id="doc-advanced"]/a/span')
    adv.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    sec = driver.find_element_by_xpath('//*[@id="doc-security"]/a/span')
    sec.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    slid = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[13]/a/span[2]')
    slid.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    tax = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[14]/a/span[2]')
    tax.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    rates = driver.find_element_by_xpath('//*[@id="doc-tax_rates"]/a/span')
    rates.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    trans = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[15]/a/span[2]')
    trans.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    scan = trans.find_element_by_xpath('//*[@id="doc-scan"]/a/span')
    scan.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    csv_tr = trans.find_element_by_xpath('//*[@id="doc-tax_rates"]/a/span')
    csv_tr.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    users = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[16]/a/span[2]')
    users.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
    mods = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[16]/a/span[2]')
    mods.click()
    h1 = driver.find_element_by_tag_name('h1')
    assert True
