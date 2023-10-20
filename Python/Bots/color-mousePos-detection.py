import pyautogui
import keyboard

pressed = False
while True:
    try:
        if keyboard.read_key() == 'w':
            x, y = pyautogui.position()
            r, g, b = pyautogui.pixel(x, y)

            if pressed:
                print(f'Pos: {x}, {y} - RGB: {r}, {g}, {b}')
            pressed = not pressed
    except KeyboardInterrupt:
        pass
