import pytest
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage

@pytest.mark.parametrize('offer', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_guest_can_add_product_to_basket(browser, offer):
    # url_4_2: str = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # url_4_3: str = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}")
    product_page.open()
    product_title = product_page.get_product_name()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()

    alert_text = product_page.browser.find_element(By.CLASS_NAME, "alertinner").text
    assert product_title in alert_text, (f"Что-то пошло не так, название продукта - {product_title} нет в тексте "
                                         f"уведомлений - {alert_text}")

@pytest.mark.exp
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, "https://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/")
    product_page.open()
    product_page.add_product_to_basket()

    assert product_page.is_not_element_present(By.CLASS_NAME, "alertinner")

@pytest.mark.exp
def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, "https://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/")
    product_page.open()

    assert product_page.is_not_element_present(By.CLASS_NAME, "alertinner")

@pytest.mark.exp
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser,
                               "https://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/")
    product_page.open()
    product_page.add_product_to_basket()

    assert product_page.is_disappeared(By.CLASS_NAME, "alertinner")
