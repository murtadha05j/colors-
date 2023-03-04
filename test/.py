import time
import pyautogui
time.sleep(5)
t=0.001

for i in range(500):
    pyautogui.moveTo(602, 625)
    time.sleep(t)
    pyautogui.click()
    pyautogui.rightClick()
    pyautogui.moveTo(665,473)
    pyautogui.click()
    pyautogui.press("enter")
    pyautogui.moveTo(806, 384)
    pyautogui.click()
    time.sleep(t)
    # pyautogui.scroll(34)
    pyautogui.drag()


