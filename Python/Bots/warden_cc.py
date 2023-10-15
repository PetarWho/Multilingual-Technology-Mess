import keyboard
import pyautogui

challenge_btn = (1342, 895)
first_pos = (1246, 539)
second_pos = (522, 438)
speed_up_btn = (1661, 721)
exit_btn = (931, 934)


def click(x, y, sleep_after_click_duration):
    pyautogui.click(x, y)
    if sleep_after_click_duration:
        pyautogui.sleep(sleep_after_click_duration)


pyautogui.sleep(3)
while not keyboard.is_pressed('q'):
    click(challenge_btn[0], challenge_btn[1], 2.7)
    click(first_pos[0], first_pos[1], 0.4)
    click(second_pos[0], second_pos[1], 0.1)
    click(second_pos[0], second_pos[1], 0.1)
    click(second_pos[0], second_pos[1], 0.1)
    click(second_pos[0], second_pos[1], 0.1)
    click(second_pos[0], second_pos[1], 0.1)
    click(speed_up_btn[0], speed_up_btn[1], 0.1)
    click(speed_up_btn[0], speed_up_btn[1], 40)
    click(exit_btn[0], exit_btn[1], 2.1)


