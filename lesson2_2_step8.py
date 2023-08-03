import time, os

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("petrov@email.com")

    browser.find_element(By.ID, "file").send_keys(os.path.join(os.path.dirname(__file__), 'foo.txt'))

    browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    time.sleep(15)
    browser.quit()
