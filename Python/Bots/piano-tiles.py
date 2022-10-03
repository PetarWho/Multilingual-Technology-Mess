from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import asyncio

# Point(1183, 420)
# Point(1283, 420)
# Point(1383, 420)
# Point(1483, 420)


async def click(x1, y1, duration):
    win32api.SetCursorPos((x1, y1))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    if duration > 0:
        await asyncio.sleep(duration)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


async def hold(x1, y1):
    win32api.SetCursorPos((x1, y1))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)


async def release():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


async def side1(p1):
    if p1[0] == 0 and p1[1] == 0:
        await click(1222, 420, 0.001)
    if 2 <= p1[1] <= 50:
        # await hold(1222, 420)
        await click(1222, 420, 0)
    # if 155 <= p1[1] <= 167 and 245 <= p1[2] <= 254:
    #     await release()


async def side2(p2):
    if p2[0] == 0 and p2[1] == 0:
        await click(1338, 420, 0.001)
    if 2 <= p2[1] <= 50:
        # await hold(1338, 420)
        await click(1338, 420, 0)
    # if 155 <= p2[1] <= 167 and 245 <= p2[2] <= 254:
    #     await release()


async def side3(p3):
    if p3[0] == 0 and p3[1] == 0:
        await click(1442, 420, 0.001)
    if 2 <= p3[1] <= 50:
        # await hold(1442, 420)
        await click(1442, 420, 0)
    # if 155 <= p3[1] <= 167 and 245 <= p3[2] <= 254:
    #     await release()


async def side4(p4):
    if p4[0] == 0 and p4[1] == 0:
        await click(1554, 420, 0.001)
    if 2 <= p4[1] <= 50:
        # await hold(1554, 420)
        await click(1554, 420, 0)
    # if 155 <= p4[1] <= 167 and 245 <= p4[2] <= 254:
    #     await release()
    # print(f'{p3[0]}, {p3[1]}, {p3[2]}')


async def run():
    await asyncio.sleep(2)
    while not keyboard.is_pressed('q'):
        p1 = pyautogui.pixel(1222, 420)
        p2 = pyautogui.pixel(1338, 420)
        p3 = pyautogui.pixel(1442, 420)
        p4 = pyautogui.pixel(1554, 420)

        await side1(p1)
        await side2(p2)
        await side3(p3)
        await side4(p4)

asyncio.run(run())
