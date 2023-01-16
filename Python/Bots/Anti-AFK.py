import asyncio
import pyautogui


async def go_to_library():
    x = 452
    y = 243
    pyautogui.click(x=x, y=y)


async def go_to_current():
    x = 755
    y = 826
    pyautogui.click(x=x, y=y)


async def main():
    while True:
        await asyncio.sleep(10)
        await go_to_library()
        await asyncio.sleep(5)
        await go_to_current()
        await asyncio.sleep(1800)


asyncio.run(main())
