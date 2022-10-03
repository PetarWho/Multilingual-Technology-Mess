from pyautogui import *
import pyautogui
import keyboard
import win32api
import win32con
import asyncio

pos1 = 1050
pos2 = 1155
pos3 = 1260
pos4 = 1365
height = 390
height_lower = 500
hold_duration = 0

continue_video_color_min = [254, 165, 45]
continue_video_color_max = [254, 180, 55]


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


async def press_note(colors, pos):
    if continue_video_color_min[1] <= colors[1] <= continue_video_color_max[1] and continue_video_color_max[2] <= colors[2] <= continue_video_color_min[2]:
        quit()

    if colors[0] == 0 and colors[1] == 0:
        await click(pos, height, hold_duration)
    if 2 <= colors[1] <= 90:
        await click(pos, height, hold_duration)


async def press_note_lower(colors, pos):
    if continue_video_color_min[1] <= colors[1] <= continue_video_color_max[1] and continue_video_color_max[2] <= colors[2] <= continue_video_color_min[2]:
        quit()

    if colors[0] == 0 and colors[1] == 0:
        await click(pos, height_lower, hold_duration)
    if 2 <= colors[1] <= 20:
        await click(pos, height_lower, hold_duration)


async def run():
    await asyncio.sleep(2)
    while not keyboard.is_pressed('q'):
        await press_note(pyautogui.pixel(pos1, height), pos1)
        await press_note(pyautogui.pixel(pos2, height), pos2)
        await press_note(pyautogui.pixel(pos3, height), pos3)
        await press_note(pyautogui.pixel(pos4, height), pos4)

        await press_note_lower(pyautogui.pixel(pos1, height_lower), pos1)
        await press_note_lower(pyautogui.pixel(pos2, height_lower), pos2)
        await press_note_lower(pyautogui.pixel(pos3, height_lower), pos3)
        await press_note_lower(pyautogui.pixel(pos4, height_lower), pos4)

asyncio.run(run())
