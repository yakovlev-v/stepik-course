from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

# try:


browser = webdriver.Chrome()
browser.get(link)

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))

browser.find_element_by_id("book").click()
# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)
x_element = browser.find_element_by_id("input_value").get_attribute()
x = x_element.text
y = calc(x)
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("solve").click()
