import pytest
from tests.pages.product_page import ProductPage
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    # Открываем страницу товара с разным параметром promo
    page = ProductPage(browser, link)
    page.open()

    # Получаем название и цену товара
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    # Добавляем товар в корзину
    page.add_product_to_basket()

    # Решаем задачу и получаем код
    page.solve_quiz_and_get_code()

    # Проверяем, что в сообщении правильное название товара
    page.should_be_success_message(product_name)

    # Проверяем, что цена корзины соответствует цене товара
    page.should_be_correct_basket_total(product_price)
