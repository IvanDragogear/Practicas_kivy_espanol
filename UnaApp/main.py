import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

#Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
#Config.set('input', 'mouse', 'mouse')

class WidAlfa(BoxLayout):
	tx = StringProperty('Gato')
	cl = ListProperty([1,1,1])
	
	def act1(self):
		self.tx = "Zorro"
		self.cl = [1,0,0]
	def act2(self):
		self.tx = "Perro"
		self.cl = [1,1,0]
	def act3(self):
		self.tx = "Gato"
		self.cl = [1,1,1]
	def act4(self):
		self.tx = "Kiwy"
		self.cl = [1,0,1]
	def act5(self):
		self.tx = "Cangrejo"
		self.cl = [0,1,1]
	def act6(self):
		self.tx = "Leon"
		self.cl = [0,1,0]
	def act7(self):
		self.tx = "Tigre"
		self.cl = [0,0,1]
	def act8(self):
		self.tx = "Oso"
		self.cl = [1,.5,.5]
	def act9(self):
		self.tx = "Elefante"
		self.cl = [.5,1,.5]

class MainApp(App):
	title = 'Botones'
	#use_kivy_settings=False
	def open_settings(*args):
		pass
		
	def build(self):
		return WidAlfa()
		
if __name__ == '__main__':
	MainApp().run()
