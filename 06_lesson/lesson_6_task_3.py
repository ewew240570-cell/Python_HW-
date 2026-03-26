from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )
    wait = WebDriverWait(driver, 10)
    third_image = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img:nth-child(3)"))
    )
    images = driver.find_elements(By.TAG_NAME, "img")
    if len(images) >= 3:
        third_image_src = images[2].get_attribute("src")
        print("SRC 3-й картинки:", third_image_src)
    else:
        print(f"Ошибка: на странице найдено только {len(images)} картинок")
    print(f"Всего картинок на странице: {len(images)}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    driver.quit()
