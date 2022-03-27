import pyautogui
import time
import pyautogui
from PIL import Image
import pytesseract
import os
import screeninfo
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\martin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def getTime():
    x1, y1 = screeninfo.get_monitors()[0].width/10, screeninfo.get_monitors()[0].height-40
    x2, y2 = screeninfo.get_monitors()[0].width/6, screeninfo.get_monitors()[0].height-40
    screenshot = pyautogui.screenshot(
        'screenshot2.png', region=(100, 1040, 400, 40))
    img = Image.open('screenshot2.png')
    return pytesseract.image_to_string(img)
time.sleep(1)
print(getTime())