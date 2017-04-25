import kivy
kivy.require('1.9.2')

from kivy.app import App
from kivy.uix.widget import Widget
#from kivy.uix.relativelayout import RelativeLayout

class Wid_Alfa(Widget):
	None

class MainApp(App):
	tittle = 'RelativeLayout'
	def build(self):
		return Wid_Alfa()
		
if __name__ == '__main__':
	MainApp().run()
