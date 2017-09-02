import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App

from kivy.properties import ListProperty

class WidAlfa(FloatLayout):
	LVertices = ListProperty([400,300,0.5,0.5,200,500,0,0,600,500,1,0,600,100,1,1,200,100,0,1])
	
	def MoverImagen(self):
		self.LVertices[4] += 10
		self.LVertices[5] += 10
		
class MainApp(App):
	title = 'Vertex Instruction Mesh'
	def build(self):
		return WidAlfa()
		
if __name__ == '__main__':
	MainApp().run()
