import kivy 
kivy.require('1.9.1')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import DragBehavior
from kivy.app import App

from kivy.lang import Builder

# Drag Behavior: https://kivy.org/doc/stable/api-kivy.uix.behaviors.drag.html

STRING_STYLE = '''
<MainWid>:
	canvas:
		Color:
			rgb: 1,1,1
		Rectangle:
			pos: self.pos
			size: self.size
	DragWid:
		
			
<DragWid>:
	size_hint: None, None
	size: 100,100
	drag_rectangle: self.x, self.y, self.width, self.height
	canvas:
		Color:
			rgb: 1,0.3,0.3
		Rectangle:
			pos: self.pos
			size: self.size
'''

Builder.load_string(STRING_STYLE)

class MainWid(FloatLayout):
	pass

class DragWid(DragBehavior,BoxLayout):
	pass

class MainApp(App):
	title = "Drag and drop"
	def build(self):
		global mainwid 
		global app
		mainwid = MainWid()
		app = self
		return mainwid
		
if __name__ == "__main__":
	MainApp().run()
