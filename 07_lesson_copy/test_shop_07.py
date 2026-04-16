import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from page_login_07 import LoginPage
from page_inventory_07 import InventoryPage
from page_cart_07 import CartPage
from page_checkout_07 import CheckoutPage


def test_shop():
    """Тест магазина с Firefox (без фикстур для отладки)"""

    # Создание драйвера Firefox
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()

    try:
        print("\n🚀 НАЧАЛО ТЕСТА ИНТЕРНЕТ-МАГАЗИНА\n")

        # 1. Авторизация
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        print("✅ Авторизация выполнена")
        time.sleep(1)

        # 2. Добавление товаров
        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack()
        inventory_page.add_tshirt()
        inventory_page.add_onesie()
        print("✅ Товары добавлены в корзину")
        time.sleep(1)

        # 3. Переход в корзину
        inventory_page.go_to_cart()
        print("✅ Переход в корзину")
        time.sleep(1)

        # 4. Нажатие Checkout
        cart_page = CartPage(driver)
        cart_page.click_checkout()
        print("✅ Нажата кнопка Checkout")
        time.sleep(1)

        # 5. Заполнение формы (ваши данные)
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_first_name("Евгений")
        checkout_page.fill_last_name("Румянцев")
        checkout_page.fill_postal_code("152830")
        print("✅ Форма заполнена (Евгений Румянцев, 152830)")
        time.sleep(1)

        # 6. Продолжение
        checkout_page.click_continue()
        print("✅ Нажата кнопка Continue")
        time.sleep(2)

        # 7. Получение итоговой суммы
        total_value = checkout_page.get_total_value()
        print(f"💰 Итоговая сумма: {total_value}")

        # 8. Проверка
        expected_total = "$58.29"
        assert total_value == expected_total, \
            f"Expected {expected_total}, but got {total_value}"

        print("\n" + "=" * 50)
        print("✅ ТЕСТ ПРОЙДЕН УСПЕШНО!")
        print(f"📊 ИТОГОВАЯ СУММА: {total_value}")
        print("=" * 50 + "\n")

    finally:
        print("⏳ Закрытие браузера через 5 секунд...")
        time.sleep(5)
        driver.quit()
        print("✅ Браузер закрыт")


if __name__ == "__main__":
    test_shop()
