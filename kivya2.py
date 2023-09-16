from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.graphics import Rectangle

class MyClass(BoxLayout):
    def __init__(self):
        super(MyClass, self).__init__()

        # self.orientation = 'vertical'
        #
        # self.command_label = Label(text="Enter command (start/stop/status/quit):")
        # self.command_input = TextInput(hint_text="Enter command", multiline=False)
        # self.result_label = Label()
        #
        # self.add_widget(self.command_label)
        # self.add_widget(self.command_input)
        # self.add_widget(self.result_label)
        #
        # self.command_input.bind(on_text_validate=self.check_command)

        background_image = Image(source='path_to_your_image.png')
        self.add_widget(background_image)

        self.engine_on = False

    def check_command(self, instance):
        command = instance.text

        if command == 'start':
            if self.engine_on:
                self.result_label.text = 'Engine is already started.'
            else:
                self.result_label.text = 'Starting the engine.'
                self.engine_on = True

        elif command == 'stop':
            if not self.engine_on:
                self.result_label.text = 'First start your engine.'
            else:
                self.result_label.text = 'Stopping the engine.'
                self.engine_on = False

        elif command == 'status':
            if self.engine_on:
                self.result_label.text = 'Engine is running.'
            else:
                self.result_label.text = 'Engine is off.'

        elif command == 'quit':
            self.result_label.text = 'Exiting the program.'
            App.get_running_app().stop()

        else:
            self.result_label.text = 'Invalid command.'

class CarEngineApp(App):
    def build(self):
        return MyClass()

CarEngineApp().run()