from .base_page import BasePage
from .locators import MainPageLocators
from .product_page import ProductPage


class MainPage(BasePage):


    def go_to_login_page(self):

        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()   
        #return LoginPage(self.browser, self.browser.current_url)  //Использован другой подход работы с методом should_be_login_page
        #alert = self.browser.switch_to.alert
        #alert.accept()  // Если будет добавлено окно с предупреждением, спрашивабще о подтверждении перехода на страницу


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"