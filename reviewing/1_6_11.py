from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_f_n = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input_f_n.send_keys("Ivan")
    input_l_n = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input_l_n.send_keys("Petrov")
    input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input_email.send_keys("ivan_petrov1997@mail.ru")
    input_phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
    input_phone.send_keys("+7 (123) 456-78-90")
    input_address = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
    input_address.send_keys("Russia, Smolensk, Lenina, 5-2")
    button_sbm = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button_sbm.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
