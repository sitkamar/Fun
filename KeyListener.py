from pyHook import HookManager
import time

class Keystroke_Watcher(object):
    def __init__(self):
        print("xd")
        self.hm = HookManager()
        self.hm.KeyDown = self.on_keyboard_event
        self.hm.HookKeyboard()


    def on_keyboard_event(self, event):
        print("haha")
        try:
            print(event.KeyID)
            if event.KeyID  == key_your_waiting_for:
                self.your_method()
        finally:
            return True

    def your_method(self):
        print("Keystroke_Watcher: You pressed the key you're looking for!")
        self.shutdown()
        pass

    def shutdown(self):
        self.hm.UnhookKeyboard()


watcher = Keystroke_Watcher()

    
