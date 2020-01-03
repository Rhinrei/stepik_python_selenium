import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
browser.find_element_by_css_selector(".btn").click()

x_value = browser.find_element_by_css_selector("#input_value").text
result = calc(x_value)
browser.find_element_by_css_selector("#answer").send_keys(result)
browser.find_element_by_css_selector("#solve").click()
time.sleep(10)
browser.quit()

