import allure
import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.shopping_cart import ShoppingCart


@pytest.mark.usefixtures("get_driver")
@pytest.mark.cart
class TestShoppingCart:

    @pytest.mark.positive
    @allure.feature('Cart')
    @allure.story('Search product')
    def test_shopping_cart_is_empty_by_default(self):
        home_page = HomePage(self.driver, self.wait)
        shopping_cart = ShoppingCart(self.driver, self.wait)
        with allure.step('Open browser'):
            home_page.open_browser()
        with allure.step('Navigate to shopping cart'):
            home_page.navigate_to_shopping_cart()
        with allure.step('Verify that the shopping cart is empty'):
            shopping_cart.check_is_cart_empty()

    @pytest.mark.positive
    @allure.feature('Cart')
    @allure.story('Add goods to shopping cart')
    def test_add_goods_to_shopping_cart(self):
        home_page = HomePage(self.driver, self.wait)
        shopping_cart = ShoppingCart(self.driver, self.wait)
        search_results_page = SearchResultsPage(self.driver, self.wait, self.act)
        with allure.step('Open browser'):
            home_page.open_browser()
        with allure.step('Search product'):
            home_page.search_amazon('#SteelSeries Arctis')
        with allure.step('Add goods to shopping cart'):
            items = search_results_page.add_to_cart()
        with allure.step('Navigate to shopping cart'):
            home_page.navigate_to_shopping_cart(True)
        with allure.step('Verify that the product is added to shopping cart'):
            shopping_cart.check_is_cart_full(items)

    @pytest.mark.positive
    @allure.feature('Cart')
    @allure.story('Delete goods from shopping cart')
    def test_delete_goods_from_shopping_cart(self):
        home_page = HomePage(self.driver, self.wait)
        shopping_cart = ShoppingCart(self.driver, self.wait)
        search_results_page = SearchResultsPage(self.driver, self.wait, self.act)
        with allure.step('Open browser'):
            home_page.open_browser()
        with allure.step('Search product'):
            home_page.search_amazon('#SteelSeries Arctis')
        with allure.step('Add goods to shopping cart'):
            items = search_results_page.add_to_cart()
        with allure.step('Navigate to shopping cart'):
            home_page.navigate_to_shopping_cart(True)
        with allure.step('Check that the products are added to shopping cart'):
            shopping_cart.check_is_cart_full(items)
        with allure.step('Delete first item from shopping cart'):
            shopping_cart.delete_first_item_from_shopping_cart()
        with allure.step('Verify that the product is deleted from shopping cart'):
            shopping_cart.check_is_cart_full(items - 1)
        with allure.step('Delete all items from shopping cart'):
            shopping_cart.delete_all_items_from_shopping_cart()
        with allure.step('Verify that the all items are deleted from shopping cart'):
            shopping_cart.check_is_cart_empty()
