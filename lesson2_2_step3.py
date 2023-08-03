import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = int(browser.find_element(By.ID, "num1").text)
    num_2 = int(browser.find_element(By.ID, "num2").text)
    sum_ = sum((num_1, num_2))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(sum_))

    browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    time.sleep(10)
    browser.quit()
