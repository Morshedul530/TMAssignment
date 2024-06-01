import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from pages.login_page import LoginPage
from pages.add_new_address_page import AddNewAddressPage
from pages.item_add_page import ItemSelectionPage


class Item_SelectionTest(unittest.TestCase):

    def test_item_selection(self):
        baseURL = "https://juice-shop.herokuapp.com/#/login"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(2)

        lp = LoginPage(driver)
        lp.login_shop("testsqa50@gmail.com", "123456")

        isp = ItemSelectionPage(driver)
        isp.item_selection()

        new = AddNewAddressPage(driver)
        new.add_new_address('Bangladesh', 'MR. XYZ', '01725147485', '1250', 'Sector-12', 'Dhaka', 'ABC')

