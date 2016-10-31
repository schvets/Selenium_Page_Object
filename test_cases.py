import unittest
from selenium import webdriver
import pages

class PrivatMarketSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://privatmarket.ua")

    def test_search_in_privatmarket(self):
        main_page = pages.MainPage(self.driver)

        assert main_page.is_title_matches(), "ПриватМаркет title doesn't match."

        main_page.search_text_element = "ШКАФ"
        main_page.click_search_button()

        search_results_page = pages.SearchResultsPage(self.driver)

        assert search_results_page.is_results_found(), "По запросу «шкаф» найдено"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()