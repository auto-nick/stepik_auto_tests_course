import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x_):
    return str(math.log(abs(12 * math.sin(int(x_)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".btn").click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(int(x))
    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(15)
    browser.quit()
