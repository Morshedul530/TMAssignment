import time
from selenium.webdriver.common.by import By


class AddNewAddressPage():

    def __init__(self, driver):
        self.driver = driver

    def add_new_address(self, country, name, mobile, zipcode, address, city, state):
        count = self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-address-create/div/mat-card/div[1]/mat-form-field[1]/div/div[1]/div[3]/input")
        count.clear()
        count.send_keys(country)

        nam = self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-address-create/div/mat-card/div[1]/mat-form-field[2]/div/div[1]/div[3]/input")
        nam.clear()
        nam.send_keys(name)

        phone = self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-address-create/div/mat-card/div[1]/mat-form-field[3]/div/div[1]/div[3]/input")
        phone.clear()
        phone.send_keys(mobile)

        code = self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-address-create/div/mat-card/div[1]/mat-form-field[4]/div/div[1]/div[3]/input")
        code.clear()
        code.send_keys(zipcode)

        address_field = self.driver.find_element(By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-address-create[1]/div[1]/mat-card[1]/div[1]/mat-form-field[5]/div[1]/div[1]/div[3]/textarea[1]")
        address_field.clear()
        address_field.send_keys(address)

        city_field = self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-address-create/div/mat-card/div[1]/mat-form-field[6]/div/div[1]/div[3]/input")
        city_field.clear()
        city_field.send_keys(city)

        state_field = self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-address-create/div/mat-card/div[1]/mat-form-field[7]/div/div[1]/div[3]/input")
        state_field.clear()
        state_field.send_keys(state)

        submit_button = self.driver.find_element(By.ID, "submitButton")
        submit_button.click()
        time.sleep(2)
