from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    def add_product_to_basket(self) -> None:
        self.browser.find_element(by=By.CSS_SELECTOR, value=".btn-add-to-basket").click()

    def get_product_name(self) -> str:
        product_title: str = self.browser.find_element(by=By.CSS_SELECTOR, value=".product_main h1").text
        return product_title

    def get_product_price(self) -> str:
        product_price: str = self.browser.find_element(by=By.XPATH, value="(//p[@class='price_color'])[1]").text
        return product_price
