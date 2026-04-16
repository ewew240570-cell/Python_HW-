from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    # Локаторы товаров
    BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT_BTN = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BTN = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self):
        """Добавить рюкзак в корзину"""
        btn = self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_BTN)
        )
        btn.click()

    def add_tshirt(self):
        """Добавить футболку в корзину"""
        btn = self.wait.until(
            EC.element_to_be_clickable(self.TSHIRT_BTN)
        )
        btn.click()

    def add_onesie(self):
        """Добавить Onesie в корзину"""
        btn = self.wait.until(
            EC.element_to_be_clickable(self.ONESIE_BTN)
        )
        btn.click()

    def add_all_items(self):
        """Добавить все три товара"""
        self.add_backpack()
        self.add_tshirt()
        self.add_onesie()

    def go_to_cart(self):
        """Перейти в корзину"""
        self.driver.find_element(*self.CART_LINK).click()
