from .base_page import BasePage
from .locators import LoginPageLocators
from .main_page import MainPage
from selenium import webdriver



class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

        # реализуйте проверку на корректный url адрес
    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "URL does not contain 'login'"

    def should_be_login_form(self): 
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"