import time
import keyboard
import pyautogui

# Target/Last location
# FROM  642, 236
# TO    697, 263

# Previous Target
# FROM  706, 236
# TO    762, 261

# Inventory pos ->  1784, 163
# Select all items ->  1391, 298
# Sell item ->  1431, 733
# Hide Inventory ->  1106, 826

# CONSTANTS
BET_PLACED = False
FREEZE = False


def bet():
    time.sleep(0.2)
    pyautogui.click(945, 858)
    global BET_PLACED
    BET_PLACED = True


def set_multiplier(multiplier):
    pyautogui.click(686, 969)
    time.sleep(0.3)
    keyboard.write(str(multiplier))


def sell():
    time.sleep(0.2)
    pyautogui.click(1784, 163)
    time.sleep(0.2)
    pyautogui.click(1391, 298)
    time.sleep(0.2)
    pyautogui.click(1431, 733)
    time.sleep(0.2)
    pyautogui.click(1106, 826)
    time.sleep(0.2)


def freeze(seconds):
    global FREEZE
    FREEZE = False
    time.sleep(seconds)


def target_found(x1, y1, x2, y2):
    return pyautogui.locateOnScreen('target.png', region=(x1, y1, x2, y2), grayscale=True, confidence=0.99)


def place_bet_found(x1, y1, x2, y2):
    return pyautogui.locateOnScreen('place_bet.png', region=(x1, y1, x2, y2), grayscale=True, confidence=0.99)


def wait_for_next():
    if not target_found(642, 236, 50, 28):
        global BET_PLACED
        BET_PLACED = False
        return
    elif target_found(642, 236, 50, 28) and target_found(706, 236, 50, 20):
        global FREEZE
        BET_PLACED = False
        FREEZE = True


def wager_play():
    pass


def main():
    time.sleep(2)
    while True:
        if place_bet_found(840, 850, 235, 20):
            time.sleep(3)
            bet()
            time.sleep(0.5)
            set_multiplier(1.01)
            time.sleep(9.5)
        else:
            time.sleep(1)

        # global BET_PLACED
        # if target_found(642, 236, 50, 28):
        #     if BET_PLACED:
        #         wait_for_next()
        #     else:
        #         if FREEZE:
        #             freeze(120)
        #         else:
        #             time.sleep(0.2)
        #             #sell()
        #             set_multiplier(1.01)
        #             bet()
        # else:
        #     BET_PLACED = False


if __name__ == "__main__":
    main()
