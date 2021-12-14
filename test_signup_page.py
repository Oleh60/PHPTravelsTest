import pytest
import time
from .pages.base_page import BasePage
from .pages.signup_page import SignupPage



class TestSignupForm():


    def test_signup_form_should_exists(self,browser):
        page = SignupPage(browser)
        page.open()
        page.go_to_signup_page()
        page.should_be_signup_form()



    def test_user_registration_step(self, browser):
        page = SignupPage(browser)
        page.open()
        page.go_to_signup_page()
        firstname_text = "User" + str(time.time())
        email = str(time.time()) + "FakeEmail@google.com"
        password = "3434567"
        page.create_valid_user(email, password, firstname_text)
        page.user_login(email, password)
        page.should_see_firstname_in_dashboard(firstname_text)
