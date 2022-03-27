from pynput import keyboard, mouse
import pyautogui
import pytesseract
import time
import cv2
import numpy as np
import screeninfo
import os
from threading import Thread
from win32 import win32gui
from win32gui import GetWindowText, GetForegroundWindow
from PIL import Image

method = cv2.TM_SQDIFF_NORMED
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\martin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
cross = cv2.imread('cross.png')
play = cv2.imread('play.png')
nextPng = cv2.imread('next2.png')
windows = []
timer = 0
playing= True

def find(tamplate):
    screen = pyautogui.screenshot()
    screen.save('screen.png')
    img_rgb = cv2.imread('screen.png')
    result = cv2.matchTemplate(tamplate, img_rgb, method)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)
    i = 0
    if(mn > 0.1):
        return -1, -1
    return mnLoc


def on_press2(key):
    global listener
    try:
        k = key.char
    except:
        k = key.name
    if k == "pause":
        playing = False
        listener.stop()
        return False


def on_press(key):
    global timer
    try:
        k = key.char
    except:
        k = key.name
    window = GetWindowText(GetForegroundWindow())
    if window.find('Opera') != -1:
        if window.find('Svetserialu.to') != -1:
            if k == "insert":
                doit()
            elif k == "delete":
                next()
                time.sleep(5)
                doit()
            elif k == "pause":
                listener.stop()
                return False
            elif k == 'home':
                time.sleep(1)
                while playing:
                    doit()
                    timing = 0
                    while timer != timing:
                        if not playing:
                            return False
                        time.sleep(60)
                        timing+=1
                    next()




def doit():
    global timer
    click(cross)
    time.sleep(0.5)
    windows = pyautogui.getAllWindows()
    currentWindow = GetWindowText(GetForegroundWindow())
    pos = pyautogui.position()
    while click(play):
        time.sleep(0.5)
        pos = pyautogui.position()
        if len(windows) != len(pyautogui.getAllWindows()):
            close()
        elif currentWindow != GetWindowText(GetForegroundWindow()):
            pyautogui.keyDown('ctrl')
            pyautogui.press('w')
            pyautogui.keyUp('ctrl')
        else:
            break
        time.sleep(0.5)
        pyautogui.moveTo(1,1)
    pyautogui.moveTo(pos)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(10, 10)
    time.sleep(0.5)
    try:
        timer = getTime()
        timer = timer.split(' / ')[1]
        timer = timer.split(':')[0]
    except:
        timer = 20
    

def close():
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')

def next():
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    time.sleep(0.5)
    pyautogui.click(200,200)
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    time.sleep(0.5)
    click(nextPng)
    time.sleep(1)

# def find(tamplate):
#     screen = pyautogui.screenshot()
#     screen.save('screen.png')
#     img_rgb = cv2.imread('screen.png')
#     result = cv2.matchTemplate(tamplate, img_rgb, method)
#     os.remove('screen.png')
#     mn, _, mnLoc, _ = cv2.minMaxLoc(result)
#     time.sleep(0.5)
#     screen = pyautogui.screenshot()
#     screen.save('screen.png')
#     img_rgb = cv2.imread('screen.png')
#     result = cv2.matchTemplate(tamplate, img_rgb, method)
#     os.remove('screen.png')
#     mn, _, mnLoc, _ = cv2.minMaxLoc(result)
#     if(mn > 0.1):
#         return -1, -1
#     return mnLoc


def click(tamplate):
    MPx, MPy = find(tamplate)
    w, h = tamplate.shape[:-1]
    if MPx != -1:
        pyautogui.click(MPx+h/2, MPy + w/2)
        return True
    else:
        return False


def getTime():
    x1, y1 = screeninfo.get_monitors()[0].width/10, screeninfo.get_monitors()[0].height-40
    x2, y2 = screeninfo.get_monitors()[0].width/6, screeninfo.get_monitors()[0].height
    screenshot = pyautogui.screenshot(
        'screenshot.png', region=(x1, y1, x2-x1, 40))
    img = Image.open('screenshot.png')
    return pytesseract.image_to_string(img)

def winEnumHandler(hwnd, ctx):
    global windows
    windows = []
    if win32gui.IsWindowVisible(hwnd):
        windows.append(GetWindowText(hwnd))


listener2 = keyboard.Listener(on_press=on_press2)
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener2.start()
listener2.join()
listener.join()
