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

    ACCOUNT_TYPE_CUSTUMER_LOCATOR = (
    By.XPATH, '//Input[@Aria-Activedescendant = "Select2-Account_type-Result-Hjze-Customers"]')

    SIGNUP_BTN_LOCATOR = (By.XPATH, '//button[@type ="submit"]')

    SIGNUP_SUCCSES_LOCATOR = (By.XPATH, '//h5[contains(text(), "Login")]')

    LOGIN_BTN_LOCATOR = (By.XPATH, '//button/span[text() = "Login"]/..')


class MainPageLocatorHeader():
    CONTACT_PHONE_LOCATOR = (By.XPATH, '//a[@href = "tel:+1-234-56789"]')

    CONTACT_EMAIL_LOCATOR = (By.XPATH, '//a[@href = "mailto:info@travelagency.com"]')

    HOTEL_BUTN_LOCATOR = (By.XPATH, '//a[contains(text(),"Hotels")]')

    HOTEL_PAGE_MAIN_TEXT_LOCATOR = (By.XPATH, '//h2[contains(text(),"SEARCH FOR BEST HOTELS")]')

    FLIGHTS_BTN_LOCATOR = (By.XPATH,'//a[contains(text(),"flights")]')

    FLIGHTS_PAGE_MAIN_TEXT_LOCATOR = (By.XPATH,'//h2[contains(text(),"SEARCH FOR BEST FLIGHTS")]')

    TOURS_BTN_LOCATOR = (By.XPATH,'//a[contains(text(),"Tours")]')

    TOURS_PAGE_MAIN_LOCATOR = (By.XPATH,'//h2[contains(text(),"FIND BEST TOURS PACKAGES TODAY")]')

    CARS_BTN_LOCATOR = (By.XPATH,'//a[contains(text(),"cars")]')

    CARS_PAGE_MAIN_TEXT_LOCATOR = (By.XPATH, '//h2[contains(text(),"RENTAL BEST CARS TODAY")]')

    VISA_BTN_LOCATOR = (By.XPATH, '//a[contains(text(),"visa")]')

    VISA_PAGE_MAIN_TEXT_LOCATOR = (By.XPATH, '//h2[contains(text(),"Submit Your Visa Today!")]')

    BLOG_BTN_LOCATOR = (By.XPATH, '//a[contains(text(),"Blog")]')

    BLOG_PAGE_MAIN_TEXT_LOCATOR = (By.XPATH, '//h2[contains(text(),"PHPTRAVELS Blog")]')

    #dropdown page locator
    COMPANY_DROPDOWN_LOCATOR = (By.XPATH, '//button[@class = "drop-menu-toggler"]/../i')
    # temporary locators, if text will change need to change locator
    ABOUTUS_COMPANY_BTN = (By.XPATH, '//a[contains(text(),"About Us")]')

    ABOUTUS_PAGE_MAIN_TEXT = (By.XPATH, '//p[contains(text(),"PHPTRAVELS")]')

    TERMSOFUSE_COMPANY_BTN = (By.XPATH, '//a[contains(text(),"Terms of Use")]')

    TERMSOFUSE_PAGE_MAIN_TEXT = (By.XPATH, '//p[contains(text(),"This Website is")]')

    FAQ_COMPANY_BTN = (By.XPATH,'//a[contains(text(),"FAQ")]')

    FAQ_PAGE_MAIN_TEXT = (By.XPATH, '//h3[contains(text(),"FAQ")]')
    #end of temporary locators

class MainPageHeaderTABLocators():

    MAIN_TAB_LOCATOR = (By.XPATH, '//div[@class = "section-tab fade-in glass"]')

    HOTELS_TAB_LOCATOR = (By.XPATH, '//button[@id = "hotels-tab"]')

    FLIGHTS_TAB_LOCATOR = (By.XPATH,'//button[@aria-controls = "flights"]')

    FLIGHTS_TAB_PRESSENT_LOCATOR = (By.XPATH, '//div[@id = "onereturn"]')

    TOURS_TAB_LOCATOR = (By.XPATH, '//button[@id = "tours-tab"]')

    TOURS_TAB_PRESSENT_LOCATOR = (By.XPATH, '//form[@id = "tours-search"]')

    CARS_TAB_LOCATOR = (By.XPATH, '//button[@id = "cars-tab"]')

    CARS_TAB_PRESENT_LOCATOR = (By.XPATH, '//span[@id = "select2-carfrom-container"]')

    VISA_TAB_LOCATOR = (By.XPATH, '//button[@id = "visa-tab"]')

    VISA_TAB_PRESENT_LOCATOR = (By.XPATH, '//span[@id="select2-from_country-container"]')



