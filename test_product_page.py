from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear "
    product_page = ProductPage(browser, link)
    product_page.open()
    time.sleep(1) #Использованы ожидания, чтобы видеть как проходит тест
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    time.sleep(1)
    product_page.should_coincidence_book_names()
    product_page.should_coincidence_book_prices()