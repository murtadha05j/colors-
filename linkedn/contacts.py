from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

service = Service(executable_path='C:/Users/steel/a.chromedriver.exe')
service.start()
time.sleep(2)
driver = webdriver.Remote(service.service_url)
driver.get("https://linkedin.com")
username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")
username.send_keys('knowledge7858d@gmail.com')
password.send_keys('Neodymium14460')
submit = driver.find_element(By.XPATH, "//button[@type='submit']")
driver.execute_script('arguments[0].click();',submit)

n_page=200
for n in range(40,n_page):
    driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=" + str(n))
    time.sleep(4)
    all_buttons =driver.find_elements(By.TAG_NAME, 'button')  # all buttons
    connect_buttons = [btn for btn in all_buttons if btn.text == 'Connect']  # connect buttons
    for btn in connect_buttons:
        driver.execute_script('arguments[0].click();', btn)
        time.sleep(2)
        send = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
        driver.execute_script('arguments[0].click();', send)
        close = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
        driver.execute_script('arguments[0].click();', close)
        time.sleep(2)




time.sleep(3000)