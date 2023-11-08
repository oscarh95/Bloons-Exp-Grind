import cv2
import numpy as np
import pyautogui
import win32con
import win32gui
import pygetwindow as pw
import threading
import time
import sys
from PIL import ImageGrab
from pynput.keyboard import Key, Listener, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

loop_bool = True

def on_press(key):
    global loop_bool
    if key == Key.esc:
        print("Exito")
        loop_bool = False
        
#Focus Bloons window   
def focus_bloons_window(bloons_title):
    hwnd = win32gui.FindWindow(None, bloons_title)
    if hwnd:
        win32gui.SetForegroundWindow(hwnd)
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        print(f"{bloons_title} up")
    else:
        print("Failed")

#Screenshot application
def capture_bloons(bloons_window):
    bloons = pw.getWindowsWithTitle(bloons_window)[0]
    
    sc = ImageGrab.grab(bbox=(bloons.left, bloons.top, bloons.right, bloons.bottom))
    sc = sc.convert('RGBA') #save with bit depth 32
    sc.save('imgs/bloonswindow.png')

def menuing(image_name):
    capture_bloons(app_title)

    bloons_menu_img = cv2.imread('imgs/bloonswindow.png', cv2.IMREAD_UNCHANGED)

    easy_img = cv2.imread(fr'imgs/{image_name}.PNG', cv2.IMREAD_UNCHANGED)

    w = easy_img.shape[1]
    h = easy_img.shape[0]

    match_play_template = cv2.matchTemplate(bloons_menu_img, easy_img, cv2.TM_CCOEFF_NORMED)

    _, max_val, _, max_loc = cv2.minMaxLoc(match_play_template)
    #print(f'Confidence value: {max_val} \nBest location: {max_loc}')
    
    cv2.rectangle(bloons_menu_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,0), 2)
    center = (max_loc[0] + w//2, max_loc[1] + h//2)
    x = center[0]
    y = center[1]
    
    threshold = .80
    if max_val >= threshold:
        pyautogui.click(x=x, y=y)
    else:
        print("Confidence value too low")
        sys.exit()

#Village upgrade + placement
def m_village():
    pyautogui.moveTo(1555, 514)
    keyboard.tap('k')
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.5)
    for i in range(2):
        keyboard.tap(',')
        time.sleep(.1)
        i += 1
    print("Village up")

#Sniper upgrade + placement
def sniper():
    pyautogui.moveTo(1543, 606)
    keyboard.tap('z')
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.5)
    for i in range(4):
        keyboard.tap('/')
        time.sleep(.1)
        i += 1
    for i in range(2):
        keyboard.tap('.')
        time.sleep(.1)
        i += 1
    print("Sniper up")

#Alchemist upgrade + placement
def alch():
    pyautogui.moveTo(1607, 630)
    keyboard.tap('f')
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.5)
    for i in range(4):
        keyboard.tap(',')
        time.sleep(.1)
        i += 1
    for i in range(2):
        keyboard.tap('.')
        time.sleep(.1)
        i += 1
    print("Alch up")

app_title = "BloonsTD6"
focus_bloons_window(app_title)

listener_thread = threading.Thread(target=lambda: Listener(on_press=on_press).start())
listener_thread.start()

while loop_bool:
    #play
    menuing("play")
    print("Play condition cleared")
    time.sleep(.5)
    #expert
    menuing("expert")
    time.sleep(.5)
    print("Expert condition cleared")
    #infernal
    menuing("infernal")
    time.sleep(.5)
    print("Infernal condition cleared")
    #easy
    menuing("easy")
    time.sleep(.5)
    print("Easy condition cleared")
    #deflation
    menuing("deflation")
    time.sleep(5)
    print("Deflation condition cleared")
    #ok
    menuing("ok")
    time.sleep(1)
    print("Ok condition cleared")

    m_village()
    time.sleep(.5)
    sniper()
    time.sleep(.5)
    alch()
    time.sleep(.5)
    mouse.click(Button.left)
    time.sleep(.1)
    for i in range(2):
        keyboard.tap(Key.space)
        time.sleep(.1)
        i += 1
    print("Starto")

    #Wait for game to end
    minutes = 5
    print("Sleepy Time")
    time.sleep(minutes*60)
    focus_bloons_window(app_title)
    print("Wake the fuck up samurai")
    #Next
    menuing("next")
    print("Next condition cleared")
    time.sleep(1)
    #Home
    menuing("home")
    print("Home condition cleared")
    time.sleep(4)

listener_thread.join()
