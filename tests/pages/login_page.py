from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")

    def register_new_user(self, email, password):
        self.browser.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.browser.find_element(*self.REGISTRATION_BUTTON).click()
