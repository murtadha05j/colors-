import pyautogui
import time

time.sleep(5)
x=0.01
q=1
for i in range(20):
    time.sleep(x)
    pyautogui.moveTo(793, 571)
    pyautogui.click()
    pyautogui.scroll(-30)
    time.sleep(x)
    q+=1
    if q==200:
        time.sleep(240)
        q=0