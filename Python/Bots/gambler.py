# 26, 30, 35 - multiplier
# 76, 71, 53 - last crash
# 0, 211, 82 - lets roll

import time
import pyautogui
import easyocr
import torch
print(torch.cuda.is_available())


def take_screenshot_and_read_text(x, y):
    # Take a screenshot
    screenshot = pyautogui.screenshot(region=(x, y, 100, 50))
    screenshot.save('screenshot.png')

    # Read text from the screenshot using EasyOCR
    reader = easyocr.Reader(['en'])
    result = reader.readtext('screenshot.png')

    if result:
        return result[0][1]  # Get the detected text
    else:
        return ""


def main():
    time.sleep(2)
    while True:
        # Capture the text from the first coordinate
        text = take_screenshot_and_read_text(76, 71)

        # Check if the text is "1.00"
        if text == "1.00":
            # Click on specified coordinates
            pyautogui.click(26, 30)
            pyautogui.typewrite("1.01")
            pyautogui.click(0, 211, 82)

        # Sleep for a while and repeat the process
        time.sleep(1)


if __name__ == "__main__":
    main()
