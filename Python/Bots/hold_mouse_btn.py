import random

import keyboard
import pyautogui
import asyncio


async def hold(button):
    if button == 0:
        pyautogui.mouseDown(button='left')
    elif button == 1:
        pyautogui.mouseDown(button='right')


async def release(button):
    if button == 0:
        pyautogui.mouseUp(button='left')
    elif button == 1:
        pyautogui.mouseUp(button='right')


async def main():
    await asyncio.sleep(3)
    button = 0
    while True:
        await hold(button)
        await asyncio.sleep(random.randint(25, 30))
    # keyboard.wait('p')
        await release(button)
        await asyncio.sleep(random.randint(20, 30))


asyncio.run(main())
