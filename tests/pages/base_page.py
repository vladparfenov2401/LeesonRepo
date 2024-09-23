from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except:
            return False
        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*self.USER_ICON), "User icon is not presented, probably unauthorised user"
