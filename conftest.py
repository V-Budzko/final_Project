import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en",
        help="Choose language: en or other supported language codes"
    )

@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение параметра language
    user_language = request.config.getoption("language")
    
    # Настройки Firefox
    options = Options()
    options.set_preference("intl.accept_languages", user_language)
    options.set_preference("browser.cache.disk.enable", False)  # Отключаем кэш браузера и все остальное
    options.set_preference("browser.cache.memory.enable", False) # Потому что браузер запускал страницу на русском языке, 
    options.set_preference("browser.cache.offline.enable", False) # Не смотря на передаваемый ему параметр
    options.set_preference("network.http.use-cache", False)
    
    print(f"\nЗапуск браузера Firefox с языком '{user_language}' для теста..")
    browser = webdriver.Firefox(options=options)
    
    yield browser
    
    print("\nЗакрытие браузера..")
    browser.quit()
