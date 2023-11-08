import pyautogui
import win32con
import win32gui
import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

PYkeyboard = KeyboardController()
mouse = MouseController()

#Focus Bloons window
def focus_bloons_window(bloons_title):
    hwnd = win32gui.FindWindow(None, bloons_title)
    if hwnd:
        win32gui.SetForegroundWindow(hwnd)
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        print(f"{bloons_title} up")
    else:
        print("Failed")

#Village upgrade + placement
def m_village():
    pyautogui.moveTo(1555, 514)
    PYkeyboard.tap('k')
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.5)
    for i in range(2):
        PYkeyboard.tap(',')
        time.sleep(.1)
        i += 1
    print("Village up")

#Sniper upgrade + placement
def sniper():
    pyautogui.moveTo(1543, 606)
    PYkeyboard.tap('z')
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.5)
    for i in range(4):
        PYkeyboard.tap('/')
        time.sleep(.1)
        i += 1
    for i in range(2):
        PYkeyboard.tap('.')
        time.sleep(.1)
        i += 1
    print("Sniper up")

#Alchemist upgrade + placement
def alch():
    pyautogui.moveTo(1607, 630)
    PYkeyboard.tap('f')
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.5)
    for i in range(4):
        PYkeyboard.tap(',')
        time.sleep(.1)
        i += 1
    for i in range(2):
        PYkeyboard.tap('.')
        time.sleep(.1)
        i += 1
    print("Alch up")
    
run = True

app_title = "BloonsTD6"
focus_bloons_window(app_title)

#Playing the game
while run:
    time.sleep(1)
    m_village()
    time.sleep(.5)
    sniper()
    time.sleep(.5)
    alch()
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.1)
    for i in range(2):
        PYkeyboard.tap(Key.space)
        time.sleep(.1)
        i += 1
    run = False
    