from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/registration2.html"
# browser = webdriver.Firefox()
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.XPATH, value="//input[@placeholder='Input your first name']").send_keys('Alex')
    browser.find_element(By.XPATH, value="//input[@placeholder='Input your last name']").send_keys('Alex')
    browser.find_element(By.XPATH, value="//input[@placeholder='Input your email']").send_keys('Alex@gmail.com')
    browser.find_element(By.XPATH, value="//input[@placeholder='Input your phone:']").send_keys('900900900')
    browser.find_element(By.XPATH, value="//input[@placeholder='Input your address:']").send_keys('Fifth Avenue at the intersection with 56th Street')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

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