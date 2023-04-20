import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# By using the webdriver as a class parameter, we can now access all the functions
# from the webdriver with self.
class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Selenium", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        # Because we used the webdriver.Chrome as a parameter,
        # we can now use the implicitly_wait
        self.implicitly_wait(25)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()
        # time.sleep(5)

        selected_currency_element = self.find_element(By.XPATH,
                                                      f'//button[@data-testid="selection-item"] //div[text()="{currency}"]')
        # The *[] means all items should be checked
        # If you need to check only specific HTML tags - use it like this: div[]
        selected_currency_element.click()

        # time.sleep(5)

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.CSS_SELECTOR, 'input[name="ss"')
        search_field.clear()
        search_field.send_keys(place_to_go)

        # Select the first result
        first_result = self.find_element(By.CSS_SELECTOR, 'ul[data-testid="autocomplete-results"] > li:nth-child(1)')
        first_result.click()

        time.sleep(5)

    # Teardown
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
