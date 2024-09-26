import logging
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class HomePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_browser(self):
        self.driver.get('https://www.amazon.com/')
        try:
            self.wait.until(ec.presence_of_element_located((By.ID, 'nav-logo-sprites')))
        except TimeoutException as ex:
            logging.info(str(ex) + 'Home page is not displayed')
            self.wait.until(ec.presence_of_element_located((By.XPATH,
            '//a[@onclick="window.location.reload()"]'))).click()


    def navigate_to_shopping_cart(self, is_pop_up=False):
        if is_pop_up is True:
            pop_up = self.driver.find_element(By.CLASS_NAME, 'a-changeover-inner')
            while pop_up.is_displayed():
                time.sleep(3)
        self.driver.find_element(By.ID, 'nav-cart').click()
        self.wait.until(ec.presence_of_element_located((By.TAG_NAME, 'h2')))

    def search_amazon(self, text):
        self.wait.until(ec.presence_of_element_located((By.ID, 'nav-logo-sprites')))
        search_field = self.driver.find_element(By.CLASS_NAME, 'nav-search-field ')
        search_field.click()
        ac_field = self.driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
        ac_field.send_keys(text)
        self.driver.find_element(By.ID, 'nav-search-submit-button').click()
        self.wait.until(
            ec.presence_of_element_located((By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')))
