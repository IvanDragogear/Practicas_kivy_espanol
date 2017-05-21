import kivy
kivy.require('1.9.2')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Wid_Alfa(BoxLayout):
	pass
	
class MainApp(App):
	title = "Label MarkUp"
	def build(self):
		return Wid_Alfa()
		
if __name__ == '__main__':
	MainApp().run()
