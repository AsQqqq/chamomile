import pyautogui as p
import time

time.sleep(1)

while True:
    p.press("down")
    p.press("end")
    p.keyDown("shift")
    p.press("home")
    p.keyUp("shift")
    p.press("[")
    p.press("right")
    p.press("backspace")
    p.press("home")
    p.press("right")
    p.press("delete")
    p.press("delete")
    p.press("delete")

    # time.sleep(3)
