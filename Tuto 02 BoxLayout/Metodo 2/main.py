import kivy
kivy.require("1.9.2")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

#Notas:
#	add_widget() es el metodo que todos los widgets
#	tienen para contener otros widgets.
#No puedes agregar la misma instacia de un widget en el 
#	mismo widget mas de una vez, ni incluir ese widget en mas de 
#	un widget diferente.
#En kivy todo es un widgen incluidas las BoxLayouts

class Box01(BoxLayout):
	def __init__(self):
		super(Box01,self).__init__()
		self.BR = BoxRed()
		self.BG = BoxGreen()
		self.BB = BoxBlue()
		
		self.BR.add_widget(BoxBlue())
		self.BR.add_widget(BoxBlue())
		
		self.BG.add_widget(self.BB)
		self.BG.add_widget(BoxBlue())
		
		self.add_widget(self.BR)
		self.add_widget(self.BG)
		
class BoxRed(BoxLayout):
	None
	
class BoxGreen(BoxLayout):
	None
	
class BoxBlue(BoxLayout):
	None

class MainApp(App):
	title = "BoxLayout Metodo 2"
	def build(self):
		return Box01()
		
if __name__ == "__main__":
	MainApp().run()
