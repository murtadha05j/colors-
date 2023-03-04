import time
import pyautogui
time.sleep(5)
t=0.001
z=0
for i in range(1000):
    z+=1
    if z ==7:
        z=0
    with open("words.txt", "r") as f:
        x = f.read().splitlines()
    pyautogui.moveTo(602, 625)
    time.sleep(t)
    pyautogui.click()
    # pyautogui.rightClick()
    # pyautogui.moveTo(665,473)
    # pyautogui.click()
    pyautogui.typewrite(x[z])
    pyautogui.press("enter")
    pyautogui.moveTo(806, 384)
    pyautogui.click()
    time.sleep(t)
    # pyautogui.scroll(34)
    pyautogui.drag()













