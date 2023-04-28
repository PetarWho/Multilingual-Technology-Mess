import pyautogui
import keyboard

while True:
    if keyboard.is_pressed('w'):
        x, y = pyautogui.position()
        r, g, b = pyautogui.pixel(x, y)

        print(f'{x}, {y} - {r}, {g}, {b}')
