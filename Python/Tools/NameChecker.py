import itertools
import pyautogui
import asyncio
import keyboard


async def run_combinations():
    await asyncio.sleep(5)
    symbols = "0123456789abcdefghijklmnopqrstuvwxyz"

    last_combination = None
    with open("last_combination.txt", "r") as f:
        lines = f.readlines()
        if lines:
            last_combination = lines[-1].strip()

    with open("successful_combinations.txt", "a") as f:
        if last_combination:
            last_index = list(itertools.product(symbols, repeat=3)).index(tuple(last_combination))
            combinations = list(itertools.product(symbols, repeat=3))[last_index + 1:]
        else:
            combinations = list(itertools.product(symbols, repeat=3))

        # Iterate through all possible 3-symbol combinations
        for combination in combinations:

            word = "".join(combination)

            pyautogui.typewrite(word)
            print(word)

            await asyncio.sleep(3)

            # RED - 200, 10, 40
            if not pyautogui.pixelMatchesColor(659, 523, (200, 10, 40)):
                f.write(word + "\n")

            with open("last_combination.txt", "w") as f2:
                f2.write(word)

            pyautogui.press("backspace")
            pyautogui.press("backspace")
            pyautogui.press("backspace")

            if keyboard.is_pressed("f4"):
                break

            await asyncio.sleep(0.05)


async def main():
    task1 = asyncio.create_task(run_combinations())

    await task1


if __name__ == "__main__":
    asyncio.run(main())
