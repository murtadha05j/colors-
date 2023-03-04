import time

import pyautogui
time.sleep(5)

x=1
pyautogui.moveTo(458,653)

for i in range(200):


    time.sleep(x)
    pyautogui.click()
    pyautogui.rightClick()
    pyautogui.moveTo(551,494)
    pyautogui.click()
    time.sleep(x)
    pyautogui.press("enter")
    pyautogui.moveTo(693,413)
    pyautogui.click()
    pyautogui.moveTo(458,653)

    time.sleep(x)
    #pyautogui.scroll(34)
    pyautogui.drag()