from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

    def add_product_to_basket(self):
        button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        # Получаем название товара на странице продукта
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        # Получаем цену товара на странице продукта
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def should_be_success_message(self, expected_product_name):
        # Проверка, что название товара в сообщении совпадает с добавленным товаром
        success_message = self.browser.find_element(*self.SUCCESS_MESSAGE).text
        assert expected_product_name == success_message, \
            f"Expected product name '{expected_product_name}' in the message, but got '{success_message}'"

    def should_be_correct_basket_total(self, expected_product_price):
        # Проверка, что стоимость корзины совпадает с ценой товара
        basket_total = self.browser.find_element(*self.BASKET_TOTAL).text
        assert expected_product_price == basket_total, \
            f"Expected basket total '{expected_product_price}', but got '{basket_total}'"
