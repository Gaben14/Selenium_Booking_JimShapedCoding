# This file will include a class with instance methods.
# That will be responsible to interact with our website
# After we have some results, to apply filtrations.
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, star_value):
        # star_filtration_box = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[4]')
        # To be able to filter for the child elements of a parent item, you need to assign
        # the parent for find_ or other methods as below:
        # star_child_element = self.driver.find_element(By.CSS_SELECTOR, f'input[name="class={star_value}"]')
        # star_child_element = self.driver.find_element(By.CSS_SELECTOR, f'div[data-filters-item="class:class={star_value}"]')
        star_child_element = self.driver.find_element(By.XPATH,f'//*[text()="{star_value} stars"]')
        # self.find_element(By.XPATH,f'//*[text()="{currency}"]')
        # div[data-filters-item="class:class=5"]
        star_child_element.click()

