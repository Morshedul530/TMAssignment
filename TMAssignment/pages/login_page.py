import time
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_shop(self, email, password):
        email_address = self.driver.find_element(By.ID, "email")
        email_address.clear()
        email_address.send_keys(email)
        time.sleep(1)

        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)
        time.sleep(1)

        login_button = self.driver.find_element(By.ID, "loginButton")
        login_button.click()
        time.sleep(2)
