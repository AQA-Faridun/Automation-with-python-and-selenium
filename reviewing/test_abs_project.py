import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistrationForms(unittest.TestCase):
    def setUp(self):
        """Подготовка драйвера перед каждым тестом"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        """Закрытие драйвера после каждого теста"""
        self.driver.quit()

    def test_registration_form_1(self):
        """Тест для первой страницы регистрации"""
        self.driver.get("http://suninjuly.github.io/registration1.html")

        # Заполнение обязательных полей
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Иван")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Петров")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test@example.com")

        # Нажатие кнопки отправки
        self.driver.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Ожидание загрузки страницы с результатом
        time.sleep(1)

        # Получение текста результата
        welcome_text = self.driver.find_element(By.TAG_NAME, "h1").text

        # Проверка результата
        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!",
            f"Текст приветствия не совпадает. Получено: '{welcome_text}'"
        )

    def test_registration_form_2(self):
        """Тест для второй страницы регистрации"""
        self.driver.get("http://suninjuly.github.io/registration2.html")

        # Заполнение обязательных полей
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Иван")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Петров")
        self.driver.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test@example.com")

        # Нажатие кнопки отправки
        self.driver.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Ожидание загрузки страницы с результатом
        time.sleep(1)

        # Получение текста результата
        welcome_text = self.driver.find_element(By.TAG_NAME, "h1").text

        # Проверка результата
        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!",
            f"Текст приветствия не совпадает. Получено: '{welcome_text}'"
        )


if __name__ == "__main__":
    unittest.main()