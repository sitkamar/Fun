from pynput import keyboard, mouse
import pyautogui
import time
import cv2
import numpy as np
import os
from win32 import win32gui
from win32gui import GetWindowText, GetForegroundWindow

method = cv2.TM_SQDIFF_NORMED
current = set()
combinationnext = {'ctrl_l', 'enter', 'shift'}
cross = cv2.imread('cross.png')
nextpng = cv2.imread('next.png')
play = cv2.imread('play.png')
close = cv2.imread('close.png')
def on_press(key):
    try:
        k = key.char
    except:
        k = key.name
    if k == "pause":
        return False
    if GetWindowText(GetForegroundWindow()).find('Opera') != -1:
        if k in combinationnext:
            current.add(k)
            if all(i in current for i in combinationnext):
                doNext()
                time.sleep(0.5)
                doit()
        if k == "insert":
            doit()
    if GetWindowText(GetForegroundWindow()).find('Time Warpers') != -1:
        if k == "pause":
            return False
        if k == "insert":
            playWarpers()  
def on_release(key):
    try:
        k = key.char
    except:
        k = key.name
    try:
        current.remove(k)
    except KeyError:
        pass
def doit():
    click(cross)
    time.sleep(0.5)
    click(play)
    time.sleep(0.5)
    h1, h2 = find(close)
    if(h1 != -1):
        pyautogui.keyDown('ctrl')
        pyautogui.press('w')
        pyautogui.keyUp('ctrl')
    time.sleep(0.5)
    for i in range(2):
        click(play)
        time.sleep(0.5)
        h1, h2 = find(close)
        if(h1 != -1):
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')
        time.sleep(0.5)
    pyautogui.press('f')
def doNext():
    time.sleep(2)
    pyautogui.press('esc')
    time.sleep(2)
    click(nextpng)
def find(tamplate):
    screen = pyautogui.screenshot()
    screen.save('screen.png')
    img_rgb = cv2.imread('screen.png')
    result = cv2.matchTemplate(tamplate, img_rgb, method)
    os.remove('screen.png')
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    i=0
    while(mn>0.1 and i<4):
        i+=1
        time.sleep(0.5)
        screen = pyautogui.screenshot()
        screen.save('screen.png')
        img_rgb = cv2.imread('screen.png')
        result = cv2.matchTemplate(tamplate, img_rgb, method)
        os.remove('screen.png')
        mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    if(mn>0.1):
        return -1,-1
    return mnLoc
def click(tamplate):
    MPx,MPy = find(tamplate)
    i=0
    w, h = tamplate.shape[:-1]
    pyautogui.click(MPx+w/2, MPy + h/2)
def playWarpers():
    stage = getStage()
    
def getStage():
    screen = pyautogui.screenshot()
listener2 = keyboard.Listener(on_press=on_press)
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join() 
