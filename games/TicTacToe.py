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

class TicTacToe(App):
    player = 'X'
    def build(self):
        gr = GridLayout()
        gr.cols = 3
        gr.rows = 4
        gr.spacing = 10
        gr.padding = 10
        gr.size_hint = (1, 1)
        gr.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        gr.bind(minimum_height=gr.setter('height'), minimum_width=gr.setter('width'))
        for i in range(0, 9):
            btn = Button(text='', size_hint=(1, 1), font_size=40)
            btn.bind(on_press=self.button_press)
            gr.add_widget(btn)
        gr.add_widget(Button(text='restart', size_hint=(0.1, 0.1), font_size=40, on_press=self.restart))
        return gr
    def on_pause(self):
        return True
    def on_resume(self):
        pass
    def on_stop(self):
        pass
    def button_press(self, instance):
        if instance.text == '':
            instance.text = self.player
            if self.check_win():
                self.show_popup()
            self.player = 'X' if self.player == 'O' else 'O'
    def check_win(self):
        if self.check_rows():
            return True
        elif self.check_cols():
            return True
        elif self.check_diag():
            return True
        return False
    def check_rows(self):
        for row in range(0, 3):
            for i in range(0, 3):
                if not self.check_button(row, i):
                    return False
        return True
    def check_cols(self):
        for col in range(0, 3):
            for i in range(0, 3):
                if not self.check_button(i, col):
                    return False
        return True
    def check_diag(self):
        for i in range(0, 3):
            if not self.check_button(i, i):
                return False
        for i in range(0, 3):
            if not self.check_button(2-i, i):
                return False
        return True
    def check_button(self, row, col):
        btn = self.root.children[row*3+col]
        print(row*3+col)
        if btn.text == self.player:
            return True
        return btn.text == self.player
    def show_popup(self):
        content = Button(text='Close', size_hint=(1, 1))
        popup = Popup(title='Game Over', content=content, size_hint=(0.5, 0.5))
        content.bind(on_press=self.end(content,popup))
        popup.open()
    def end(self, instance, popup):
        popup.dismiss()
        self.restart()
    def restart(self, instance):
        self.root.clear_widgets()
        for i in range(0, 9):
            btn = Button(text='', size_hint=(1, 1), font_size=40)
            btn.bind(on_press=self.button_press)
            self.root.add_widget(btn)
        self.root.add_widget(Button(text='restart', size_hint=(0.1, 0.1), font_size=40, on_press=self.restart))
        self.player = 'X'


TicTacToe().run()