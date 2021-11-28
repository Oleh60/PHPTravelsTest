from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from .locators import SignupPageLocator

class BasePage():

    def __init__(self, browser):

        self.browser = browser
        self.link = "https://www.phptravels.net/"



    def open(self):
        self.browser.get(self.link)



    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return False
        return True


    def go_to_signup_page(self):
        link = self.browser.find_element(*SignupPageLocator.SIGNUPBUT_LOCATOR)
        link.click()

