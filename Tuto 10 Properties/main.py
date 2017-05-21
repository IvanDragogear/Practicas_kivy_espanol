import kivy
kivy.require('1.9.2')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, StringProperty
from kivy.properties import NumericProperty, BooleanProperty
from kivy.properties import ObjectProperty
from kivy.config import Config
Config.set('graphics', 'width', 300)
Config.set('graphics', 'height', 600)

class Wid_Alfa(BoxLayout):
	V_color = ListProperty([1,0,0])
	V_texto = StringProperty("Cambiar texto")
	V_size = NumericProperty(20)
	V_bold = BooleanProperty(False)
	
	#V_color = ObjectProperty([1,0,0])
	#V_texto = ObjectProperty("Cambiar texto")
	#V_size = ObjectProperty(20)
	#V_bold = ObjectProperty(False)
	
	def cambiarTexto(self):
		if self.V_texto == "Cambiar texto":
			self.V_texto = 'Otro texto'
		else:
			self.V_texto = "Cambiar texto"
	
	def cambiarColor(self):
		if self.V_color == [1,0,0]:
			self.V_color = [1,1,1]
		else:
			self.V_color =[1,0,0]
		print self.V_color

class MainApp(App):
	title = 'Preperties'
	def build(self):
		return Wid_Alfa()
		
if __name__ == '__main__':
	MainApp().run()
	
	
