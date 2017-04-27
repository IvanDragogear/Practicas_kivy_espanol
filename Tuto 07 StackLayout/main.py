import kivy
kivy.require('1.9.2')

from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class Wid_Alfa(StackLayout):
	def __init__(self):
		super(Wid_Alfa,self).__init__()
		self.orientation = 'lr-tb' #LeftRight-TopBottom
		#self.orientation = 'lr-bt' #LeftRight-BottomTop
		#self.orientation = 'rl-tb' #RightLeft-TopBottom
		#self.orientation = 'rl-bt' #RightLeft-BottomTop
		#self.orientation = 'tb-lr' #TopBottom-LeftRight
		#self.orientation = 'bt-lr' #BottomTop-LeftRight
		#self.orientation = 'tb-rl' #TopBottom-RightLeft
		#self.orientation = 'bt-rl' #BottomTop-RightLeft
		for x in range(100):
			self.add_widget(Button(size_hint=[None,None,],
			size=[20+(x*5),50], text=str(x)))
		
	
class MainApp(App):
	title = 'StackLayout'
	def build(self):
		return Wid_Alfa()
		
if __name__ == '__main__':
	MainApp().run()
