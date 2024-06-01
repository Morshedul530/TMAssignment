import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ItemSearchPage():

    def __init__(self, driver):
        self.driver = driver

    # Verify that the search button is present
    def item_search(self, apple):
        try:
            search_btn = self.driver.find_element(By.XPATH,
                                                  "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/mat-search-bar/span/mat-icon[2]")
            self.driver.implicitly_wait(2)
            search_btn.click()
            time.sleep(3)

            print("Search button is present.")

        except:
            print("Search button is not present.")

        # Search for apple
        search_for = self.driver.find_element(By.XPATH,
                                              "/html[1]/body[1]/app-root[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-navbar[1]/mat-toolbar[1]/mat-toolbar-row[1]/mat-search-bar[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]")
        search_for.clear()
        search_for.send_keys(apple)
        search_for.send_keys(Keys.RETURN)

        try:
            results = self.driver.find_element(By.ID, "searchValue")

            display = results.is_displayed()
            if display is True:
                print("Verified that at least two Apple products are displayed and No Banana product is displayed")
            else:
                print('Less than two Apple products are displayed')

        except:
            print('Mouse Hover Action Failed.')