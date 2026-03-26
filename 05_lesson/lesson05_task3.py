from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.add_argument("--width=1200")
options.add_argument("--height=800")

driver = webdriver.Firefox(options=options)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    input_field = driver.find_element(By.TAG_NAME, "input")

    input_field.send_keys("12345")
    time.sleep(1)

    input_field.clear()
    time.sleep(1)

    input_field.send_keys("54321")
    time.sleep(2)

finally:
    driver.quit()
