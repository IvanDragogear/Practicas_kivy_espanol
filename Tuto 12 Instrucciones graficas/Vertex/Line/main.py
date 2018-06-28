import kivy
kivy.require('1.9.2')

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class Wid_Alfa(BoxLayout):
	pass
	
class MainApp(App):
	title = 'Line'
	def build(self):
		return Wid_Alfa()
		
if __name__ == '__main__':
	MainApp().run()
