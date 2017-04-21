import kivy
kivy.require('1.9.2')

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

class Wid_Alfa(AnchorLayout):
	def __init__(self):
		super(Wid_Alfa,self).__init__()
		self.anchor_x = 'left'
		self.anchor_y = 'bottom'
	
class MainApp(App):
	title = 'AnchorLayout'
	def build(self):
		return Wid_Alfa()
		
if __name__ == '__main__':
	MainApp().run()
