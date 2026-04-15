from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Настройки браузера
options = Options()
options.add_argument("--start-maximized")

# Укажи путь к chromedriver.exe
service = Service("C:/Users/Евгений/PycharmProjects/Python_HW/05_lesson/chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

try:
    # 1. Открыть страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # 2. Найти синюю кнопку
    # У кнопки динамический ID, поэтому ищем по тексту
    button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")

    # 3. Клик по кнопке
    button.click()

    # Пауза, чтобы увидеть результат
    time.sleep(2)

finally:
    driver.quit()
