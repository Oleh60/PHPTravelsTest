from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from .locators import MainPageLocatorHeader
from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):

    def should_see_contact_number(self):
        assert self.is_element_present(*MainPageLocatorHeader.CONTACT_PHONE_LOCATOR), "User can't see phone number or number " \
                                                                                "is incorrect"

    def should_see_contact_email(self):
        assert self.is_element_present(*MainPageLocatorHeader.CONTACT_EMAIL_LOCATOR), "User can't see email address ot it's " \
                                                                                "incorrect"

    def pressing_hotel_button(self):
        link = self.browser.find_element(*MainPageLocatorHeader.HOTEL_BUTN_LOCATOR)
        link.click()

    def should_be_on_hotels_page(self):
        assert self.is_element_present(*MainPageLocatorHeader.HOTEL_PAGE_MAIN_TEXT_LOCATOR), "User is not on Hotels page"


    def pressing_flights_button(self):
        link = self.browser.find_element(*MainPageLocatorHeader.FLIGHTS_BTN_LOCATOR)
        link.click()


    def should_be_on_flights_page(self):
        assert self.is_element_present(*MainPageLocatorHeader.FLIGHTS_PAGE_MAIN_TEXT_LOCATOR),"User is not on Flights page"


    def pressing_tours_button(self):
        link = self.browser.find_element(*MainPageLocatorHeader.TOURS_BTN_LOCATOR)
        link.click()

    def shold_be_on_tours_page(self):
        assert self.is_element_present(*MainPageLocatorHeader.TOURS_PAGE_MAIN_LOCATOR), "User is not on Tours page"


    def pressing_cars_button(self):
        link = self.browser.find_element(*MainPageLocatorHeader.CARS_BTN_LOCATOR)
        link.click()

    def should_be_on_cars_page(self):
        assert self.is_element_present(*MainPageLocatorHeader.CARS_PAGE_MAIN_TEXT_LOCATOR), "User is not on Cars page"

    def pressing_visa_button(self):
        link = self.browser.find_element(*MainPageLocatorHeader.VISA_BTN_LOCATOR)
        link.click()

    def should_be_on_visa_page(self):
        assert self.is_element_present(*MainPageLocatorHeader.VISA_PAGE_MAIN_TEXT_LOCATOR), "User is not on Visa page"

    def pressing_blog_button(self):
        link = self.browser.find_element(*MainPageLocatorHeader.BLOG_BTN_LOCATOR)
        link.click()

    def should_be_on_blog_page(self):
        assert  self.is_element_present(*MainPageLocatorHeader.BLOG_PAGE_MAIN_TEXT_LOCATOR), "User is not on Blog page"


    def pressing_aboutus_btn(self):
        element_hover_over = self.browser.find_element(*MainPageLocatorHeader.COMPANY_DROPDOWN_LOCATOR)
        hover = ActionChains(self.browser).move_to_element(element_hover_over)
        hover.perform()
        time.sleep(8)
        link = self.browser.find_element(*MainPageLocatorHeader.ABOUTUS_COMPANY_BTN)
        link.click()

    def should_be_on_aboutus_page_text_present(self):
        assert self.is_element_present(*MainPageLocatorHeader.ABOUTUS_PAGE_MAIN_TEXT), "User is not on about us page,or " \
                                                                                       "text is not present"

    def pressing_termsofuse_btn(self):
        element_hover_over = self.browser.find_element(*MainPageLocatorHeader.COMPANY_DROPDOWN_LOCATOR)
        hover = ActionChains(self.browser).move_to_element(element_hover_over)
        hover.perform()
        link = self.browser.find_element(*MainPageLocatorHeader.TERMSOFUSE_COMPANY_BTN)
        link.click()

    def should_be_on_termsofuse_page_text_present(self):
        assert self.is_element_present(*MainPageLocatorHeader.TERMSOFUSE_PAGE_MAIN_TEXT),"User is not on Terms of use page" \
                                                                                         "or text is not present "

    def pressing_FAQ_btn(self):
        element_hover_over = self.browser.find_element(*MainPageLocatorHeader.COMPANY_DROPDOWN_LOCATOR)
        hover = ActionChains(self.browser).move_to_element(element_hover_over)
        hover.perform()
        link = self.browser.find_element(*MainPageLocatorHeader.FAQ_COMPANY_BTN)
        link.click()

    def should_be_on_FAQ_page_text_present(self):
        assert self.is_element_present(*MainPageLocatorHeader.FAQ_PAGE_MAIN_TEXT), "User is not on FAQ page or text is " \
                                                                                   "not present"