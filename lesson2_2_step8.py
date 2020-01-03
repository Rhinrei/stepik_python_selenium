from selenium import webdriver
import time, os

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("a@b.com")
    file_path = os.path.join(current_dir, 'doc.txt')
    browser.find_element_by_css_selector("#file").send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
