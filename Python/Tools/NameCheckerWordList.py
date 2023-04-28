import itertools
import pyautogui
import asyncio
import keyboard


async def run_combinations():
    await asyncio.sleep(5)
    symbols = "0123456789abcdefghijklmnopqrstuvwxyz"

    last_word = None
    with open("last_word.txt", "r") as f:
        lines = f.readlines()
        if lines:
            last_word = lines[-1].strip()

    with open("words.txt", "r") as f:
        words = f.readlines()
        if last_word:
            index = words.index(last_word + "\n")
            words = words[index + 1:]

        # Only iterate over words starting with "m"
        words = [word.strip() for word in words if word.startswith("m")]

        for word in words:
            pyautogui.typewrite(word)
            print(word)

            await asyncio.sleep(3.5)

            # RED - 200, 10, 40
            # FULL SCREEN - 659, 523
            # Half Screen - 180, 534
            if not pyautogui.pixelMatchesColor(180, 534, (200, 10, 40)):
                with open("successful_combinations.txt", "a") as s:
                    s.write(word + "\n")
            with open("last_word.txt", "w") as f2:
                f2.write(word)

            for x in range(len(word)):
                pyautogui.press("backspace")

            if keyboard.is_pressed("f4"):
                break

            await asyncio.sleep(0.05)


async def main():
    task1 = asyncio.create_task(run_combinations())

    await task1


if __name__ == "__main__":
    asyncio.run(main())
