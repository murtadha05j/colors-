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
time.sleep(2)
n_pages=20
for n in range(0,n_pages):

    driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&page=" + str(n))
    time.sleep(4)

    all_buttons = driver.find_elements(By.TAG_NAME,'button')
    message_buttons = [btn for btn in all_buttons if btn.text == 'Message']
    for i in range(0,len(message_buttons)):
        driver.execute_script('arguments[0].click();',message_buttons[i])
    #if message_buttons:
     #   message_buttons[0].click()
    #else:
     #   print("No 'Message' button found.")
    #paragraphs=driver.find_elements(By.TAG_NAME,'p')
    #counter=0
    #for p in paragraphs:
        #print(counter)
        #print(p.text)
        #counter+=1
    #print(paragraphs[-4].text)
    #print("done")
        time.sleep(4)
        main_div=driver.find_element(By.XPATH, "//div[starts-with(@class,'msg-form__msg-content-container')]")
        driver.execute_script('arguments[0].click();',main_div)
        # send messages
        paragraphs=driver.find_elements(By.TAG_NAME,'p')
        # extract names from linkedin contacts
        all_span = driver.find_elements(By.TAG_NAME, 'span')
        all_span = [s for s in all_span if s.get_attribute('aria-hidden') == 'true']  # select just the span that hidden
        idx = [*range(17, 57, 4)]  # i make this list through i mimic the loop a that i know from it the incrmenting index number
        greetings = ["hello", 'hi', 'hey']
        all_names=[]
        for j in idx:
            names = all_span[j].text.split(" ")[0]  # select the names and split it to select the first name
            all_names.append(names)
        greeting_idx = random.randint(0, len(greetings) - 1)
        my_message=", I am looking for a job, if you can help me to find one please contact with me."
        message= greetings[greeting_idx] + " " + all_names[i] + my_message
        paragraphs[-5].send_keys(message)
        time.sleep(4)
        submit1 = driver.find_element(By.XPATH, "//button[@type='submit']")
        driver.execute_script('arguments[0].click();',submit1)
        time.sleep(4)
        close_button=driver.find_element(By.XPATH, "//button[starts-with(@class,'msg-overlay-bubble-header__control artdeco-button artdeco-button')]")
        driver.execute_script('arguments[0].click();',close_button)

        time.sleep(4)

"""
# extract names from linkedin contacts
all_span=driver.find_elements(By.TAG_NAME,'span')
all_span=[s for s in all_span if s.get_attribute('aria-hidden')=='true'] # select just the span that hidden
idx=[*range(17,57,4)] # i make this list through i mimic the loop
greetings=["hello",'hi','hey','yo yo']
for i in idx:
    greeting_idx=random.randint(0,len(greetings)-1)
    names=all_span[i].text.split(" ")[0] # select the names and split it to select the first name
    print(greetings[greeting_idx]+ " " + names+  ", nice to meet you")

loop a
counter=0
that loop select all index in the contact names by counter variable and i.text
for i in all_span:
    print(counter)
    print(i.text)
    counter+=1
"""





time.sleep(3000)
