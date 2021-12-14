from .pages.base_page import BasePage
from .pages.signup_page import SignupPage
from .pages.main_page import MainPage
import pytest
import time


class TestMainPage():

    def test_user_must_see_contact_phone_number(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_see_contact_number()

    def test_user_must_see_contact_email(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_see_contact_email()

    def test_user_press_hotel_btn(self, browser):
        page = MainPage(browser)
        page.open()
        page.pressing_hotel_button()
        page.should_be_on_hotels_page()

    def test_user_press_flights_btn(self,browser):
        page = MainPage(browser)
        page.open()
        page.pressing_flights_button()
        page.should_be_on_flights_page()

    def test_user_press_tours_btn(self,browser):
        page = MainPage(browser)
        page.open()
        page.pressing_tours_button()
        page.shold_be_on_tours_page()

    def test_user_press_cars_btn(self,browser):
        page = MainPage(browser)
        page.open()
        page.pressing_cars_button()
        page.should_be_on_cars_page()

    def test_user_press_visa_btn(self,browser):
        page = MainPage(browser)
        page.open()
        page.pressing_visa_button()
        page.should_be_on_visa_page()

    def test_user_press_blog_btn(self,browser):
        page = MainPage(browser)
        page.open()
        page.pressing_blog_button()
        page.should_be_on_blog_page()

    @pytest.mark.xfail(reason ="for unknown reason locators not working")
    def test_user_press_aboutus_btn(self,browser):
        page = MainPage(browser)
        page.open()
        page.pressing_aboutus_btn()
        page.should_be_on_aboutus_page_text_present()

    @pytest.mark.xfail(reason ="for unknown reason locators not working")
    def test_user_press_termsofuse_btn(self,browser):
        page = MainPage(browser)
        page.open()
        page.pressing_termsofuse_btn()
        page.should_be_on_termsofuse_page_text_present()

    @pytest.mark.xfail(reason ="for unknown reason locators not working")
    def test_user_press_FAQ_btn(self,browser):
        page = MainPage(browser)
        page.open()
        page.pressing_FAQ_btn()
        page.should_be_on_FAQ_page_text_present()

    def test_quick_order_tab_is_present(self,browser):
        page = MainPage(browser)
        page.open()
        page.should_see_quick_order_tab()

    #test only on presentation because hotel button is open by default
    def test_hotels_tab_is_present(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_see_hotels_tab()


    def test_flights_tab_is_present_and_clickable(self, browser):
        page = MainPage(browser)
        page.open()
        page.pressing_flights_tab()
        page.should_be_on_flights_tab()


    def test_tours_tab_is_present_and_clickable(self, browser):
        page = MainPage(browser)
        page.open()
        page.pressing_tours_tab()
        page.should_be_on_tours_tab()


    def test_cars_tab_is_present_and_clickable(self, browser):
        page = MainPage(browser)
        page.open()
        page.pressing_cars_tab()
        page.should_be_on_cars_tab()


    def test_visa_tab_is_present_and_clickable(self, browser):
        page = MainPage(browser)
        page.open()
        page.pressing_visa_tab()
        time.sleep(4)
        page.should_be_on_visa_tab()




