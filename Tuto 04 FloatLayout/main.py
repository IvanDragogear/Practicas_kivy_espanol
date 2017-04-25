import kivy
kivy.require('1.9.2')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class Wid_Alfa(FloatLayout):
	None
	
class MainApp(App):
	tittle = 'FloatLayout'
	def build(self):
		return Wid_Alfa()
		
if __name__ == '__main__':
	MainApp().run()
