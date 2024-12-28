from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "a#registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner p strong")
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")