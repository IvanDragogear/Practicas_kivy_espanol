import kivy
kivy.require('1.9.2')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Wid_Alfa(GridLayout):
	None
	
class GridRed(GridLayout):
	None

class GridBlue(GridLayout):
	None
	
class GridGreen(GridLayout):
	None

class MainApp(App):
	def build(self):
		return Wid_Alfa()
		
if __name__ == '__main__':
	MainApp().run() 
