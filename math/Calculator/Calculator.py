from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class Calculator(App):
    pressedKeys = []
    def build(self):
        backround = GridLayout()
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down,on_key_up=self._on_keyboard_up)
        backround.cols = 1
        backround.rows = 2
        display = Label(text='', font_size=40, size_hint=(1, 0.5))
        display.color = (200, 0, 0, 1)
        backround.add_widget(display)
        gr = GridLayout()
        gr.cols = 5
        gr.rows = 4
        gr.spacing = 10
        gr.padding = 10
        gr.size_hint = (1, 1)
        gr.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        gr.bind(minimum_height=gr.setter('height'), minimum_width=gr.setter('width'))
        for i in range(4):
            for j in range(5):    
                btn = Button(text='', size_hint=(1, 1), font_size=40)
                btn.color = (200,0,0,1)
                if j < 3 and i<3:
                    btn.text = str(7 - i*3 + j)
                elif j==3 and i==2:
                    btn.text = '+'
                elif j==4 and i==2:
                    btn.text = '-'
                elif  j==3 and i==1:
                    btn.text = '*'
                elif j==4 and i==1:
                    btn.text = '/'
                elif j==3 and i==3:
                    btn.text = '='
                elif j==4 and i==3:
                    btn.text = 'C'
                elif j==0 and i==3:
                    btn.text = '.'
                elif j==1 and i==3:
                    btn.text = '0'
                elif j==2 and i==3:
                    btn.text = 'Del'
                elif j==3 and i==0:
                    btn.text = '('
                elif j==4 and i==0:
                    btn.text = ')'
                btn.bind(on_press=self.button_press)
                gr.add_widget(btn)
        backround.add_widget(gr)
        return backround
    def button_press(self,instance):
        if instance.text == 'C':
            self.root.children[1].text = ''
        elif instance.text == 'Del':
            self.root.children[1].text = self.root.children[1].text[:-1]
        elif instance.text == '=':
            try:
                self.root.children[1].text = str(eval(self.root.children[1].text))
            except:
                self.root.children[1].text = 'Error'
        else:
            self.root.children[1].text += instance.text
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.pressedKeys.append(keycode[1])
        if keycode[1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', '*', '/','(',')']:
            self.root.children[1].text += keycode[1]
        elif keycode[1] == 'backspace':
            self.root.children[1].text = self.root.children[1].text[:-1]
        elif keycode[1] in ['enter', '=']:
            try:
                self.root.children[1].text = str(eval(self.root.children[1].text))
            except:
                self.root.children[1].text = 'Error'
        elif keycode[1] == 'c':
            self.root.children[1].text = ''
        return True
    def _on_keyboard_up(self, keyboard, keycode):
        self.pressedKeys.remove(keycode[1])
        return True
Calculator().run()