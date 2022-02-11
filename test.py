from pynput import keyboard, mouse
from win32 import win32gui, win32api
from win32gui import GetWindowText, GetForegroundWindow
import pyautogui
import win32con
import time
import cv2
import numpy as np
import os
import datetime
import ctypes


method = cv2.TM_SQDIFF_NORMED
one = cv2.imread('one.png')
two = cv2.imread('two.png')

def on_press(key):
    try:
        k = key.char
    except:
        k = key.name
    if k == "f24":
        return False
    if k == "insert":
        click(one)
        print(GetWindowText(GetForegroundWindow()))
    if k == "t":
        pruchod1()
        pruchod2()
        return False


def find(tamplate):
    screen = pyautogui.screenshot()
    screen.save('screen.png')
    img_rgb = cv2.imread('screen.png')
    result = cv2.matchTemplate(tamplate, img_rgb, method)
    os.remove('screen.png')
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)
    i = 0
    if(mn > 0.1):
        return -1, -1
    return mnLoc


def click(tamplate):
    MPx, MPy = find(tamplate)
    if(MPx == -1):
        return
    w, h = tamplate.shape[:-1]
    pyautogui.click(MPx+w/2, MPy + h/2)


def rotateR(angle):
    mouse_move_relative(angle*4.8527777, 0)


def rotateL(angle):
    mouse_move_relative(-angle*4.8527777, 0)


def look_up():
    mouse_move_relative(0, -1000)


def mouse_move_relative(dx, dy):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx), int(dy), 0, 0)


def move_forward(destination):
    pyautogui.keyDown("w")
    pyautogui.keyDown("shift")
    while(find(cv2.imread(str(destination) + '.png'))[0] == -1):
        time.sleep(0.1)
    pyautogui.keyUp("shift")
    pyautogui.keyUp("w")

def pruchod1():
    look_up()
    rotateL(45)
    move_forward(2)


def pruchod2():
    rotateR(50)
    move_forward(3)
def pruchod3():
    move_forward(4)

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
