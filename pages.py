from elements import BasePageElement
from locators import MainPageLocators

class SearchTextElement(BasePageElement):
    locator = 'businessSearch'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "ПриватМаркет" in self.driver.title

    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.Search_button)
        element.click()


class SearchResultsPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source