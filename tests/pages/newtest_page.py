import pytest
from .pages.product_page import ProductPage

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    # Добавляем товар в корзину
    page.add_product_to_basket()

    # Проверяем, что сообщение об успехе не появляется
    assert page.is_not_element_present(*ProductPage.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    # Проверяем, что сообщения об успехе нет
    assert page.is_not_element_present(*ProductPage.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    # Добавляем товар в корзину
    page.add_product_to_basket()

    # Проверяем, что сообщение об успехе исчезает
    assert page.is_disappeared(*ProductPage.SUCCESS_MESSAGE), \
        "Success message did not disappear, but should have"
