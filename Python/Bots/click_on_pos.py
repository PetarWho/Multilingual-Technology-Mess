import pyautogui
import time

pos1 = (1606, 786)
pos2 = (868, 582)

time.sleep(3)
for x in range(0, 25):
    pyautogui.click(pos1[0], pos1[1])
    time.sleep(0.05)
    pyautogui.click(pos2[0], pos2[1])
    time.sleep(0.05)
