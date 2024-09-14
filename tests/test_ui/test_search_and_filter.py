import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


@pytest.mark.usefixtures("get_driver")
class TestSearchFilter:

    def test_search(self):
        home_page = HomePage(self.driver, self.wait)
        search_results_page = SearchResultsPage(self.driver, self.wait, self.act)
        home_page.open_browser()
        home_page.search_amazon('Nothing Phone')
        search_results_page.check_is_product_found('Nothing Phone')

    def test_product_filter_by_price(self):
        home_page = HomePage(self.driver, self.wait)
        search_results_page = SearchResultsPage(self.driver, self.wait, self.act)
        home_page.open_browser()
        home_page.search_amazon('Nothing Phone')
        search_results_page.change_prices_range()
        search_results_page.check_are_prices_in_range()

    def test_product_filter_by_brands(self):
        home_page = HomePage(self.driver, self.wait)
        search_results_page = SearchResultsPage(self.driver, self.wait, self.act)
        home_page.open_browser()
        home_page.search_amazon('Nothing Phone')
        search_results_page.set_first_brand()
