import time

import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.shopping_cart import ShoppingCart


@pytest.mark.usefixtures("get_driver")
class TestShoppingCart:

    def test_shopping_cart_is_empty_by_default(self):
        home_page = HomePage(self.driver, self.wait)
        shopping_cart = ShoppingCart(self.driver, self.wait)
        home_page.open_browser()
        home_page.navigate_to_shopping_cart()
        shopping_cart.check_is_cart_empty()

    def test_add_goods_to_shopping_cart(self):
        home_page = HomePage(self.driver, self.wait)
        shopping_cart = ShoppingCart(self.driver, self.wait)
        search_results_page = SearchResultsPage(self.driver, self.wait, self.act)
        home_page.open_browser()
        home_page.search_amazon('#SteelSeries Arctis')
        items = search_results_page.add_to_cart()
        home_page.navigate_to_shopping_cart(True)
        shopping_cart.check_is_cart_full(items)

    def test_delete_goods_from_shopping_cart(self):
        home_page = HomePage(self.driver, self.wait)
        shopping_cart = ShoppingCart(self.driver, self.wait)
        search_results_page = SearchResultsPage(self.driver, self.wait, self.act)
        home_page.open_browser()
        home_page.search_amazon('#SteelSeries Arctis')
        items = search_results_page.add_to_cart()
        home_page.navigate_to_shopping_cart(True)
        shopping_cart.check_is_cart_full(items)
        shopping_cart.delete_first_item_from_shopping_cart()
        shopping_cart.check_is_cart_full(items - 1)
        shopping_cart.delete_all_items_from_shopping_cart()
        shopping_cart.check_is_cart_empty()
