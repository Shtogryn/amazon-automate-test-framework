import time
import allure

from selenium.webdriver.common.by import By

class ShoppingCart:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def delete_first_item_from_shopping_cart(self):
        with allure.step('Delete first item from shopping cart'):
            self.driver.find_element(By.XPATH, '//input[@value="Delete"][1]').click()
            time.sleep(2)

    def delete_all_items_from_shopping_cart(self):
        with allure.step('Delete all items from shopping cart'):
            items = self.driver.find_elements(By.XPATH, '//input[@value="Delete"]')
        for item in items:
            item.click()
            self.driver.implicitly_wait(2)

    def check_is_cart_empty(self):
        with allure.step('Verify that the all items are deleted from shopping cart'):
            txt = self.driver.find_element(By.TAG_NAME, 'h2')
            assert txt.is_displayed() is True
            assert txt.text == 'Your Amazon Cart is empty'

    def check_is_cart_full(self, items):
        with allure.step('Check that the products are added to shopping cart'):
            cart_items= self.driver.find_elements(By.CLASS_NAME, 'a-truncate-cut')
            assert len(cart_items) == items, f"Actually {len(cart_items)} "
