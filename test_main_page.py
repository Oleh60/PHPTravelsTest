from .pages.base_page import BasePage
from .pages.signup_page import SignupPage
import time


class TestMainPage():

    def test_user_see_register_from(self,browser):
        page = SignupPage(browser)
        page.open()
        page.go_to_signup_page()
        # time.sleep(3)
        page.should_be_signup_form()



