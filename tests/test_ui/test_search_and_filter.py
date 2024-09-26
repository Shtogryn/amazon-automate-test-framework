import pytest
import allure
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

@pytest.mark.usefixtures("get_driver")
@pytest.mark.searchfilter
class TestSearchFilter:

    @pytest.mark.search
    @allure.feature('Search')
    @allure.story('Search product')
    def test_search(self):
        home_page = HomePage(self.driver, self.wait)
        search_results_page = SearchResultsPage(self.driver, self.wait, self.act)
        with allure.step('Open browser'):
            home_page.open_browser()
        with allure.step('Search product'):
            home_page.search_amazon('Nothing Phone')
        with allure.step('Verify that product is found'):
            search_results_page.check_is_product_found('Nothing Phone')

    @pytest.mark.filter
    @allure.feature('Filter')
    @allure.story('Filter products by price')
    def test_product_filter_by_price(self):
        home_page = HomePage(self.driver, self.wait)
        search_results_page = SearchResultsPage(self.driver, self.wait, self.act)
        with allure.step('Open browser'):
            home_page.open_browser()
        with allure.step('Search product'):
            home_page.search_amazon('Nothing Phone')
        with allure.step('Change prices range'):
            search_results_page.change_prices_range()
        with allure.step('Verify that the products are displayed with prices in correct range'):
            search_results_page.check_are_prices_in_range()

    @pytest.mark.filter
    @allure.feature('Filter')
    @allure.story('Filter products by brand')
    def test_product_filter_by_brands(self):
        home_page = HomePage(self.driver, self.wait)
        search_results_page = SearchResultsPage(self.driver, self.wait, self.act)
        with allure.step('Open browser'):
            home_page.open_browser()
        with allure.step('Search product'):
            home_page.search_amazon('Nothing Phone')
        with allure.step('Set first brand'):
            search_results_page.set_first_brand()
        with allure.step('Verify that the products are displayed of one brand name'):
            search_results_page.check_are_goods_same_brand('Nothing Phone')
