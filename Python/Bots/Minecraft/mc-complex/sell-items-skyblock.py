import random

import keyboard
import win32api
import win32con
import asyncio
import pyautogui


sell_pos = (960, 524)
confirm_pos = (908, 400)
colors = [139, 237, 176]


async def send(message):
    keyboard.write(message, 0.1)
    await asyncio.sleep(0.5)


async def click(x1, y1, duration):
    win32api.SetCursorPos((x1, y1))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    if duration > 0:
        await asyncio.sleep(duration)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


async def main():
    await asyncio.sleep(3)
    while True:
        keyboard.press_and_release("T")
        await asyncio.sleep(0.5)
        await send('/sell')
        keyboard.press_and_release("enter")
        await asyncio.sleep(2)
        if pyautogui.pixel(sell_pos[0], sell_pos[1])[1] == colors[1]:
            await click(sell_pos[0], sell_pos[1], 0.1)
            await asyncio.sleep(1)
            pyautogui.moveTo(confirm_pos[0], confirm_pos[1])
            await asyncio.sleep(0.3)
            await click(confirm_pos[0], confirm_pos[1], 0.1)
        else:
            keyboard.press_and_release("Escape")
        await asyncio.sleep(random.randint(300, 400))


asyncio.run(main())
