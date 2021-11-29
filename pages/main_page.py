from selenium.webdriver.common.by import By

from .locators import MainPageLocator
from .base_page import BasePage

class MainPage(BasePage):

    def should_see_contact_number(self):



        assert self.is_element_present(*MainPageLocator.CONTACT_PHONE_LOCATOR), "User can't see phone number or number " \
                                                                                "is incorrect"


    def should_see_contact_email(self):

        assert  self.is_element_present(*MainPageLocator.CONTACT_EMAIL_LOCATOR), "User can't see email address ot it's " \
                                                                                 "incorrect"


    def pressing_hotel_button(self):

        link = self.browser.find_element(*MainPageLocator.HOTEL_BUTN_LOCATOR)
        link.click()


    def should_be_on_hotels_page(self):

        assert self.is_element_present(*MainPageLocator.HOTEL_PAGE_MAIN_TEXT_LOCATOR),"User is not on Hotels page"