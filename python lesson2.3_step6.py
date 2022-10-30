from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
browser = webdriver.Chrome ()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get (link)
def calc(x):
    return str(math.log(abs(12*math.sin(x))))
try:
    browser.find_element (By.TAG_NAME, 'button').click ()
    new_window = browser.window_handles [1]
    browser.switch_to.window (new_window)
    x=int(browser.find_element (By.ID, 'input_value').text)
    y=str (calc (x))
    browser.find_element (By.ID, 'answer').send_keys (y)
    browser.find_element (By.TAG_NAME, 'button').click ()
    control=browser.switch_to.alert
    print (control.text)
finally:
    time.sleep (1)
    browser.quit ()