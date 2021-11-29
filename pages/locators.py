from selenium.webdriver.common.by import By

class SignupPageLocator():
    SIGNUPBUT_LOCATOR = (By.XPATH, "//a[@href = 'https://www.phptravels.net/signup']")

    SIGNUPFORM_LOCATOR = (By.XPATH, "//div[@class = 'modal-content col align-self-center']")

    SIGNUP_FIRSTNAME_LOCATOR = (By.XPATH, '//input[@placeholder = "First Name"]')

    SIGNUP_LASTNAME_LOCATOR = (By.XPATH, '//input[@placeholder = "Last Name"]')

    Phone_LOCATOR = (By.XPATH, '//input[@placeholder = "Phone"]')

    SIGNUP_EMAIL_LOCATOR = (By.XPATH, '//input[@placeholder = "Email"]')

    SIGNUP_PASSWORD_LOCATOR = (By.XPATH, '//input[@placeholder = "Password"]')

    ACCOUNT_TYPE_LOCATOR = (By.XPATH, '//span[@id = "select2-account_type-container"]')

    ACCOUNT_TYPE_CUSTUMER_LOCATOR = (By.XPATH, '//Input[@Aria-Activedescendant = "Select2-Account_type-Result-Hjze-Customers"]')

    SIGNUP_BTN_LOCATOR = (By.XPATH, '//button[@type ="submit"]')

    SIGNUP_SUCCSES_LOCATOR  = (By.XPATH, '//h5[contains(text(), "Login")]')

    LOGIN_BTN_LOCATOR = (By.XPATH,'//button/span[text() = "Login"]/..')

class MainPageLocator():

    CONTACT_PHONE_LOCATOR = (By.XPATH, '//a[@href = "tel:+1-234-56789"]')

    CONTACT_EMAIL_LOCATOR = (By.XPATH,'//a[@href = "mailto:info@travelagency.com"]')

    HOTEL_BUTN_LOCATOR = (By.XPATH, '//a[contains(text(),"Hotels")]')

    HOTEL_PAGE_MAIN_TEXT_LOCATOR =(By.XPATH, '//h2[contains(text(),"SEARCH FOR BEST HOTELS")]')



