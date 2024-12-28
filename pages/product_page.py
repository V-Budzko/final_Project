from selenium.webdriver.ie.webdriver import WebDriver
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductPage(BasePage):

    def should_be_product_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_ON_PAGE), "Product name is not presented" 

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
    
    def should_coincidence_book_names(self):
        time.sleep(1)
      #Используем явные ожидание, чтобы тест не спешил искать элемент и не выдалавал исключение
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        book_name_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE).text
        assert book_name_in_basket == book_name_on_page, "Book names are not equal"

    def should_coincidence_book_prices(self):
        time.sleep(1)
        book_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        book_price_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE).text
        assert book_price_in_basket == book_price_on_page, "Book prices are not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapered_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"