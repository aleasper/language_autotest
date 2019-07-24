from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'

def test_find_btn_basket(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".btn-add-to-basket")
