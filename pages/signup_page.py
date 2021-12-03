from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import SignupPageLocator
import time


class SignupPage(BasePage):
    def should_be_signup_page(self):
        self.should_be_signup_page()

    def go_to_signup_page(self):
        link = self.browser.find_element(*SignupPageLocator.SIGNUPBUT_LOCATOR)
        link.click()

    def should_be_signup_form(self):
        assert self.is_element_present(*SignupPageLocator.SIGNUPFORM_LOCATOR), "This is not Signup page"

    def input_user_data_to_signup_form(self, firstname_text, lastname_text, phone, email_text, password_text):
        first_name = self.browser.find_element(*SignupPageLocator.SIGNUP_FIRSTNAME_LOCATOR)
        first_name.send_keys(firstname_text)
        last_name = self.browser.find_element(*SignupPageLocator.SIGNUP_LASTNAME_LOCATOR)
        last_name.send_keys(lastname_text)
        phone_form = self.browser.find_element(*SignupPageLocator.Phone_LOCATOR)
        phone_form.send_keys(phone)
        email = self.browser.find_element(*SignupPageLocator.SIGNUP_EMAIL_LOCATOR)
        email.send_keys(email_text)
        password = self.browser.find_element(*SignupPageLocator.SIGNUP_PASSWORD_LOCATOR)
        password.send_keys(password_text)
        signup_btn = self.browser.find_element(*SignupPageLocator.SIGNUP_BTN_LOCATOR)
        signup_btn.click()

    def create_valid_user(self, email, password, firstname_text):
        lastname_text = "text_lastname"
        phone = "+123456789"
        self.input_user_data_to_signup_form(firstname_text, lastname_text, phone, email, password)

    def create_invalid_user(self):
        firstname_text = "text_firstname"
        lastname_text = "text_lastname"
        phone = "+123456789"
        email_text = "test_email"
        password_text = "test_paSSword"
        self.input_user_data_to_signup_form(firstname_text, lastname_text, phone, email_text, password_text)

    def should_see_registration_is_complete(self):
        assert self.is_element_present(*SignupPageLocator.SIGNUP_SUCCSES_LOCATOR), "Registration is not complete"

    def user_login(self, email, password):
        email_field = self.browser.find_element(*SignupPageLocator.SIGNUP_EMAIL_LOCATOR)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*SignupPageLocator.SIGNUP_PASSWORD_LOCATOR)
        password_field.send_keys(password)
        login_btn = self.browser.find_element(*SignupPageLocator.LOGIN_BTN_LOCATOR)
        login_btn.click()

    def should_see_firstname_in_dashboard(self, firstname_text):
        assert self.is_element_present(By.XPATH, f'//span[text()= "{firstname_text}"]')
