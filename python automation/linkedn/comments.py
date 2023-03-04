from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import pyautogui

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
time.sleep(2)


driver.get("https://www.linkedin.com/search/results/CONTENT/?origin=FACETED_SEARCH&sid=t*N&sortBy=%22relevance%22")
time.sleep(4)
all_buttons = driver.find_elements(By.TAG_NAME,'button')
comment_buttons = [btn for btn in all_buttons if btn.text == 'Comment']
for i in range(0,len(comment_buttons)):
    driver.execute_script('arguments[0].click();',comment_buttons[i])
    time.sleep(4)
    main_div = driver.find_element(By.XPATH, "//div[starts-with(@class,'comments-comment-box-comment__text-editor')]")
    driver.execute_script('arguments[0].click();', main_div)
    # send messages
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')
    paragraphs[1].send_keys("j")
    time.sleep(2)
    submit1 = driver.find_element(By.XPATH, "//button[starts-with(@class,'comments-comment-box__submit-button')]")
    driver.execute_script('arguments[0].click();', submit1)
    print(i)
    time.sleep(4)
"""
    counter=0
    for p in paragraphs:
        print(counter)
        print(p.text)
        counter+=1
"""

time.sleep(3000)
