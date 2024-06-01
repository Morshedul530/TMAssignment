import unittest


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from pages.login_page import LoginPage
from pages.search_page import ItemSearchPage


class LoginTest(unittest.TestCase):

    def test_search(self):
        baseURL = "https://juice-shop.herokuapp.com/#/login"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(2)

        sp = ItemSearchPage(driver)
        sp.item_search("apple")
        time.sleep(2)







