from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def basket_should_be_present(browser):
    try:
        browser.find_element(By.CSS_SELECTOR,"button.btn-add-to-basket")
        return True
    except NoSuchElementException:
        return False

def test_basket_shuld_be_visible(browser):
    browser.get(link)
    time.sleep(5)
    assert basket_should_be_present(browser), "Basket element shuld be present."