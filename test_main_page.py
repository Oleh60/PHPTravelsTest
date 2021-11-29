from .pages.base_page import BasePage
from .pages.signup_page import SignupPage
from .pages.main_page import MainPage
import time


class TestMainPage():

    def test_user_must_see_contact_phone_number(self,browser):
        page = MainPage(browser)
        page.open()
        page.should_see_contact_number()


    def test_user_must_see_contact_email(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_see_contact_email()


    def test_user_press_hotel_btn(self,browser):
        page = MainPage(browser)
        page.open()
        page.pressing_hotel_button()
        page.should_be_on_hotels_page()

