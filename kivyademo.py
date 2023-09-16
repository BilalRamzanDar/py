from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
        self.random_num = None

    def generate_number(self):
        self.random_num = random.randint(0, 9)
        self.random_label.text = "Generated Number: " + str(self.random_num)
        self.result_label.text = ""

    def check_guess(self):
        if self.random_num is None:
            return

        entered_num_str = self.entered_number_input.text
        if not entered_num_str:
            return

        try:
            entered_num = int(entered_num_str)
            if entered_num == self.random_num:
                self.result_label.text = "You won!"
            else:
                self.result_label.text = "You lost!"
        except ValueError:
            self.result_label.text = "Invalid input!"

class RandomNumberApp(App):
    def build(self):
        return MyRoot()

randomNumber = RandomNumberApp()
randomNumber.run()
