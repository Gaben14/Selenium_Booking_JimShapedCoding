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

    # Each method is different test case.
    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()

        selected_currency_element = self.find_element(By.XPATH,
                                                      f'//button[@data-testid="selection-item"] //div[text()="{currency}"]')
        # The *[] means all items should be checked
        # If you need to check only specific HTML tags - use it like this: div[]
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.CSS_SELECTOR, 'input[name="ss"')
        search_field.clear()
        search_field.send_keys(place_to_go)

        # Select the first result
        first_result = self.find_element(By.CSS_SELECTOR, 'ul[data-testid="autocomplete-results"] > li:nth-child(1)')
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count=1):
        # 1. Click on the button so that adult config is visible.
        selection_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
        selection_element.click()

        # 2. Decrease the Adults count to the minimum (1) on the page
        # We need to get the current value, and decrease it until it reaches 1.
        while True:
            decrease_adults_element = self.find_element(By.XPATH,
                                                        '//div[@data-testid="occupancy-popup"]/div/div/div[2]/button[1]')
            decrease_adults_element.click()
            # If the value of adults == 1, then the loop should stop.
            adults_value_element = self.find_element(By.XPATH,
                                                     '//div[@data-testid="occupancy-popup"]/div/div/div[2]/span')
            adults_value = int(adults_value_element.text)

            if adults_value == 1:
                break

        # 3. Locate the increase button and increase the amount of users to a specific number.
        # The loop should run until it's specified in the method / function call.
        increase_button_element = self.find_element(By.XPATH,
                                                    '//div[@data-testid="occupancy-popup"]/div/div/div[2]/button[2]')
        # Because the default value at booking.com is 1, we need to subtract 1 from the count variable.
        for _ in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_btn = self.find_element(By.CSS_SELECTOR, 'button[type="submit"')
        search_btn.click()

    # Teardown
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
