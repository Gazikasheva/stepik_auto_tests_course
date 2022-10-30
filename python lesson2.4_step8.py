from selenium import webdriver
from selenium.webdriver.common.by import By
#import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(x))))
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link='http://suninjuly.github.io/explicit_wait2.html'
    browser.get (link)
    price = WebDriverWait (browser,12).until (
        EC.text_to_be_present_in_element ((By.ID,'price'), ('$100'))
        )
    button = WebDriverWait (browser,12).until (
        element_to_be_clickable ((By.TAG_NAME, 'button'))
        )
    button.click ()
    x = int (browser.find_element (By.ID, 'input_value').text)
    y=calc (x)
    answer = browser.find_element (By.ID, 'answer').send_keys (str(y))

    submit_button = browser.find_element (By.ID, 'solve')
    browser.execute_script ("return arguments[0].scrollIntoView(true);", submit_button)
    #submit.click()
    #submit = webdriver (browser,12).until (
        #EC.element_to_be_clickable (submit_button)
    #)
    submit_button.click ()
    control=browser.switch_to.alert
    print (control.text)
finally:
    time.sleep (3)
    browser.quit ()