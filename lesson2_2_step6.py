import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x_):
    return str(math.log(abs(12 * math.sin(int(x_)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    print(x)
    y = calc(int(x))
    input_ = browser.find_element(By.ID, "answer")
    input_.send_keys(y)

    browser.find_element(By.ID, "robotCheckbox").click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, "robotsRule").click()
    button.click()

finally:
    time.sleep(15)
    browser.quit()
