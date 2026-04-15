from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def test_purchase():
    # 1. Откройте сайт магазина в FireFox
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # 2. Авторизуйтесь как пользователь standard_user
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # 3. Добавьте в корзину товары
    # Sauce Labs Backpack
    backpack = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    backpack.click()

    # Sauce Labs Bolt T-Shirt
    tshirt = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        )
    )
    tshirt.click()

    # Sauce Labs Onesie
    onesie = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))
    )
    onesie.click()

    # 4. Перейдите в корзину
    cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart.click()

    # 5. Нажмите Checkout
    checkout = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout.click()

    # 6. Заполните форму своими данными
    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    first_name.send_keys("Евгений")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Румянцев")

    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("152830")

    # 7. Нажмите кнопку Continue
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    # 8. Прочитайте со страницы итоговую стоимость (Total)
    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".summary_total_label")
        )
    )
    total_text = total_element.text
    # Извлекаем число из текста "Total: $58.29"
    total_value = total_text.replace("Total: ", "")

    # 9. Закройте браузер
    driver.quit()

    # 10. Проверьте, что итоговая сумма равна $58.29
    expected_total = "$58.29"
    assert total_value == expected_total, (
        f"Expected total {expected_total}, but got {total_value}"
    )


if __name__ == "__main__":
    test_purchase()
