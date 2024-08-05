import win32api
import win32con
import asyncio
import pyautogui
from pynput.keyboard import Controller, Key
keyboard = Controller()


async def click(x1, y1, duration):
    win32api.SetCursorPos((x1, y1))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    if duration > 0:
        await asyncio.sleep(duration)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


async def jump_and_wait(delay=1):
    keyboard.press(Key.space)
    await asyncio.sleep(0.2)
    keyboard.release(Key.space)
    await asyncio.sleep(delay)


async def check_position_colors_full_match(pos, colors):
    return ((pyautogui.pixel(pos[0], pos[1])[0] == colors[0])
            and (pyautogui.pixel(pos[0], pos[1])[1] == colors[1])
            and (pyautogui.pixel(pos[0], pos[1])[2] == colors[2]))


async def rebirth():
    rebirth_pos = (730, 730)
    rebirth_panel_opened_indicator = (599, 267)
    rebirth_panel_opened_indicator_colors = [255, 140, 169]
    bar_end_pos = (1275, 660)
    bar_end_colors = [33, 212, 245]
    if await check_position_colors_full_match(rebirth_panel_opened_indicator, rebirth_panel_opened_indicator_colors):
        if pyautogui.pixel(bar_end_pos[0], bar_end_pos[1])[1] == bar_end_colors[1]:
            await asyncio.sleep(0.7)
            await click(rebirth_pos[0], rebirth_pos[1], 0.1)
            await asyncio.sleep(0.5)


async def collect_crystal():
    bar_end_pos = (1142, 600)
    bar_end_colors = [0, 204, 255]
    bar_verify_clicked_pos = (1100, 600)
    bar_verify_clicked_colors = [255, 255, 255]

    if await check_position_colors_full_match(bar_end_pos, bar_end_colors):
        await asyncio.sleep(0.5)
        await click(960, 680, 0.1)
        if await check_position_colors_full_match(bar_verify_clicked_pos, bar_verify_clicked_colors):
            await jump_and_wait(1)
            await jump_and_wait(1)


async def main():
    await asyncio.sleep(3)
    while True:
        await collect_crystal()


asyncio.run(main())
