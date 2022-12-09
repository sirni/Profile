import pyautogui
import time
time.sleep(7)
count=0
while count<20:
    pyautogui.typewrite("Automation Text"+str(count))
    pyautogui.press("enter")
    count=count+1