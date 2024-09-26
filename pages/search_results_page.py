import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class SearchResultsPage:
    def __init__(self, driver, wait, actions):
        self.driver = driver
        self.wait = wait
        self.actions = actions

    def check_is_product_found(self, expected_text):
        list_goods = self.driver.find_element(By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"][1]')
        assert expected_text in list_goods.text

    def change_prices_range(self):
        lower_bound = self.driver.find_element(By.ID, 'p_36/range-slider_slider-item_lower-bound-slider')
        upper_bound = self.driver.find_element(By.ID, 'p_36/range-slider_slider-item_upper-bound-slider')
        action = self.actions.move_to_element(lower_bound)
        action.perform()
        time.sleep(1)
        action = self.actions.move_to_element(upper_bound)
        action.perform()
        time.sleep(1)

    def set_first_brand(self):
        self.driver.find_element(By.XPATH, '//*[@id="p_123/424137"]/span/a/div/label/i').click()
        self.wait.until(
            ec.presence_of_element_located((By.XPATH, '//h2[@class="a-size-mini a-spacing-none a-color-base '
                                                      's-line-clamp-4"]')))
        first_checkbox = self.driver.find_element(By.XPATH, '//input[@type = "checkbox"]')
        while not first_checkbox.is_selected():
            self.driver.implicitly_wait(1)

    def check_are_prices_in_range(self):
        lower_price = self.driver.find_element(By.XPATH, '//*[@id="p_36/range-slider"]/form/div[1]/label[1]/span')
        high_price = self.driver.find_element(By.XPATH, '//*[@id="p_36/range-slider"]/form/div[1]/label[2]/span')
        slider_min_value = int(lower_price.text[1::])
        slider_max_value = int(high_price.text[1:-1])
        prices = self.driver.find_elements(By.XPATH, '//span[@class="a-color-base"]')
        for p in prices:
            price = int(round(float(p.text[1:-1])))
            assert slider_min_value <= price <= slider_max_value, f"Price {price} is out of range!"

    def add_to_cart(self) -> int:
        buttons: list = self.driver.find_elements(By.XPATH, '//button[@class= "a-button-text"]')
        cnt = len(buttons)
        for button in buttons:
            button.click()
            self.wait.until(
                ec.presence_of_element_located((By.CLASS_NAME, 'a-changeover-inner')))
        return cnt

    def check_are_goods_same_brand(self, expected_name):
        list_goods = self.driver.find_elements(By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')
        for i in list_goods:
            assert expected_name in i.text
        self.driver.implicitly_wait(1)
