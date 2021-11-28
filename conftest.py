import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




@pytest.fixture(scope="function")
def browser(request):
    # user_language = request.config.getoption("language")
    options = Options()
    # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\n start Chrome browser for test ...")
    browser = webdriver.Chrome(executable_path="C:\\CD\\chromedriver.exe", options=options)
    browser.maximize_window()
    browser.implicitly_wait(7)
    yield browser
    print("\nquit browser..")
    browser.quit()

