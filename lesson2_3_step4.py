import math
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_css_selector(".btn").click()
confirm = browser.switch_to.alert
confirm.accept()
x_value = browser.find_element_by_css_selector("#input_value").text
result = calc(x_value)
browser.find_element_by_css_selector("#answer").send_keys(result)
browser.find_element_by_css_selector(".btn").click()
time.sleep(10)
browser.quit()

