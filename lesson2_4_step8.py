import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x_):
    return str(math.log(abs(12 * math.sin(int(x_)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(int(x))
    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(15)
    browser.quit()
