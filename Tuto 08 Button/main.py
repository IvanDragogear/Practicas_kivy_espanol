import kivy
kivy.require('1.9.2')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Wid_Alfa(BoxLayout):
	def __init__(self):
		super(Wid_Alfa,self).__init__()
		self.add_widget(Wid_BoxPy())
		self.add_widget(Wid_BoxKv())
		
class Wid_BoxPy(BoxLayout):
	def __init__(self):
		super(Wid_BoxPy,self).__init__()
		self.Btn = Button(text="Agregar Py")
		self.add_widget(self.Btn)
		self.Btn.bind(on_press = self.add_btn)
	
	def add_btn(self,*arg):
		self.add_widget(Button(text="Btn Py"))
	
class Wid_BoxKv(BoxLayout):
	def add_btn(self,*arg):
		self.add_widget(Button(text="Btn Kv"))
	
class MainApp(App):
	title = "Button"
	def build(self):
		return Wid_Alfa()
		
if __name__ == "__main__":
	MainApp().run()
