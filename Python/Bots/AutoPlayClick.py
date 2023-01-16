from pyautogui import *
import pyautogui
import keyboard
import win32api
import win32con
import asyncio

x = 1197
y = 840


async def click(x1, y1, duration):
    win32api.SetCursorPos((x1, y1))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    if duration > 0:
        await asyncio.sleep(duration)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


async def doit():
    if pyautogui.pixel(x, y)[0] == 0 and pyautogui.pixel(x, y)[1] == 0 and pyautogui.pixel(x, y)[2] == 0:
        await click(x, y+3, 0.1)


async def run():
    await asyncio.sleep(2)
    while not keyboard.is_pressed('q'):
        await doit()

asyncio.run(run())