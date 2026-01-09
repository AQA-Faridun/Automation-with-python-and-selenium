from time import sleep

from selenium.webdriver.common.by import By

def test_guest_should_see_add_to_basket_button(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    sleep(5)

    add_to_basket_button = browser.find_element(By.XPATH, "(//button[@type='submit'])[2]")

    assert add_to_basket_button.is_displayed(), "The “Add to cart” button is not displayed"