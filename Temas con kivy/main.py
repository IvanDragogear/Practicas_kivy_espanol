import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.config import Config

from styles.common import *

Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 640)

class MainWid(BoxLayout):
    title = StringProperty("My App")
    subtitle= StringProperty("Sub titulo")
    text = StringProperty("Hola soy texto")

class MainApp(App):
    title = "Styles"
    def build(self):
        return MainWid()
        
if __name__ == "__main__":
    MainApp().run()
