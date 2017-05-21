import kivy
kivy.require('1.9.2')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.config import Config
Config.set('graphics', 'width', 300)
Config.set('graphics', 'height', 600)

class Wid_Animales(BoxLayout):
	nombre = 'Animales'
	wid1 = ObjectProperty(None)
	wid2 = ObjectProperty(None)
	
	def Accion(self):
		print self.wid1.text
		print self.wid2.text
		print self.ids['cangrejo'].text
	
	
class Wid_Frutas(BoxLayout):
	nombre = 'Frutas'
	
class MainApp(App):
	title = 'IDs app root self'
	def build(self):
		return Wid_Animales()
		
if __name__ == '__main__':
	MainApp().run()
