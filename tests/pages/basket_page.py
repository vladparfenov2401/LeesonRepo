from .base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*self.EMPTY_BASKET_MESSAGE), "Basket is not empty, but should be"

    def should_be_empty_message(self):
        assert self.browser.find_element(*self.EMPTY_BASKET_MESSAGE).text == "Your basket is empty.", "Empty basket message is not presented"

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except:
            return True
        return False
