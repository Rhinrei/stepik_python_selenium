from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

x_value = browser.find_element_by_css_selector("#input_value").text
result = calc(x_value)
browser.execute_script("window.scrollBy(0, 100);")
browser.find_element_by_css_selector("#answer").send_keys(result)
browser.find_element_by_css_selector("#robotCheckbox").click()
browser.find_element_by_css_selector("#robotsRule").click()
browser.find_element_by_css_selector(".btn").click()
time.sleep(10)
browser.quit()

