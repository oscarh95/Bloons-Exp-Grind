import pyautogui
import win32con
import win32gui
import time
import logging
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()
logging.basicConfig(filename="tracker.log", level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - (message)s', 
                    datefmt='%b-%d-%y %H:%M:%S')
#Focus Bloons window
def focus_bloons_window(bloons_title):
    hwnd = win32gui.FindWindow(None, bloons_title)
    if hwnd:
        win32gui.SetForegroundWindow(hwnd)
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        logging.info(f"{bloons_title} up")
    else:
        logging.info("Failed")

def mouse_click():
        mouse.click(Button.left)
        time.sleep(.5)
        mouse.click(Button.left)

def monkey_placement(monke):
    #Village upgrade + placement
    if monke == "village":
        pyautogui.moveTo(1555, 514)
        keyboard.tap('k')
        time.sleep(.5)
        mouse_click()
        time.sleep(.5)
        for i in range(2):
            keyboard.tap(',')
            time.sleep(.1)
            i += 1
        logging.info("Village up")
    #Sniper upgrade + placement
    elif monke == "sniper":
        pyautogui.moveTo(1543, 606)
        keyboard.tap('z')
        time.sleep(.5)
        mouse_click()
        time.sleep(.5)
        for i in range(4):
            keyboard.tap('/')
            time.sleep(.1)
            i += 1
        for i in range(2):
            keyboard.tap('.')
            time.sleep(.1)
            i += 1
        logging.info("Sniper up")
    #Alchemist upgrade + placement
    elif monke == "alchemist":
        pyautogui.moveTo(1607, 630)
        keyboard.tap('f')
        time.sleep(.5)
        mouse_click()
        time.sleep(.5)
        for i in range(4):
            keyboard.tap(',')
            time.sleep(.1)
            i += 1
        for i in range(2):
            keyboard.tap('.')
            time.sleep(.1)
            i += 1
        logging.info("Alch up")
    else:
        logging.error("Wrong monkey")

run = True

app_title = "BloonsTD6"
focus_bloons_window(app_title)

#Playing the game
while run:
    time.sleep(1)
    monkey_placement("village")
    time.sleep(.5)
    monkey_placement("sniper")
    time.sleep(.5)
    monkey_placement("alchemist")
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.1)
    for i in range(2):
        keyboard.tap(Key.space)
        time.sleep(.1)
        i += 1
    run = False
    