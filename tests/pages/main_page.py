import pytest
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage

class TestMainPage:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
        basket_page.should_be_empty_message()
