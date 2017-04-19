import kivy
kivy.require("1.9.2")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Box01(BoxLayout):
	def __init__(self):
		super(Box01,self).__init__()
		self.add_widget(BoxRed())
		
class BoxRed(BoxLayout):
	None
	
class BoxGreen(BoxLayout):
	None
	
class BoxBlue(BoxLayout):
	None

class MainApp(App):
	title = "BoxLayout Metodo 3"
	def build(self):
		return Box01()
		
if __name__ == "__main__":
	MainApp().run()
