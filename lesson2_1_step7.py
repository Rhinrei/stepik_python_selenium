import math
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

x_value = browser.find_element_by_css_selector("#treasure").get_attribute("valuex")
result = calc(x_value)
browser.find_element_by_css_selector("#answer").send_keys(result)
browser.find_element_by_css_selector("#robotCheckbox").click()
browser.find_element_by_css_selector("#robotsRule").click()
browser.find_element_by_css_selector(".btn").click()
time.sleep(10)
browser.quit()

