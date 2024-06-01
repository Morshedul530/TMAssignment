import time

from selenium.webdriver.common.by import By


class ItemSelectionPage():

    def __init__(self, driver):
        self.driver = driver

    def item_selection(self):

        try:
            add_to_basket = self.driver.find_element(By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-search-result[1]/div[1]/div[1]/div[2]/mat-grid-list[1]/div[1]/mat-grid-tile[1]/div[1]/mat-card[1]/div[2]/button[1]/span[1]/span[1]")
            self.driver.implicitly_wait(2)
            add_to_basket.click()
            time.sleep(2)

            your_basket = self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[4]/span[1]/span[1]")
            your_basket.click()
            time.sleep(2)

            checkout = self.driver.find_element(By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-basket[1]/mat-card[1]/button[1]")
            checkout.click()
            time.sleep(2)

            add_new_address = self.driver.find_element(By.XPATH,
                                                "/html[1]/body[1]/app-root[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-address-select[1]/div[1]/app-address[1]/mat-card[1]/div[1]/button[1]/span[1]/span[1]")
            add_new_address.click()
            time.sleep(2)

        except:
            print('Mouse Hover Action Failed.')
